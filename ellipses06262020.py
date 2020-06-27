#x2/a2 + y2/b2 = 1
import matplotlib
import math
import numpy as np
from matplotlib import pyplot as plt
from math import pi

# def draw_ellipse(h, v, a, b)
#
#     # h = 1.  # x-position of the center
#     # v = 0.5  # y-position of the center
#     # a = 2.  # radius on the x-axis
#     # b = 1.5  # radius on the y-axis




# a>b
# the length of the major axis is 2a
# the coordinates of the vertices are (±a,0)
# the length of the minor axis is 2b
# the coordinates of the co-vertices are (0,±b)
# the coordinates of the foci are (±c,0)
# , where c2=a2−b2.

#(x-h)^2/a^2 + (y-v)^2/b^2 = 1 horizontal
#center is (h, v)
#major axis is 2*a
#minor axis is 2*b
#(x-h)^2/b^2 + (y-v)^2/a^2 = 1

both_verticies = (input('do you know both verticies?'))
if both_verticies == 'y':

    value_l = (input('first axis verticie, x and y'))
    xl, yl = value_l.split(',')
    xl, yl = float(xl), float(yl)
    value_r = (input('second axis verticies, x and y'))
    xr, yr = value_r.split(',')
    xr, yr = float(xr), float(yr)
    h = (xl + xr) / 2
    a = (xr - h)

    value_t = (input('upper co verticie, x and y'))
    xt, yt = value_t.split(',')
    xt, yt = float(xt), float(yt)
    value_b = (input('lower co verticies, x and y'))
    xb, yb = value_b.split(',')
    xb, yb = float(xb), float(yb)
    v = (yt + yb) / 2
    b = (yt - v)
    f =  math.sqrt(abs(a**2 - b**2))
    t = np.linspace(0, 2 * pi, 100)
    plt.plot((xl, xr), (v, v), color = 'black')


    plt.text(xl, yl, '({}, {})'.format(xl, yl))
    plt.text(xr, yr, '({}, {})'.format(xr, yr))
    plt.text(xb, yb, '({}, {})'.format(xb, yb))
    plt.text(xt, yt, '({}, {})'.format(xt, yt))
    plt.text(h, v, '({}, {})'.format(h, v))
    plt.text(f, v, '({}, {})'.format(f, v))
    plt.text(-f, v, '({}, {})'.format(-f, v))



    plt.plot((h,h), (yb, yt), color='black')
    plt.plot(h + a * np.cos(t), v + b * np.sin(t))
    plt.grid(color='lightgray', linestyle='--')
    plt.show()



    value_f = (input('what are the foci x and y'))
    if value_f == '':
        pass
    else:
        xf, yf = valuef.split(',')
        xf, yf = float(xf), float(yf)
        c2 = xf ** 2
#    a2 = h**2

#    b2 = a2 - c2

    print('the equation for the elipse is (x - ', h, ')^2/',a**2, ' + (y2- ', v, ')^2/', b**2, ' = 1')
    print('the centerpoint is ', h, ', ', v)
    print('the focus is {:.2f}'.format (f))
else:
    single_verticies = (input('do you know one of the verticies?'))
    if single_verticies == 'y':
        value_l = (input('left end point of the verticie, x and y'))
        xl, yl = value_l.split(',')
        xl, yl = float(xl), float(yl)
        value_r = (input('right end point of the verticie, x and y'))
        xr, yr = value_r.split(',')
        xr, yr = float(xr), float(yr)
        h = (xl + xr) / 2
        a = (xr - h)

        foci = (input('do you know the foci?'))
        if foci == 'y':
            focus_l = (input('left end point of the focus, x and y'))
            flx, fly = focus_l.split(',')
            flx, fly = float(flx), float(fly)
            focus_r = (input('right end point of the focus, x and y'))
            frx, fry = focus_r.split(',')
            frx, fry = float(frx), float(fry)
            f_sqrd = frx**2
            b = f_sqrd - a**2
            print('the equation for the elipse is x2/', a ** 2, ' + y2/', round(abs(b), 0), ' = 1')

    else:
        raise SystemExit

