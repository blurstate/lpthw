class Person(object):
	def __init__(self):
		self.name=''
		self.age= 0
		self.gender= ''
		self.kids=''
	
	
	def speak(self, phrase='Hi'):
		print phrase
		
	
		
		
		
class Building(object):
	def __init__(self, num_floors=2):
		self.num_floors= num_floors
		self.num_exits=0
		self.address=''
		self.has_basement = False 
		self.floors = {
			1: {'num_mail': 0},
			2: {'num_mail': 0},
			3: {'num_mail': 0},
		}
		for i in range(1, num_floors+1):
			self.floors[i]= {'num_mail': 0}
		
		
		
	def receive_mail(self, mail):
		
		for letter in mail:
			self.floors[letter.floor]['num_mail'] += 1
		
		
		
		
		
class Letter(object):
	def __init__(self):
		self.to=''
		self.sentfrom=''
		self.floor=0

		
	
		
		

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
		self.num_doors= 0
		self.engine = Engine()
		self.heading = 'North'
		
	def report_horsepower(self):
		print"{}'s vehilcle has {} horsepower" .format(self.owner.name, self.engine.horsepower)
		
	def turn(self, turning=None):
		directions=['North', 'West', 'South', 'East']
		
		if turning.lower()=='left':
			d=1
		
		elif turning.lower()=='right':
			d=(-1)
		
		for i, j in enumerate(directions):
			
			print j
			if j == self.heading:
				i=i+d
				
				if i==4:
					i=0
				elif i==(-1):
					i=3
				
				#print j
				#print "|",i,directions[i],"|"
				self.heading= directions[i]
				break

print "=================================================================="
print " "



l1=Letter()
l1.floor=1

l2=Letter()
l2.floor=1

l3=Letter()
l3.floor=2

l4=Letter()
l4.floor=3

l5=Letter()
l5.floor=1

l6=Letter()
l6.floor=2

l7=Letter()
l7.floor=3

l8=Letter()
l8.floor=4

mail=[l1,l2,l3,l4,l5,l6,l7,l8]


b=Building(5)



print b.floors
b.receive_mail(mail)
print b.floors
