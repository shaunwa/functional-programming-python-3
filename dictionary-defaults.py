person = { "name": "Shaun", "age": 123, "hair_color": "brown" }

def get_value_with_default(dictionary, key, default_value):
    if key in dictionary:
        return dictionary[key]
    else:
        return default_value

def get_value_partial(key, default_value):
    def inner(dictionary):
        return get_value_with_default(dictionary, key, default_value)

    return inner

get_name = get_value_with_default("entity_name", "")
get_age = get_value_with_default("age", 0)

get_name(person)
get_name(dog)
get_name(building)
get_name(location)
