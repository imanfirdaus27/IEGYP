from City import City
from State import State

state_list = []
state_list.append(State("Tamilnadu",[]))
state_list.append(State("Andhra",[]))
state_list.append(State("Karnataka",[]))
state_list.append(State("Kerala",[]))

print("Enter City Details")
city_created_list = []
choice = "Yes"
while choice == "Yes" :
	city_name = input("Enter city name\n")
	state_name = input("Enter state name\n")
	state_found_flag = 0
	for state in state_list :
		if state_name == state.name :
			city = City(city_name, state)
			state.city_list.append(city)
			city_created_list.append(city)
			state_found_flag = 1
	if state_found_flag == 0 :
		state = State(state_name,[])
		state_list.append(state)
		city = City(city_name, state)
		city_created_list.append(city)
		state.city_list.append(city)
	choice = input("Do you want to add another city? Type Yes / No\n")

print("\nCity Details\n")
for city in city_created_list :
	print(city)

print("\nState Details\n")	
for state in state_list :
	print(state)