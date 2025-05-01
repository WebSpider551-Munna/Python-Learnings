rows = int(input("\n Enter the no of rows: "))
steps = int(input("\n Enter the no of Steps: "))

for count, i in enumerate(range(1, rows, steps), start=1):
    end = min(i + steps - 1, rows)
    print(f"\n{'Proper' if end == i + steps - 1 else 'Inadequate'} Set:")
    print(f"Set_{count}: [{i}]-[{end}]")
    if end < i + steps - 1:
        print(f"To form a Set of {steps} items, Set_{count} requires {i + steps - 1 - rows} elements")

print("_" * 50)
