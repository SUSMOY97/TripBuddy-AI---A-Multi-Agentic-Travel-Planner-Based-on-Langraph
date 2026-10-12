from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

#res = tavily_search("Best Hotels in India")

#print(res)

#print(search_flights("Plan a 7 days Japan trip from India"))

user_input = input("Enter Travel Request: ")
response = run_travel_agent(user_input=user_input,thread_id="test_user")

print(response["answer"])