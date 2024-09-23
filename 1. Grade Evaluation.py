number = float(input("Enter Your Score: "))

if number <= 90 and number >= 100:
    print("A")
elif number < 90 and number >= 80:
    print("B")
elif number < 80 and number >= 70:
    print("C")
elif number < 70 and number >= 60:
    print("D")
else:
    print("F")
