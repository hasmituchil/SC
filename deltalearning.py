import math

x1 = [[2],[0],[-1]]
x2 = [[1],[-2],[-1]]
w1T = [[1,0,1]]


d1 = -1
d2 = -1
lamb = 1
c = 0.25

result = [[0],[0],[0]]


def net(X = [], Y = []):
	result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
	return result[0][0]
	
def dele(X = [], Y = []):
	result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
	for r in result:
		print (r)
	
	
def Oh(x, lamb):
	a = 1 + (math.e**(-1*lamb*x))
	O = (2/a)-1
	print("O1 value is {}".format(O))
	return O

def delw(c, d, O, X=[]):
	print(O)
	res = 0.5 * c * (d - O)
	print(res)
	res2 = 1 - (O**2)
	print(res)
	Ron = [[res * res2]]
	print(Ron[0][0])
	print(dele(X, Ron))
	

net1 = net(w1T , x1)
O1 = Oh(net1, lamb)

dw1 = delw(c, d1, O1, x1)

