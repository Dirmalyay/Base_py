def inp():
    name = input("Enter the name:")
    position = input("Enter position: ")
    age = input("Enter your age: ")
    with open("new.txt", 'a') as f:
        f.writelines(f"Name: {name}, position: {position}, age: {age}\n")

def out():
    with open("new.txt", 'r') as f:
        for line in f:
            print(line)

while True:
    menu = input(" 1. Input info\n 2. Print info\n 3. Stop\n Enter: ")
    if menu == "1":
        inp()
    elif menu == "2":
        out()
    elif menu == "3":
        break
    else:
        print("Wrong input")