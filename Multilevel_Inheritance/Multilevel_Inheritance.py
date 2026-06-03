class a:
    def ass(me):
        print("in a")
class c(a):
    def bi(me):
        print("in c")
class b(c):
    def re(me):
        print("in b")


A=b()
A.ass()
A.bi()
A.re()
