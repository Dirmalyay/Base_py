a = input("Enter string: ")
l1 = []
count = 0
'''for i in a:
    count1 = a.count(i)
    if count1 > 1 and [i, count1] not in l1:
        l1.append([i, count1])
print(l1)'''

gen = [count += 1 for s in a if a.count(s) > 1 and s not in l1]
print(l1)