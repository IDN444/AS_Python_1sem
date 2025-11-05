n = [1,2,3,4,5,6]
for i in range(len(n)):
    if n[i] % 2 != 0:
        n[i] = 0
print(n)
