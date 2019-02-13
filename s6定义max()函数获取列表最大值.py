def max(l):
    if l == []:
        return (None,None)
    else:
        num_max = l[0]
    for i in l:
        if num_max < i:
            num_max = i
    return (num_max)


msg='请输入任意个数字，每个数字以英文字符逗号隔开：'
s=input(msg)
l=s.split(',')
l = [ int(x) for x in l ]
s=max(l)
print(s)
