class food:
 def __init__(self, fruit, color):
    self.fruit = fruit
    self.__color = color
 def show(self):
    print("fruit is", self.fruit)
    print("color is", self.__color )



    
apple = food("apple", "red")
grapes = food("grapes", "green")
apple.show()
grapes.show()
