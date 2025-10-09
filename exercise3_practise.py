name=input("What is your name? ")
gpa=float(input("What is your GPA(0.0-4.0)? "))
TCH=int(input("Your total credit hours: "))
print(name)
if gpa >= 3.5 and TCH>=12:
    print("Congratulations! You are not in dean's list!")
    print("You do not need more GPA and credit hours!")
else:
    if gpa>=3.5 and TCH<12:
        print('You are dean\'s list!')
        print("You do not need more GPA")
        print(f"You need {12-TCH} credits.")
    elif gpa<3.5 and TCH>=12:
        print("You are dean's list")
        print(f"You need {3.5-gpa:.1f} GPA points")
        print("You do not need more credits")
    else:
        print(f"You need {3.5-gpa:.1f} GPA points")
        print(f"You need {12-TCH} credits.")