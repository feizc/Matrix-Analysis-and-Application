import numpy as np
import math

def row_change(a,i,j):
	if i==j:
		return
	else:
		tmp=a[i].copy()
		a[i]=a[j]
		a[j]=tmp

def LU(m):
	n=m.shape[0]
	l=np.zeros((n,n))
	a=np.zeros((n,n+1))
	a[0:,:-1]=m
	for i in range(n):
		a[i][n]=i

	for i in range(n):
		maxrow=i
		maxvalue=math.fabs(a[i][i])
		for j in range(i,n):
			value=math.fabs(a[j][i])
			if value>maxvalue:
				maxrow=j
				maxvalue=value
		row_change(a, i, maxrow)
		row_change(l, i, maxrow)
	#	print(a)
		for j in range(i+1,n):
			l[j][i]=a[j][i]/a[i][i]
	#		print(l[j][i])
			for k in range(i,n):
				a[j][k]-=a[i][k]*l[j][i]
	#	print(a)
	u=a[:,:-1]
	p=np.zeros((n,n))
	for i in range(n):
		p[i][int(a[i][n])]=1
	for i in range(n):
		l[i][i]=1
	return l,u,p


