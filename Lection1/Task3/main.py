temp = float(input("Enter temperature: "))
deg = input("Enter C or F: ")

if deg == "C":
    print("Result:", "%.1f" % ((temp) * 1.8 + 32), "F")
if deg == "F":
    print("Result:", "%.1f" % (((temp) - 32) / 1.8), "C")
