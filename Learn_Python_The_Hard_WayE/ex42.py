## Animal is-a object (yes, sort of confusing) look at the credit
class Animal(object):
	pass
	
## Dog is-a Animal that has-a __init__ that takes self and name parameters
class Dog(Animal):

	def__init__(self, name):
		## From self get the name attribute and set it to name
		self.name = name
		
## Cat is-a Animal that has-a __init__ that takes self and name parameters
class Cat(Animal):

	def__init__(self, name):
		## From self get the name attribute and set it to name
		self.name = name
		
## Person is-a object that has-a __init__ that takes self and name parameters
class Person(object):

	def__init__(self, name):
		## From self get the name attribute and set it to name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person that has-a __init__ that takes self, name  and salery parameters
class Employee(Person):

	def__init__(self, name, salary):
		## hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## From self get the salary attribute and set it to salary
		self.salary = salary
		
## Fish is-a object  
class Fish(object):
	pass
	
## Salmon is-a Fish 
class Salmon(Fish):
	pass

## Halibut is-a Fish  
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## From frank get the pet attribute and set it to rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of class Salmon
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()

	
