class Person(object):
    def __init__(self):
        self.name = ''
        self.age = 0
        self.gender = ''
     #allow you to have default 'Hi' is default   
    def speak(self, phrase='Hi'):
        print phrase
        
    
    
#rec mail
#print how many items went to each floor       
        
class Building(object):
    def __init__(self):
        self.num_floors = 0
        self.num_exits = 0
        self.address = ''
        self.has_basement = False
        self.floors = {
            1: {'num_letters': 0},
            2: {'num_letters': 0},
            3: {'num_letters': 0},   
        }
        
     #for letter in mail:    
    def receive_inventory(self, mail):
        for letter in mail:
            self.floors[letter.floor]['num_letters'] += 1
            
        for 
            
         
            
        
        
        
        
        
        
        
class Engine(object):
    def __init__(self):
        self.num_cylinders = 0
        self.horsepower = 0
        self.fuel_type = ''

        
class Vehicle(object):
    def __init__(self):
        self.owner = Person()
        self.color = ''
        self.year = 0
        self.num_doors = ''
        self.engine = Engine()
        self.heading = 'North'
        self.newDirection = ''
        
    def turn(self, newDirection):
       #turn left, heading west
       if self.heading == 'North' and newDirection == 'left':
           self.heading = 'West'
       else:
           self.heading == 'North'and newDirection == 'right'
           self.heading = 'East'
           print "You are now heading {}".format(self.heading)
       if self.heading == 'West' and newDirection == 'left':
           self.heading = 'South'
       else:
           self.heading == 'West'and newDirection == 'right'
           self.heading = 'North'
           print "You are now heading {}".format(self.heading)
       # if self.heading == 'South' and newDirection == 'left':
#            self.heading = 'East'
#            print "You are now heading {}".format(self.heading)
#        if self.heading == 'East' and newDirection == 'left':
#                self.heading = 'North'
#                print "You are now heading {}".format(self.heading)
#
        
        
    def report_horsepower(self):
        print "{}'s vehicle has {} horsepower".format(self.owner.name, self.engine.horsepower)
        print self.engine.horsepower
        
p1 = Person()
p1.name = 'Jeremy'

p2 = Person()
p2.name = 'Adam'


        
v1 = Vehicle()
v1.owner = p1
#give vehicle some hp
v1.engine.horsepower = 200
print 'v1 hp', v1.engine.horsepower

v2 = Vehicle()
v2.owner = p2
v2.engine = v2.engine
print 'v2 hp', v2.engine.horsepower


v1.turn('left')

# p = Person()
# p.speak('yo')
# p.speak('hi')
# p.speak()







# write a program that will count how many times each word in a paragraph is used
# Zipf's law

words = """

"""
words = words.split('')
wordC
for 

#Step1: 



#Step2:  
#Step3: 

