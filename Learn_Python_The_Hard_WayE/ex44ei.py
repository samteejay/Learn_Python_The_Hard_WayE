from other import *

class Child(object):

	def implicit(self):
		implicit()
	
	def override(self):
		print "CHILD override"	
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		altered()
		print "CHILD, AFTER PARENT altered()"
		
son = Child()

son.implicit()
son.override()
son.altered()