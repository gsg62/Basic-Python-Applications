# Greg Geary

# Career Path Gamebook
print("Career Path Gamebook")
choice1 = input("Do you want to go to college after highschool? (yes/no)")
if choice1 == "yes":
    choice2 = input("What major do you want? (computer science or buisness)")
    if choice2 == "computer science":
        choice3 = input("Do you want to be a programmer or computer engineer?")
        if choice3 == "programmer":
            print("you will be a programmer")
        elif choice3 == "computer engineer":
            print("You will be a computer engineer")
    elif choice2 == "buisness":
        choice4 = input("Do you want to be an accountant or entrepreneur?")
        if choice4 == "accountant":
            print("You will be an accountant")
        elif choice4 == "entrepreneur":
            print("You will be an entrepreneur")
elif choice1 == "no":
    choice5 = input("Do you want to work restaurant or construction?")
    if choice5 == "restaurant":
        choice5 = int(input("How many hours do you want"
                            " to work a week?(20/30/40)"))
        if choice5 == 20:
            print("You will make about $16000 a year")
        elif choice5 == 30:
            print("You will make around $24000 a year")
        elif choice5 == 40:
            print("You will make around $31000 a year")
    elif choice6 == "construction":
        print("The average construction worker makes around $31000 a year")
