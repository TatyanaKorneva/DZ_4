import random
q=int(input())
t=[]
for i in range(0,q+1):
    t.append(random.randrange(0,20))
    random.shuffle(t)
print(set(t))
