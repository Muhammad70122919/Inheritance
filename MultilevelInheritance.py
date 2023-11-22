class base:
    def base(self):
        print("base class")

	
class derived1(base):
    def derived(self):
        print("derived one class")
	
class derived2(derived1):
      def derive1(self):
          print("drive class")

object=derived2()
object.base()
object.derived()
