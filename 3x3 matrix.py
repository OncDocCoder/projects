#det   |a b c| j          |e f|           |d f|           |d e|
     # |d e f| k = a * det |h i| - b * det |g i| + c * det |g h|
     # |g h i| l

# a = 2
# b = -3
# c = 1
# d = 2
# e = 0
# f = -1
# g = 1
# h = 4
# i = 5



a = int(input('the value for a'))
b = int(input('the value for b'))
c = int(input('the value for c'))
d = int(input('the value for d'))
e = int(input('the value for e'))
f = int(input('the value for f'))
g = int(input('the value for g'))
h = int(input('the value for h'))
i = int(input('the value for i'))
j = int(input('the value for j'))
k = int(input('the value for k'))
l = int(input('the value for l'))

print('{}x+ {}y+ {}z=  {}'.format(a, b, c, j))
print('{}x+ {}y+ {}z= {}'.format(d, e, f, k))
print('{}x+ {}y+ {}z= {}'.format(g, h, i, l))

denom_det = a * ((e *i) - (h * f)) - b * ((d *i) - (g * f)) + c * ((d *h) - (g * e))

x_det = j * ((e *i) - (h * f)) - b * ((k *i) - (l * f)) + c * ((k *h) - (l * e))
y_det = a * ((k *i) - (l * f)) - j * ((d *i) - (g * f)) + c * ((d *l) - (g * k))
z_det= a * ((e *l) - (h * k)) - b * ((d *l) - (g * k)) + j * ((d *h) - (g * e))
print('the determinant is {}.'.format(denom_det))
print('the determinant x is {}.'.format(x_det))
print('the determinant y is {}.'.format(y_det))
print('the determinant z is {}.'.format(z_det))

xval = x_det/denom_det
yval = y_det/denom_det
zval = z_det/denom_det
print('the solution is {}, {}, {}'.format(xval, yval, zval))
