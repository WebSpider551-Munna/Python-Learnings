# Import required function
from collections.abc import Hashable

print("==== Mutability & Hashability Check ====\n")

# Define the data types
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_set = {1, 2, 3}
my_dict = {"name": "Anvith", "age": 5}

# Check if object is hashable
def check_hashable(obj):
    return isinstance(obj, Hashable)

# Try changing the object (to check mutability)
def test_mutability(obj, obj_type):
    try:
        if obj_type == "tuple":
            obj[0] = 100  # Tuples are immutable
        elif obj_type == "list":
            obj[0] = 100  # Lists are mutable
        elif obj_type == "set":
            obj.add(4)    # Sets are mutable
        elif obj_type == "dict":
            obj["age"] = 6  # Dicts are mutable
        return "Mutable ✅"
    except TypeError:
        return "Immutable ❌"

# Apply checks
objects = {
    "Tuple": my_tuple,
    "List": my_list,
    "Set": my_set,
    "Dictionary": my_dict
}

for name, obj in objects.items():
    print(f"{name}:")
    print(f"   ➤ Mutability: {test_mutability(obj, name.lower())}")
    print(f"   ➤ Hashable: {'✅' if check_hashable(obj) else '❌'}")
    print()
