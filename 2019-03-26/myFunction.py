def bmi(h,w):
    x=w/(h/100)**2
    return f'{x:.2f}'

def fc(*args,**kwargs):
    return args,kwargs
m,n=fc(3,5,7,9,x=8,y=13)