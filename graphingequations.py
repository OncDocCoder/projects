
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return ((x**2)/49 + (y**2)/16) -100


delta = 1
x = np.linspace(-7.5, 7.5, 50 )
y = np.linspace(-4, 4, 50)
X, Y = np.meshgrid(x, y)


#eqn = ((x)**2)/9 + ((y)**2)/16
Z = f(X,Y)
# Z1 = np.exp(-X**2 - Y**2)
# Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
# Z = (Z1 - Z2) * 2

plt.contour(X, Y, Z, colors = 'blue' )
plt.xlim([-12, 12])
plt.ylim(-10, 10)
plt.show()