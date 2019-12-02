import numpy as np
import math

def norm(x,y):
	m=math.sqrt(x*x+y*y)
	return x/m, y/m

def rotate_matrix(i,j,a):
	r=np.eye(a.shape[0])
	c,s=norm(a[i][i],a[j][i])
	r[i][i]=c
	r[i][j]=s
	r[j][i]=-s
	r[j][j]=c
	#print(r)
	return r

# 返回矩阵P和T
def GIVENS(a):
	n=a.shape[0]
	b=a
	p=np.eye(n)
	for col in range(n):
		for row in range(col+1,n):
			t=rotate_matrix(col,row,b)
			b=t.dot(b)
			p=t.dot(p)
		#	print(t)
		#	print(b)
		#	print(p)
	return p,b




