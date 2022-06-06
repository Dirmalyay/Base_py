while True:
    a = input("Enter R: ")
    try:
        a = int(a)
        if a <= 0:
            print("Value must be more then 0.")
        else:
            break
    except ValueError:
        print("Error")

res = 3.14 * (a ** 2)
print(res)
