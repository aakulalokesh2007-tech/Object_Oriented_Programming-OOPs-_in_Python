class vol:
    def __init__(me,le,br):
        me.le=le
        me.br=br
    def area(me):
        return me.le*me.br
print(vol(2,3).area())
