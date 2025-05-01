rows = int(input("\n Enter the no of rows: "))
steps = int(input("\n Enter the no of Steps: "))
counter =1
for i in range(1,rows,steps):
    if not (steps+i-1) > rows:
        print(f"Proper Set:")
        print(f"Set_{counter}: [{i}]-[{steps+i-1}]")
        counter += 1
    else:
        print(f"\nInadequate Set:")
        print(f"Set_{counter}: [{i}]-[{rows}]")
        #print((steps+i-1))
        print(f"To form a Set of {steps} items, Set_{counter} requires {(steps+i-1)-rows} elements")

print("_" * 50)

