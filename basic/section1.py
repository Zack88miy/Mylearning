# 1-1
import math
print('1-1')
a = 123
print(a)

#黄金比
ans = (math.sqrt(5) + 1) / 2
print(ans)
print('\n')

#1-2
print('1-2')
h = 188.0
w = 104.0

w / (h/100.0) ** 2

def bmi(height, weight):
    return weight / (height/100.0) ** 2
x = bmi(188.0,104.0)
print(x)

def ft_to_cm(f,i):
    return f * 30.48 + i * (30.48 / 12)

assert round(ft_to_cm(5,2) - 157.48, 6) == 0
assert round(ft_to_cm(6,5) - 195.58, 6) == 0

def quadratic(a,b,c,x):
    return a * x**2 + b * x + c

assert quadratic(1, 2, 1, 3) == 16
assert quadratic(1, -5, -2, 7) == 12

def heron(a,b,c):
    s = 0.5 * (a+b+c)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

heron(3,4,5)

def qe_disc(a, b, c):
    return b*b - 4*a*c

def qe_solution1(a, b, c):
    return (-b - math.sqrt(qe_disc(a, b, c))) / (2*a)

def qe_solution2(a, b, c):
    return (-b + math.sqrt(qe_disc(a, b, c))) / (2*a)

assert qe_disc(1, -2, 1) == 0
assert qe_disc(1, -5, 6) == 1
assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
assert round(qe_solution2(1, -5, 6) - 3, 6) == 0