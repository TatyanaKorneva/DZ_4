def decomposition_prime_numbers(s):
f=[]
x=2
while (x<=s):
    if s%x==0:
        f.append(x)
        s=s/x
    else:
        x +=1

    return f
s=int(input())
print(decomposition_prime_numbers(s))
