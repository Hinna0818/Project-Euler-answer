<<<<<<< HEAD
def fun():
    a = []
    i = 1
    while len(a) < 1000000:
        a.extend(str(i))
        i += 1
    a = ''.join(a)
    return int(a[0]) * int(a[9]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999])

=======
def fun():
    a = []
    i = 1
    while len(a) < 1000000:
        a.extend(str(i))
        i += 1
    a = ''.join(a)
    return int(a[0]) * int(a[9]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999])

>>>>>>> 3f15ab277c139ecdfe2bf6b799f4f01d1a658c42
print(fun())