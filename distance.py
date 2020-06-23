import math
blue = False

while blue == False:
    dims = input('how many dimensions (2 or 3)?')
    if dims == '2':

        value_1 = (input('first point, x and y'))
        x1, y1 = value_1.split(',')
        x1, y1 = float(x1), float(y1)
        value_2 = (input('second point x and y'))
        x2, y2 = value_2.split(',')
        x2, y2 = float(x2), float(y2)
        distance_x = x2 -x1
        distance_y = y2 - y1
        x_sqrd = math.pow(distance_x, 2)
        y_sqrd = distance_y**2
        final_distance = math.sqrt(x_sqrd + y_sqrd)
        print('the distance is {:.2f}'.format(final_distance))
        response = input('do you want to go again y/n'.lower())
        if response == 'n':
            raise SystemExit

    if dims == '3':

        value_1 = (input('first point, x, y and z'))
        x1, y1, z1 = value_1.split(',')
        x1, y1, z1 = float(x1), float(y1), float(z1)
        value_2 = (input('second point x, y, and Z'))
        x2, y2, z2 = value_2.split(',')
        x2, y2, z2 = float(x2), float(y2), float(z2)
        distance_x = x2 -x1
        distance_y = y2 - y1
        distance_z = z2 - z1
        x_sqrd = math.pow(distance_x, 2)
        y_sqrd = distance_y**2
        z_sqrd = math.pow(distance_z, 2)
        final_distance = math.sqrt(x_sqrd + y_sqrd +z_sqrd)
        print('the distance is {:.2f}'.format(final_distance))
        response = input('do you want to go again y/n'.lower())
        if response == 'n':
            raise SystemExit