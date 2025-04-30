def powersum(n, m):
    a = str(n**m)
    result = 0
    for i in a:
        result = result + int(i)
    return result

powersum(2,1000)
    
