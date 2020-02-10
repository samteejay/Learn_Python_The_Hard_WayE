class Parent(object):

	def override(self):
		print "PARENT overide()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD overide()"
		
dad = Parent()
son = Child()

dad.override()
son.override()