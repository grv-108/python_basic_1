# 137. Extract Dictionary Pair

# Write a Python program to extract a single key-value pair from a dictionary into variables.

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

iterable = iter(person.items())

first_entry = next(iterable)

print(first_entry)