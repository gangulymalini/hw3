print("Malini Ganguly - HW3")
print("Leap year code with error handling")

username = input("Enter year number (must be greater than 0): ")

while (username < 0):
    print("Please enter in a valid year!")
    username = input("Enter year number (must be greater than 0): ")


if (username % 400) == 0 :
    print(username, " is a leap year")
else:
    if (username % 100) == 0 :
        print(username, " is not a leap year")
    else:
        if (username % 4) == 0 :
            print(username, " is a leap year")
        else:
            print(username, " is not a leap year")