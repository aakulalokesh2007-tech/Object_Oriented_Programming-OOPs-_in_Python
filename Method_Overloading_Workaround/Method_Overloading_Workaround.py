class ins:
    def add(me,tan,*args):
        re=0
        if tan == 'str':
            re=''
        if tan=='int':
            re=0
        for b in args:
            re+=b
        print(re)
a=ins()
a.add('int',1,2,3,4,5)
