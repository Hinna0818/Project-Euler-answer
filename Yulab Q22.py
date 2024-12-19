## 先把文件读进来，然后根据字母顺序排序一下，返回一个列表，最后计算每个值对应的得分
def fun(dir):
    with open(dir, 'r') as f:
        content = f.read()
    
    names = content.replace('"', '').split(',')

    ## 按照字母表排序
    names.sort()

    ## 计算每个名字的分值
    totals = 0
    for i in range(len(names)):
        points = 0
        for j in range(len(names[i])):
            if 'A' <= names[i][j] <= 'Z':
                points += ord(names[i][j]) - ord('A') + 1   ## 使用ASCII码来计算每个字母对应的位置
        totals += points * (i+1)
    
    return totals

fun('names.txt')
        

                