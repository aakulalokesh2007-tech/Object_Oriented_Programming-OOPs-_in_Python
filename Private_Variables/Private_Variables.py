class var:
    def go(self):
       self.na='lok'
       self.__num=110112
    def no(self):
        print("name=",self.na)
        print("number",self.__num)
p=var()
p.go()
p.no()
print(p._var__num)
        
