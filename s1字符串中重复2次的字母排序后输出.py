s='Wow,Today is Very Fine!'
s=s.replace(' ','')#去除空格
i=0
cf2c=''
while i<len(s):
    if s.count(s[i])==2: #选出重复两次的
        if s[i] in cf2c:
            i+=1
            continue
        cf2c+=s[i]
    i+=1
print('重复的元素有：%s'%cf2c)
#建立列表并排序
l=list(cf2c)
l.sort()
print(l)
for pr in l: #遍历列表并输出
    print (pr)

