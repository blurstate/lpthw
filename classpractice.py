import sqlite3
import datetime

class Person(object):
	def __init__(self):
		self.name = ''
		self.gender= ''
		self.dob= None
		
	@property
	def age(self):
		if self.dob is not None:
			return (datetime.datetime.now() - self.dob).days/365
		else:
			return None
	
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
	

	
def main():	
	
	me= Person()
	me.dob=datetime.datetime(1988, 5, 2)
	me.name="Cory"
	me.gender="female"

	print me.can_drink()
	print me.valad_gender()


	if (me.can_drink()==True):
		print"You are over 21 and can drink"
	else:
		print"You are under 21 and cannot drink"

	mcount=0
	fcount=0
	people=[]	


	while (mcount<2 or fcount<2):
		p=Person()
		p.name=raw_input("What is the persons name? ")

				
		while (is_int(p.age)==False):
			dob=raw_input("What is their date of birth? Use Month/Day/Year format with numbers only ")
			dob=dob.split('/')
			p.dob=datetime.datetime(int(dob[2]),int(dob[0]),int(dob[1]))
			
			print p.dob.date()
			
				
		while (p.valad_gender() == False ):
			p.gender=raw_input("Are they Male or Female? ").lower()

			if(p.gender=='male'):
				mcount+=1
			elif(p.gender=='female'):
				fcount+=1





		people.append(p)


	for i in people:
		if i.gender=='female':
			print"Age= {} and DOB= {}" .format(i.age, i.dob.date()) 
			print"{} {} vote" .format(i.name, 'can' if i.can_vote()==True else "can't")


	for i in people:
		if i.gender=='male':
			print"Age= {} and DOB= {}" .format(i.age, i.dob) 

			print"{} {} vote" .format(i.name, 'can' if i.can_vote()==True else "can't")
		
if __name__ == '__main__':
	main()
	