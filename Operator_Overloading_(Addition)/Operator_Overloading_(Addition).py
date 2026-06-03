class demo:
    def __init__(me,x):
        me.x=x
    def __add__(me,y):
        return(me.x+y.x)
a=demo(20)
b=demo(30)
c=demo(10)
d=(a+b)
print(d)
print(demo(d)+demo(10))
