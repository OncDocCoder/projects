door_count = 500

locker_value = [] #is the door open or closed.  -1 is closed, 1 is open
for item in range(0, (door_count + 1)):
    locker_value.append(-1)

locker_num = [] #the number on the locker
for namer in range(1, (door_count+ 1)):
    locker_num.append(namer)

#print("lockernum is ",  locker_num) #the number on the locker

#run through 'cycler' number cycles


for x in range(1, door_count + 1):
    for y in range(1, (len(locker_num) + 1)):
        if y % x ==0:
            locker_value[y-1] = -1 * locker_value[y-1]

        if y % x != 0:
            locker_value[y - 1] = 1 * locker_value[y - 1]

 #           #print(x, y, "true")
#print(locker_value)
door_open = []
tick = 0
for z in locker_value:
    if z == 1:
        door_open.append(tick+1)
    tick += 1
print("for ", door_count, "number of doors, open lockers are ", door_open)