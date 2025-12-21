import math
def abs(a, b):
    return math.sqrt(a * a + b * b)


def mult(a1, b1, a2, b2):
    x = a1 * a2 - b1 * b2
    y = a1 * b2 + b1 * a2
    return x, y

def div(a1, b1, a2, b2):
    z = a2 * a2 + b2 * b2
    x = (a1 * a2 + b1 * b2) / z
    y = (b1 * a2 - a1 * b2) / z
    return x, y

m = abs(3, 4)
print(m)
x1, y1 = mult(3, 4, 1, -2)
print(x1, "+", y1, "i")
x2, y2 = div(3, 4, 1, -2)
print(x2, "+", y2, "i")
