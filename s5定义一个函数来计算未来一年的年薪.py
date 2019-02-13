def calsalary():
    msg = '请输入姓名：'
    name = input(msg)
    msg = '请输入目前的年薪：'
    salary_now = int(input(msg))
    if salary_now < 40000:
        salary_add = salary_now*0.05
    else: 
        salary_add = 20000 + (salary_now-40000)*0.05

    salary_new = salary_now + salary_add
    msg = '%s新一年的年薪是：%s'%(name,salary_new)
    print(msg)


calsalary()
