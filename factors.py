
import math
from functools import reduce

# def factors(n):
#     return set(reduce(list.__add__,
#                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#
# a = factors(16)
# b = sorted(a)
# print(b)


def figure_factors(square, base, offset):
    a = int(square)
    b = int(base)/a
    c = int(offset)/a
    d = -1 * c
    e = b/2
    f = e**2
    g = f + c
    h = f + d
    i = h**0.5
    j = i + e
    k = (i * -1) + e
    l = j * -1
    m = k * -1
    return(j, k, l, m)



square = input('enter squared number')
base = input('base')
offset = input('offset')
print(square + 'x**2'+ ' + ' + base + 'x' + '+ ' + offset)
j, k, l, m = figure_factors(square, base, offset)
if j < 0 and k < 0:
    print('the factors are x', j, 'and x', k)
elif j > 0 and k > 0:
    print('the factors are x +', j, 'and x +', k)
elif j < 0 and k > 0:
    print('the factors are x', j, 'and x +', k)
elif j > 0 and k < 0:
    print('the factors are x +', j, 'and x +', k)


print("the solutions are ", l, 'and ', m)







