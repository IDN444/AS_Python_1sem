n = int(input())
sm = 0
factorial = 1
for i in range(1, n+1):
    factorial *= i
    sm += 1 / factorial
print(sm)
