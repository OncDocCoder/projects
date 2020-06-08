# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('Jack', '33')
#
#
# sentence = 'My name is {name} and I am {age} years old.'.format(name= 'Mitch', age= '56')

# person = {'name' : 'John', 'age' : 23}
# l = ['Jenn', 35]

#sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'

#sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])

#sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])

# tag = 'Hi'
# text = 'This is a headline.'
#
# sentence  = '<{0}>{1}<{0}'.format(tag, text)

#sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)

#sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(p1)

# print(sentence)

# for i in range(1, 11):
#     sentence = 'The value is {}'.format(i)
#     print(sentence)

# pi =  3.14159265
#
# sentence = 'Pi is equal to {:.2f}'.format(pi) #uses 2 decimals

# sentence = '1 MB is equal to {:,} bytes'.format(1000**2) #1,000,000 bytes
# sentence2 = '1 MB is equal to {:,.2f} bytes'.format(1000**2) #1,000,000 bytes
# print(sentence, sentence2)

import datetime
my_date = datetime.datetime(2020, 5, 18, 2, 59, 45)
sentence  = '{:%B %d, %Y}'.format(my_date)
sentence2 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence2)