#Task1
#validate use input exercie
#1.username is no more than 12 characters
#2.username should not contain any spaces
#3.username should not contain any digits

user_name = input("Enter your username: ")
if len(user_name) > 12:
    print("username should not be more than 12 characters")
#elif " " in user_name:
    #print("username should not contain any spaces")
elif user_name.find(" ") != -1:
    print("username should not contain any spaces")
elif any(char.isdigit() for char in user_name):
    print("username should not contain any digits")
else:
    print(" Welcome ", user_name,"\n")

#---------------------------------------------------------------
#Task2