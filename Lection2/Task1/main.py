num = int(input("How many elements do you want to enter into the list?: "))

userlist = []
index = 0

while index < num:
    userlist.append(int(input()))
    index += 1

 
print(userlist)