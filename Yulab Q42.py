def fun(dir):
    f = open(dir, 'r')
    words = f.read().replace('"', '').split(',')
    dp = []
    triangle_num = [0.5*n*(n+1) for n in range(1000)]
    for letter in words:
        position = 0
        for i in letter:
            position += ord(i) - ord('A') + 1
        if position in triangle_num:
            dp.append(position)
    return len(dp)

fun('0042_words.txt')
