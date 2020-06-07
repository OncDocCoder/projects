#to calculate the mortgage

# r = interest rate
# P = amount borrowed
# N = number of monthly payments
# c = monthly payment
z = False
while z == False:

    q = input('do you want to calculate the amount you can borrow (b) or your payment (p)?').lower()
    if q == 'p':

        a = float(input('interest rate'))
        b = int(input('amount borrowed'))
        d = int(input('length of mortgage'))

        r = a/12
        p = b
        n = d
        c = (r * p * ((1 + r)**n)) / (((1 + r)**n) - 1)


        print('the payment is ${:,.2f}'.format(c))
        z == True
        quit()
    if q == 'b':

        a = float(input('interest rate'))
        b = float(input('payment'))
        d = int(input('length of mortgage'))

        r = a/12
        n = d


        x = (((1 + r)**n) - 1) * b  / (((1 + r)**n)* r)
        print('the amount you can borrow is ${:,.2f}'.format(x))
        z == True
        quit()
    else:
        print('enter b or p')
        z == False
