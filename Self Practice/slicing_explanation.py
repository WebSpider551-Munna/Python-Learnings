# String slicing explanation

text = "Hello, Python!"

# Accessing a single character
first_char = text[0]  # Access the first character (index 0)
print(f"First character: {first_char}")

# Slicing a substring
substring = text[7:13]  # Get characters from index 7 up to (but not including) 13
print(f"Substring: {substring}")

# Slicing from the beginning
start_slice = text[:5]  # Get characters from the beginning up to (but not including) index 5
print(f"Start slice: {start_slice}")

# Slicing to the end
end_slice = text[7:]  # Get characters from index 7 to the end
print(f"End slice: {end_slice}")

# Slicing with a step
step_slice = text[::2]  # Get every second character
print(f"Step slice: {step_slice}")

# Reversing a string
reversed_text = text[::-1]  # Reverse the string
print(f"Reversed text: {reversed_text}")

# Combining start, end, and step
combined_slice = text[1:10:2]  # Start at index 1, end before index 10, take every second character
print(f"Combined slice: {combined_slice}")
