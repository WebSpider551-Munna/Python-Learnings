#working with math functions and if else statements.
# Choice:1 Area of a Circle = πr^2
# Choice:2 Circumference of a Circle = 2πr

import math

choice = int(input("\nChoose:\n1:Area of a Circle \n2:Circumference of a Circle: "))

radius = float(input("\nEnter the radius of the circle: "))

if choice == 1:
    area = math.pi * radius ** 2
    print(f"\nThe Area of the Circle is: {area:.2f}\n")
elif choice == 2:
    circumference = 2 * math.pi * radius
    print(f"\nThe Circumference of the Circle is: {circumference:.2f}\n")
else:
    print(f"\nInvalid Choice! Please choose 1 or 2")
# End of Code

