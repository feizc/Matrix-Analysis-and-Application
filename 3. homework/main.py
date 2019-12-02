import numpy as np
from givens import GIVENS
from householder import HOUSE
from schmidt import SM
from lu import LU

data=np.loadtxt('matrix.txt')
print(data)

with open('parameter.txt','r') as f:
	a=f.readline()
	a=f.readline()
	print("分解类型为：",a)
	if a[0]=='G':
		p,t=GIVENS(data)
		print(p.T)
		print(t.astype(int))
	elif a[0]=='H':
		p,t=HOUSE(data)
		print(p.T)
		print(t.astype(int))
	elif a[0]=='S':
		q,r=SM(data)
		print(q)
		print(r)

	elif a[0]=='L':
		l,u,p=LU(data)
		print(l)
		print(u)
		print(p)
	else:
		print("参数设置错误！")


#p,t=GIVENS(data)
#print(p.T)
#print(t.astype(int))

#p,t=HOUSE(data)
#print(p.T)
#print(t.astype(int))

#q,r=SM(data)
#print(q)
#print(r)

#LU(data)