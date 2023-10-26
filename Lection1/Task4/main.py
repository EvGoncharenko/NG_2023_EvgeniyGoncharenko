import math
sing = input("Choose a sign +,-,*,/,** or √: ")

match sing:
    case "+":
        numone = float(input("Enter the first number: "))
        numtwo = float(input("Enter the second number: "))
        print("Result:", (numone) + (numtwo))
    case "-":
        numone = float(input("Enter the first number: "))
        numtwo = float(input("Enter the secomd number: "))
        print("Result:", (numone) - (numtwo))
    case "*":
        numone = float(input("Enter the first number: "))
        numtwo = float(input("Enter the second number: "))
        print("Result:", (numone) * (numtwo))
    case "/":
        numone = float(input("Enter first the number: "))
        numtwo = float(input("Enter second the number: "))
        print("Result:", (numone) / (numtwo))
    case "**":
        num = float(input("Enter the number: "))
        deg = int(input("Enter degree: "))
        print("Result:", (num) ** (deg))
    case "√":
        num = int(input("Enter the number: "))
        print("Result:", math.isqrt(num))