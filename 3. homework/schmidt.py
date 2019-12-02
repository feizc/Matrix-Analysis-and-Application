import numpy as np
import math

def norm(u):
	return math.sqrt(u.T.dot(u))


#返回QR
def SM(a):
	n=a.shape[0]
	q=a
	r=np.eye(n)
	for j in range(n):
		for i in range(j):
			r[i][j]=q[:,i].T.dot(a[:,j])
			q[:,j]-=r[i][j]*q[:,i]

		r[j][j]=norm(q[:,j])
		q[:,j]=q[:,j]/r[j][j]

	return q,r