for x in range(100,500):
    bai = x // 100
    shi = x % 100 // 10
    ge = x % 10
    if x == bai**3 + shi**3 + ge**3:
        print(x)
        
for y in range(1000,5000):
    qian = y // 1000
    bai = y % 1000 // 100
    shi = y % 100 // 10
    ge = y % 10
    if y ==qian**4 + bai**4 + shi**4 + ge**4:
        print(y)
        
