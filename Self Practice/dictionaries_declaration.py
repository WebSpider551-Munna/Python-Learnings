# Example: Collecting key-value pairs into a dictionary
my_dict = {}  # Initialize an empty dictionary

for i in range(3):  # Adjust the range as needed
    key = input(f"Enter key {i+1}: ")  # Get input for the key
    value = input(f"Enter value for {key}: ")  # Get input for the value
    my_dict[key] = value  # Add the key-value pair to the dictionary

print("Stored dictionary:", my_dict)  # Print the dictionary
