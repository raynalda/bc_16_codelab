class Person(object):
      # Constructor
    def __init__(self, name):
    	# the name is attached to the object (Encapsulation) , i can have different objects with different values
        self._name = name 
    #Defining the accessor methods 
    # getter method
    def getName(self):
        return self._name

    #setter method
    def setName(self,name):
         self._name=name

    # To check if this person is a musician
    def isMusician(self):
        return False
 
 
#class Musician (subClass) inheriting from class Person (baseClass)
class Musician(Person):
 
    # Here we return true
    def isMusician(self):
    	return True
      

    def sing(self):
    	print("Musician Sings")

    def produce(self):
        print("Musician can not make beats")

class Producer(Person):
 
    def isProducer(self):
        return super().isMusician() # access the parent method 

    def produce(self):
    	print("Producer Makes some beats") 
    def sing(self):
    	print("Producer Cannot sing") 

        
#program execution starts here
studioMember1 = Person("Raynalda")  # An Object of a Person
print("Is ",studioMember1.getName(),"A Musician ?", studioMember1.isMusician())
 
studioMember2 = Musician("Nameless") # An Object of a musician
print("Is ",studioMember2.getName(),"A Musician ? ", studioMember2.isMusician())

studioMember3=Producer("RK") # An Object of a producer
print("Is ",studioMember3.getName(),"A Musician? ", studioMember3.isProducer())


#using the setter method
studioMember2.setName("Ali Kiba")
print("Is ",studioMember2.getName(),"A Musician ? ", studioMember2.isMusician())

musician1=Musician("Diamond")
Producer1=Producer("Master J")

def in_the_stage(musician):
	musician.sing()

def in_the_studio(producer):
	producer.produce()

#this shows polymorphism , the object of the class don't care what the name of the class is
in_the_stage(musician1)
in_the_stage(Producer1)
in_the_studio(musician1)
in_the_studio(Producer1)