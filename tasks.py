import time
def a(t):
	z = []
	for x in range(len(t)):
		for y in range(len(t[x])):
			if t[x][y]==0:
				z.append((x,y))
	return z

def minimax(t,r=0):
	time.sleep(0.5)
	print t
	print a(t)
	return a(t)