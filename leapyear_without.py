print("Malini Ganguly - HW3")
print("Leap year code without error handling")


username = input("Enter year number: ")

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