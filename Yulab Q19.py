## 1990.1.1是星期一，且不是闰年，那么1991.1.1就是星期二(365%7 = 1)
## 现在就是要算1991.1.1-2000.12.31里有多少个周日是每个月的第一天
## 不妨定义星期一就是0，以7为一个循环,如果每个月的第一天是星期天，计数变量就递增1，然后计算下一个月的第一天，重复判断

def fun(n1, n2):
    a = [31,28,31,30,31,30,31,31,30,31,30,31]
    day = 6
    sunday_counts = 0


    for i in range(n1, n2+1):
        if (i%4 == 0 and i%100 != 0) or (i%400 == 0):
            a[1] = 29
        else:
            a[1] = 28
        
        for month in range(12):
            if day == 6:
                sunday_counts += 1
            
            day = (day+ a[month]) % 7
    return sunday_counts

result = fun(1901, 2000)
print(result)
        



