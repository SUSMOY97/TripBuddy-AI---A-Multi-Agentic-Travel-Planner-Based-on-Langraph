import uuid
from langchain_core.messages import HumanMessage
from backend import travel_graph

query = "Plan a 4-day trip from Kolkata to Goa in December, mid-range budget"
config = {"configurable": {"thread_id": str(uuid.uuid4())}}

# 1. Stream: watch each agent finish, one by one
for step in travel_graph.stream(
    {"user_query": query, "messages": [HumanMessage(content=query)]},
    config,
    stream_mode="updates",
):
    for node, update in step.items():
        print(f"\n===== {node} finished =====")
        for key, value in update.items():
            if key != "messages":
                print(f"{key}: {str(value)[:300]}")   # first 300 chars only

# 2. Inspect the final state
state = travel_graph.get_state(config).values
print("\n===== CHECKS =====")
print("flight_results filled:", bool(state.get("flight_results")))
print("hotel_results filled: ", bool(state.get("hotel_results")))
print("itinerary filled:     ", bool(state.get("itinerary")))
print("llm_calls:            ", state.get("llm_calls"))   # should be 4
print("messages count:       ", len(state["messages"]))   # should be 5 (1 human + 4 agent)

print("\n===== FINAL ANSWER =====")
print(state)
print(state["messages"][-1].content)
