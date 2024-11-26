sum = 0
a = 1
b = 2

while(a <= 4000000):
    if a % 2 == 0:
        sum = sum + a
    a, b = b, a+b

print(sum)
