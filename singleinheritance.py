class Parent:
    def initi(self):

        print("heloo")
class Child(Parent):
 
    def child1(self):
        print("child")

object = Child()
object.child1()
object.initi()


