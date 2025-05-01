# Function to generate Fibonacci sequence up to n terms
def fibonacci(n):
  # Initialize the first two Fibonacci numbers
  a, b = 0, 1
  # Iterate n times to generate the sequence
  for _ in range(n):
    # Yield the current Fibonacci number
    yield a
    # Update the next two Fibonacci numbers
    a, b = b, a + b

# Print the first 10 Fibonacci numbers on a single line
print("First 10 Fibonacci numbers:")
# Create a generator object and iterate through it, printing each number followed by a space
for number in fibonacci(10):
  print(number, end=' ')
# Print a final newline character after the loop
print()
