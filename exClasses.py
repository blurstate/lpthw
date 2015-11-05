# Make a person class


class Person(object):
	def __init__(self):
		self.age = 0
		self.name = ''
		self.has_kids = False
		
	def speak(self, phrase='Hi'):
		print phrase

# receive mail
# print how many items went to each floor

class Floor(object):
    def __init__(self):
        self.number = 0
        self.num_letters = 0

class Building(object):
	def __init__(self, num_floors=2):
		self.num_exits = 0
		self.address = ''
		self.has_basement = False
        self.floors = {}

class Engine(object):
	def __init__(self):
		self.num_cylinders = 0
		self.horsepower = 0
		self.fuel_type = ''

	
class Vehicle(object):
    DIRECTIONS = {
        0: 'North',
        90: 'East',
        180: 'South',
        270: 'West',
    }
    
    def __init__(self):
        self.owner = Person()
        self.color = ''
        self.year = 0
        self.num_doors = 0
        self.engine = Engine()
        self.heading = 0
    
    @property    
    def direction(self):
        return Vehicle.DIRECTIONS[self.heading]
        
    def turn(self, newDirection):
        oldDirection = self.direction
        
        if newDirection == 'left':
            self.heading = self.heading - 90
            
            if self.heading == -90:
                self.heading = 270
        else:
            self.heading = self.heading + 90
            
            if self.heading == 360:
                self.heading = 0
        
        print "You were heading {}.  You turned {}.  You are now heading {}".format(oldDirection, newDirection, self.direction)
        
        
    def report_horsepower(self):
        print "{}'s vehicle has {} horsepower".format(self.owner.name, self.engine.horsepower)

print "================================"
print ""

p1 = Person()
p1.name = 'Justin'

p2 = Person()
p2.name = 'Derrick'

v1 = Vehicle()
v1.owner = p1
v1.engine.horsepower = 100
v1.report_horsepower()

v2 = Vehicle()
v2.owner = p2
v2.engine.horsepower = 200
v2.report_horsepower()

e = v1.engine
e.horsepower = 300

#v1.report_horsepower()
#v2.report_horsepower()

v1.turn('right')
v1.turn('right')
v1.turn('right')
v1.turn('right')

v1.turn('right')
v1.turn('right')
v1.turn('right')
v1.turn('right')

v1.turn('left')
v1.turn('left')
v1.turn('left')
v1.turn('left')

v1.turn('left')
v1.turn('left')
v1.turn('left')
v1.turn('left')

print ""

# write a program that will count how many times each word in a paragraph is used
#  Zipf's law



