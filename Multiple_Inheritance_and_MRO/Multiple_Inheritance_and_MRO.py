class demo:
    def dis(me):
        print("in a")
class c(demo):
    def dis(me):
        print("in c")
        super().dis()
class d(demo):
    def dis(me):
        print("in d")
        super().dis()
        
class newdemo(c,d):
    def dis(me):
        print("in b")
        super().dis()
a=newdemo()
a.dis()
