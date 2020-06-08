# names = ['Jeff', 'Gary', 'Jill', 'Samantha']
#
# for name in names:
#     #print('Hello there, ' + name)
#     print(' '.join(['Hello there, ', name]))
#
# #Gary bought 12 apples today
# who = 'Gary'
# how_many = 12
#
# sentence = who + " bought " , how_many , " apples today?"
# print(sentence)
# print(who, ' bought ', how_many,  'apples today?')
# print('{} bought {} apples today beep'.format(who, how_many))

a= 0

first_group = [32, 2, -5, 24]
second_group = [32, 2, -5]

for x in first_group:
    a += x

b = 0
for y in second_group:
    b += y

print(abs(b - a))

# first_group.sort()
# second_group.sort()
q = []
if len(first_group) > len(second_group):
    for item in first_group:
        if item not in second_group:
            q.append(item)
else:
    for item in second_group:
        if item not in first_group:
            q.append(item)

print(q)

first_group.sort()
second_group.sort()
v = len(first_group)
g = len(second_group)

if v > g:
    p = 0
    while p < v:
        if first_group[p] != second_group[p]:
            print(first_group[p])
            break
        else:
            p += 1
    if p == v:
        print(first_group[-1])

else:
    p = 0
    while p < g:
        if second_group[p] != first_group[p]:
            print(second_group[p])
            break
        else:
            p += 1
    if p == v:
        print(second_group[-1])








