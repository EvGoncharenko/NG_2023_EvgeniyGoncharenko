import math
sing = input("Choose a sign +,-,*,/,** or √: ")

if sing == "+" or sing == "-" or sing == "*" or sing == "/":
    numone = float(input("Enter the first number: "))
    numtwo = float(input("Enter the second number: "))
    match sing:
        case "+":
            print((numone) + (numtwo))
        case "-":
            print((numone) - (numtwo))
        case "*":
            print((numone) * (numtwo))
        case "/":
            print((numone) / (numtwo))
elif sing == "**" or sing == "√":
    match sing:
        case "**":
            num = float(input("Enter the number: "))
            deg = int(input("Enter degree: "))
            print((num) ** (deg))
        case "√":
            num = int(input("Enter the number: "))
            print(math.isqrt(num))
else:
    print("This sign is missing! Choose from the above")