import numpy as np
d=[]
b=list(map(int,raw_input().split()))
for i in range(b[0]):
    d.append(list(map(int, raw_input().split())))
print(np.array(d).T)
print(np.array(d).flatten())