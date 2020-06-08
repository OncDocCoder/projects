# a is acceleration
# t is time
# v1 is original speed
# d is distance

def distance(v1, t, a):
    d = round(v1 * t + 0.5 * a * t ** 2, 2)
    return d

def acceleration(v1, t, a):
    a = round(d / (v1 * t + 0.5  * t ** 2), 2)
    return a

def times(v1, a, d):
    t = round((d / (0.5  * a))**0.5, 2)
    return t




process = input('solve for distance(d), time(t), original velocity(v) or time(t)')
if process == 'd':
    v1 = float(input('enter initial velocity(v1)'))
    t = float(input('time(t)'))
    a = float(input('acceleration(a)'))
    d = distance(v1, t, a)
    print('the distance is ', d)

if process == 'a':
    v1 = float(input('enter initial velocity(v1)'))
    t = float(input('time(t)'))
    d = float(input('distance(d)'))
    a = acceleration(v1, t, d)
    print('the acceleration is ', a)

if process == 't':
    v1 = float(input('initial velocity(v1) must be zero'))
    a = float(input('acceleration(a)'))
    d = float(input('distance(d)'))
    t = times(v1, a, d)
    print('the time is ', t)




#d = v1 * t + 0.5 * a * t**2
#vf**2 = vi**2 + 2*a*d