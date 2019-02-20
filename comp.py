a=10
b=2
c=1
def compare():
    if((a>b) and (a>c)):
        print('a is greatest')
    if((b>a) and (b>c)):
        print('b is greatest')
    if((c>a) and (c>b)):
        print('c is greatest')

def compare_exp():
    great=a if (a>b) else b
    greatest= great if(great>c) else c
    print('greatest number is'+str(great))
   
def compare_nested():
    if((a>b) and (a>c)):
        print('a is greatest')
    elif((b>a) and (b>c)):
        print('b is greatest')
    else:
        print('c is greatest')
