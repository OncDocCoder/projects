import math

n = input('do you want to figure out the sine(S), cosine(C) or tangent(T)').lower()
print(n)
if n == 's':
    b = int(input('how many degrees?'))
    a = math.radians(b)
    x = math.sin(a)

    print('the sin of {} is {:.4f}'.format(a, x))

elif n == 'c':
    b = int(input('how many degrees?'))
    a = math.radians(b)
    y = math.cos(a)
    print('the cos of {} is {:.4f}'.format(a, y))

elif n == 't':
    b = int(input('how many degrees?'))
    a = math.radians(b)
    z = math.tan(a)
    print('the tan of {} is {:.4f}'.format(a, z))
else:
    print('you input the wrong letter')

print('calculate the sin value if you know the lengths of the sides')
o = int(input('Enter the opposite side length'))
h = int(input('Enter hypotenuse length'))


opposite = o
hypotenuse = h
sin = opposite/hypotenuse
print('sin is opposite/hypotenuse or {} / {} with solution {}'.format(opposite, hypotenuse, sin))

print('calculate the angle if you know the value of sine ')
v = float(input('value of sine'))
u = math.asin(v)
r = math.degrees(u)
print('The angle is {:.4f} degrees'.format(r))

print('calculate the cos value if you know the lengths of the sides')
adjacent = int(input('Enter the adjacent side length'))
hypotenuse = int(input('Enter hypotenuse length'))
cos = adjacent/hypotenuse
print('cos is adjacent/hypotenuse or {} / {} with solution {}'.format(adjacent, hypotenuse, cos))

#cotang = cos of x / sin of x

