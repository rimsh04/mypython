print('enter Hours')
hours=float(input())
print('enter rate')
rate=float(input())
pay=rate*hours
if(hours>40):
    pay=pay*1.5
    print('pay: '+str(pay))
else:
    print('pay: '+str(pay))
