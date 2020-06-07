#to calculate the mortgage

# r = interest rate
# P = amount borrowed
# N = number of monthly payments
# c = monthly payment

a = float(input('interest rate'))
b = int(input('amount borrowed'))
d = int(input('length of mortgage'))

r = a/12
p = b
n = d
c = (r * p * ((1 + r)**n)) / (((1 + r)**n) - 1)


print('the payment is ${:,.2f}'.format(c))

a = float(input('interest rate'))
b = float(input('payment'))
d = int(input('length of mortgage'))

r = a/12
n = d


p = (((1 + r)**n) - 1) * c  / (((1 + r)**n)* r)
print('the amount you can borrow is ${:,.2f}'.format(p))