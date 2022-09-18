import random
q=int(input())
t=[]
for i in range(1,q+1):
    t.append(i)
    random.shuffle(t)
k=len(t)
print(t)
for j in range(k):
    k=k-1
    if k>0 and k!=1:
        print(t[j],'*x','**',k, end='+',sep='')
    elif k==1:
        print(t[j],'*x', end='+',sep='')
    else:
        print(t[j], end='=0',sep='')
