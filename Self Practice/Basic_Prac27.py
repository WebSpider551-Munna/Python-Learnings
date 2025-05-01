# Program to demonstrate the usage of Lists[] and Tuples()
# List[]: Mutable, can be changed
# Tuple(): Immutable, cannot be changed

#List1 = [1, 2, 3, 4, 5]
#List1[2] = 20
#List1[0] = 10
#print(f"List1: {List1}\n")
#
#List2 = ["Apple", "Banana", "Cherry"]
#List2[2] = "UPDATED FRUIT"
#print(f"List1: {List2}\n")
#
#Tuple1 = (1, 2, 3, 4, 5)
##Tuple1[2] = 20
#print(f"Tuple1: {Tuple1}\n")
#
#print("*" * 50)
#
#a=10
#name="Python"
#floatvalue=10.5
#complexvalue=3+4j
#
#print(f"a = {a}", type(a))
#print(f"name = {name}", type(name))
#print(f"floatvalue = {floatvalue}", type(floatvalue))
#print(f"complexvalue = {complexvalue}", type(complexvalue), "\n")
#print("*" * 50, "\n")

# program to demonstrate the usage of enumerate() function
# enumerate() function adds a counter to an iterable and returns it in a form of enumerate object
# enumerate(iterable, start=0)
# iterable: any object that supports iteration
# start: the index value from which the counter is to be started, by default it is 0

"""List3 = ["Apple", "Banana", "Cherry", "Dates", "Elderberry"]
print(f"List3: {List3}\n")
print(f"Enumerate List3: {list(enumerate(List3))}\n")
print(f"Enumerate List3: {list(enumerate(List3, 10))}\n")
print("*" * 50, "\n")"""

tuple2 = ("Apple", "Banana", "Cherry", "Dates")
print(f"tuple2: {tuple2}\n")
print(f"Enumerate tuple2: {list(enumerate(tuple2))}\n")
print(f"Enumerate tuple2: {list(enumerate(tuple2, 100))}\n")
print(enumerate(tuple2))
print(f"{list(enumerate(tuple2))}")
print("*" * 50, "\n")
print("*" * 50, "\n")

tuple3 = (1, 2, 3, 4, 5)
print(f"tuple3: {tuple3}\n")
print(f"Enumerate tuple3: {list(enumerate(tuple3))}\n")
print(f"Enumerate tuple3: {list(enumerate(tuple3, 100))}\n")
print(enumerate(tuple3))
print(f"{list(enumerate(tuple3))}")
print("*" * 50, "\n")
print("*" * 50, "\n")

