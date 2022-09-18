from sympy import simplify
from sympy.abc import x, y
f = open('Многочлены1.txt', 'r', encoding='cp1251')
l = open('Многочлены2.txt','r', encoding='cp1251')
m=f.readlines()[0]
n=l.readlines()[0]
a = m+'+'+n
print(simplify(a))
my_file = open("BF.txt", "w+")
my_file.write(a)
my_file.close()
