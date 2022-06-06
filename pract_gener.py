pow = [x**5 for x in range(5, 26)]
print(pow)

gen = (x**5 for x in range(5, 26))
while True:
    print(next(gen))

print()



