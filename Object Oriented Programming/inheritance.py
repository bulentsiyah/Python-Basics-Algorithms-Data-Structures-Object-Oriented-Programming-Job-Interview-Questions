# parent
class Animal:
    def __init__(self):
        print("animal is created")
    
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")
    
# child
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent(animal) class
        print("monkey is created")
    
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def fly(self):
        print("fly")        
#
m1 = Monkey()
m1.toString()
m1.walk()
m1.climb()
print("----")
b1 = Bird()
b1.walk()
# b1.climb()
b1.fly()   

# ------------------------------------------------------  

class Website:
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def loginInfo(self):
        print(self.name + " "+ self.surname )

class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
    
    def login(self):
        print(self.name + " "+ self.surname + " "+self.ids)
class Website2(Website):
    "child"
    def __init__ (self, name, surname, email):
        Website.__init__(self,name,surname)
        self.email = email

    def login(self):
        print(self.name + " "+ self.surname + " "+self.email)
          
p1 = Website("name","surname")
p2 = Website1("name","surname", "123")
p3 = Website2("name","surname", "email@")