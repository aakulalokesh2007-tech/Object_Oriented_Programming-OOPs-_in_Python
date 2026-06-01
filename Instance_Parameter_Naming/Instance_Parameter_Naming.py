class Person:
  def __init__(yes, name, age):
    yes.name = name
    yes.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name+'my age is ',abc.age)

p1 = Person("John", 36)
p1.myfunc()
