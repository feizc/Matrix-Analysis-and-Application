import numpy as np
import math

def norm(u):
	return math.sqrt(u.T.dot(u))

def reflector(u):
	l=(u.T).dot(u)
	#print(u.dot(u.T))
	return np.eye(u.shape[0])-2/l*u.dot(u.T)

# 返回矩阵P和T
def HOUSE(a):
	n=a.shape[0]
	b=a
	r=np.eye(n)
	for i in range(n-1):
		u=b[i:,i].copy()
		u[0]=u[0]-norm(u)
		u=np.array([u])
		rr=reflector(u.T)
		#print(rr)
		r_total=np.eye(n)
		r_total[i:,i:]=rr
		#print(r_total)
		r=r_total.dot(r)
		b=r_total.dot(b)
	return r,b









