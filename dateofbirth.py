import datetime



class Person(object):
	def __init__(self):
		self.age = ''
		self.name = ''
		self.gender= ''
		
	def can_drink(self):
		return self.age >=21
	
	def can_vote(self):
		return self.age >=18
	
	def valad_gender(self):
		return self.gender =='male' or self.gender== 'female'
	
	
	@staticmethod
	def createtable():
		
		conn = sqlite3.connect('voters.db')
		print"Opened database succesfully"
		
		conn.execute('''CREATE TABLE PEOPLE (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , NAME TEXT NOT NULL, DOB DATE NOT NULL, GENDER VARCHAR(1) NOT NULL);''')
		
		print"Created table seccesfully"
		
	def save(self):
				
		if self.gender == 'male':
			sex='M'
		else:
			sex='F'
		
		try:
			conn.execute(" INSERT INTO PEOPLE(NAME, DOB, GENDER) VALUES(?,?,?)", (self.name, self.dob, sex))
			
			conn.commit()
			print " Records treated succesfully"
		
		except sqlite3.IntegrityError:
			print "Not a unique data entry"

			
			
			
			
			
			
def is_int(n):
	try:
		int(n)
		return True
	except:
		return False

	
p=Person()

while (is_int(p.age) == False):		
	age=raw_input("What is their date of birth? Use Month/Day/Year format with numbers only ")
	age=age.split('/')
	for i in age:
		i=int(i) 
	
	print age
	p.age=datetime.datetime(int(age[2]),int(age[0]),int(age[1]))
	print p.age
	
	
	
	