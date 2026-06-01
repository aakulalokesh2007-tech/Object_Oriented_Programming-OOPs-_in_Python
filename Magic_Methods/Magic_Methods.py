class com:
    def __init__(me,a):
        me.x=a
    def __eq__(me,ot):
        return me.x == ot.x
    def __lt__(me,ot):
        return me.x < ot.x
    def __le__(me,ot):
        return me.x <= ot.x
    def __gt__(me,ot):
        return me.x > ot.x
    def __ge__(me,ot):
        return me.x >= ot.x
a=com(20)
b=com(2)
c=(a<=b)
print(c)
