from other2 import *

class Child(object):

	def implicit(self):
		san.implicit()
	
	def override(self):
		print "CHILD override"	
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		san.altered()
		print "CHILD, AFTER PARENT altered()"
		
son = Child()

son.implicit()
son.override()
son.altered()