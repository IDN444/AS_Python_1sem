n = [1,2,9,4,5,3,7,8,6]
n3 = []
for i in range(len(n)):
    if n[i] % 3 == 0:
        n3.append(n[i])
n3.sort()
print(n3)
