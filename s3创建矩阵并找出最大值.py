import numpy as np
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
new_data=[]
for i in range(len(a)):
    new_data.append(max(a[i]))

print('矩阵a的最大值为:%s'%max(new_data))

