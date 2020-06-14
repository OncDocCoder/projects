import matplotlib.pyplot as plt
import math

x = [1, .866, 1.414/2, 0.5, 0, -0.5, -1.414/2, -.866, -1 ]
y = [0, 0.5, 1.414/2, 0.866, 1, 0.866, 1.414/2, .5, 0]


# for item in range(180):
#     v = math.radians(item)
#     z = math.sqrt(1 - (math.cos(item)**2))
#     x.append(v)
#     y.append(z)


plt.plot(x, y, color = 'red', marker = 'o')
plt.xlabel('x- axis', color = 'orange')
plt.ylabel('y- axis', color = 'pink')
plt.title('My first graph', color = 'green')
plt.show()