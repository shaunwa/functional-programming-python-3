list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

combined_list = [0, *list_1, *list_2, 7]

print(combined_list)


dict_1 = { "a": 1, "b": 2 }
dict_2 = { "c": 3, "d": 4 }

combined_dict = { **dict_1, **dict_2 }
print(combined_dict)