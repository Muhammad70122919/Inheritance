class Parent:
    def func1(self):
        print(" in parent class.")
 
class Child1(Parent):
    def func2(self):
        print("in child 1.")

class Child2(Parent):
    def func4(self):
        print("in child 2.")

object2 = Child2()
object1 = Child1()
object1.func1()
object1.func2()
object2.func1()
object2.func4()
