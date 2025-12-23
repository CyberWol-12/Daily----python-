print("Welcome to the slider")
height = int(input("What is your height?"))
bill = 0

if height >= 120:
    print("You are allowed to do")
    age = int(input("What is exactly your age?"))
    if age <= 34:
        bill += 23
        print("You are allowed")
    elif 45 <= age <= 55:
        bill += 34
        print("you are also allowed ")
    else:
        bill += 23
        print("You are suppose to allow")

    want_photo = input("Do you want to take a picture? y or n"
                       "")
    if want_photo == "Y":
        bill += 3

    print(f"your overall bill:${bill}")
else:
    print("sorry, first you have to be taller before you can ride")

