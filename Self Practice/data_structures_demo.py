# This program shows how to use some basic ways to store collections of data in Python.

# 1. List: A list is an ordered collection of items, and you can change it after creating it.
# Think of it like a shopping list where you can add or remove items.
print("--- List Example ---")
my_list = [1, "hello", 3.14, "hello"] # A list can hold different types of items
print("Original list:", my_list)

# Add an item to the end
my_list.append("world")
print("List after adding 'world':", my_list)

# Remove the first occurrence of an item
my_list.remove("hello")
print("List after removing 'hello':", my_list)

# Access an item by its position (index starts from 0)
print("Item at index 1:", my_list[1])
print("\n")


# 2. Tuple: A tuple is also an ordered collection, but you cannot change it after creating it.
# Think of it like a fixed list of coordinates (latitude, longitude) that shouldn't change.
print("--- Tuple Example ---")
my_tuple = (10, 20, "apple", 20) # Tuples use parentheses ()
print("Original tuple:", my_tuple)

# You can access items by index, just like lists
print("Item at index 2:", my_tuple[2])

# Count how many times an item appears
print("Count of 20 in tuple:", my_tuple.count(20))

# Trying to change a tuple will cause an error (uncomment the line below to see)
# my_tuple[0] = 5 # This line will raise a TypeError
print("\n")


# 3. Set: A set is an unordered collection of unique items. No duplicates allowed.
# Think of it like collecting unique stamps - you only keep one of each kind.
print("--- Set Example ---")
my_set = {1, 2, 3, "banana", 2, 1} # Sets use curly braces {}
print("Original set (duplicates removed):", my_set)

# Add an item (if it's not already there)
my_set.add("orange")
print("Set after adding 'orange':", my_set)

# Remove an item
my_set.remove(3)
print("Set after removing 3:", my_set)

# Check if an item is in the set
print("Is 'banana' in the set?", "banana" in my_set)
print("\n")


# 4. Dictionary: A dictionary stores data in key-value pairs. Each key must be unique.
# Think of it like a real dictionary where each word (key) has a definition (value).
print("--- Dictionary Example ---")
my_dict = {"name": "Alice", "age": 30, "city": "New York"} # Dictionaries also use {} but with key:value pairs
print("Original dictionary:", my_dict)

# Access a value using its key
print("Name:", my_dict["name"])

# Add a new key-value pair
my_dict["job"] = "Engineer"
print("Dictionary after adding job:", my_dict)

# Change the value associated with a key
my_dict["age"] = 31
print("Dictionary after changing age:", my_dict)

# Remove a key-value pair
del my_dict["city"]
print("Dictionary after removing city:", my_dict)

print("\nFinished demonstrating basic data structures!")
