import numpy as np
def curve(points):
	x = points[:,0]
	y = points[:,1]

	z = np.polyfit(x, y, 2)
	f = np.poly1d(z)

	x_n = np.linspace(x[0], x[-1], 100)
	y_n = f(x_n)
	return list(zip(x_n, y_n))
