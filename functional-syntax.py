my_list = [1, 2, 3, 4, 5]

print(my_list)

my_new_list = my_list + [6]

print(my_new_list)

my_new_new_list = my_new_list + [7, 8]

print(my_list)
print(my_new_list)
print(my_new_new_list)

api_user_data = [{ "name": "Shaun", "age": 123 }, { "name": "Bob", "age": 54 }]

print(api_user_data)

user_names = [person["name"] for person in api_user_data]

print(user_names)