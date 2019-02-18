try:
    print('Enter hours')
    hours=float(input())
    print('Enter rate')
    rate=float(input())
    pay=hours*rate
    print('Pay: '+str(pay))
except:
    print('enter numeric values')

