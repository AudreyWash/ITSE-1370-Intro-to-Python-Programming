name = input("Enter your name: ")

password = "Pas$Word"

first = True

while first:
    pwd = input("Enter your password: ")
    if pwd != password:
        print("Incorrect password, try again...")
    else:
        print("Welcom back," + name)
        break