def firstex():
	# ask user info about themselves, age, married, name
	myname="cory"
	myage=27
	name= raw_input("Hello friend! What is your name? ")
	age= input("How old are you? ")

	married = raw_input("Are you married? Y/N ? ")
	#print type(married)
	loop = False  #using bool while loop to make sure proper syntax is used 
	while (loop == False):

		if married in ["Y","y","N","n"]:
			if married in[ "Y","y"]:
				married = True
			else: 
				married = False
			loop = True
		else: married= raw_input("Sorry you must answer with a Y for yes or N for no: ")

	#tells you if your old enough to drink		
	if( age>=21 ):
		print"You are old enough to drink."
	else: print"You are not old enough to drink."

	#tells you if your old enough to smoke
	if( age>=18 ):
		print"You are old enough to smoke."
	else: print"You are not old enough to smoke."

	#tells you if your old enough to date arbitrary(16) 
	if( age>=16):
		print"You are old enough to date."
	else: print"You are not old enough to date."

	#tells you if your married or not
	#print married
	if( married==True ):
		print"You are married"
	else:
		print"You are not married"

	#tells you how many years you have to wait to drink or how many you have been able to 
	#print type(age)

	if( age>=21 ):
		if (age>21):
			print"You have been able to drink for the last {} years".format(age-21)
		else: print"This is your first year being able to drink"
	if (age<21):
		print"You have to wait {} more years till you can drink".format(21-age)


	if( age>=18 ):
		if (age>18):
			print"You have been able to smoke for the last {} years".format(age-18)
		else: print"This is your first year being able to somke"
	if (age<18):
		print"You have to wait {} more years till you can smoke".format(18-age)


	if( age>=16 ):
		if (age>16):
			print"You have been able to date for the last {} years".format(age-16)
		else: print"This is your first year being able to date"
	if (age<16):
		print"You have to wait {} more years till you can go on a date".format(16-age)


	if (21>age>=18):
		print"You can smoke but you cannot drink."

	if (age>=21):
		print"You can smoke and drink."

	if name.lower() in myname:
		print"We have the same name!"
	else:
		print"We dont have the same name."

	if (age==myage):
		print"We are the same age!"
	else:
		print"We are not the same age."


#firstex()
##################################################################################
# second set of exampls showing while loops and lists
def secondex():
	
	#keep asking user for age until they tell you they are 29
	age=0
	count=0
	while (age!=29):
		age = input("What is your age? ")
		count+=1
		
		if (age==29):
			print"I took you {} times to say you were 29" .format(count)
	#ask age 5 times		
#	for i in range (5):
#		age = input("what is your age? ")
#	#ask age 5 times or untill you say your are 29
#	for i in range (5) :
#		age= input("OK, now What is your age? ")
#		if (age==29):
#			print "you are 29"
#			break
#	print "you are not 29"
	
	#print out evey even number from 1 to 100 and count how many there are
	count= 0
	for i in range (1,100+1):
		if i%2==0:
			print i
			count+=1
	print"there are {} even numbers" .format(count)
	
	
	#divide every number from 1 to 100 by 3 and print out the remainder of that division operation. tell me how many have a remainder of 2 
	count=0
	for i in range(1,101):
		print i%3
		if (i%3==2):
			count+=1
			
	print "there were {} remanders of 2 when divided by 3" .format(count)
	
	# creat a for loop that will ask for your favorite foods. have it propigate a list 
	
	faveFoods=[]
	for i in range (10):
		fave=raw_input("What are your 10 favorite foods? ")
		faveFoods.insert(i,fave)
		
	#print out what the favorit foods are
	print"Your favorite foods are:"
	print"========================"
	for i in faveFoods:
		print "||", i
	myFaveFoods= ["pizza", "steak", "chips", "beer", "pasta", "corn", "fish", "milk", "cheese", "cake"]
	
	#compare every food item in faveFoods to myFaveFoods and mod the string to accoutn for capitalisation, have an if statment print out the foods that matched
	for i in faveFoods:
		for idx in myFaveFoods:
			if (i.lower()==idx.lower()):
				print"we both like {}" .format(i.lower())
	
#########################################################################	
#secondex()
#########################################################################

#dictionary practice
def thirdex():
	
	kidsage= {'Jake': 4, "Aaron": 18, "Jakson": 23, "Kate": 14, "Susan" : 22}
	
	for name, age in kidsage.iteritems():
		if (age>=21):
			print"{} is {} and can drink.".format(name,age)
		else:
			print"{} is {} and can not drink alcohol" .format(name,age)
	#build a class to set into another class for children and pets
	class Pet:
			petType=' '
			breed=' '
			
	class Person(object):
		name=' '
		age= 0
		pet= None
		kid= None
	#Person.pet=Pet()
	#Preson.kid=Person()
	
	numKid=raw_input("How manny kids do you have? ")
	numPets=raw_input("How manny pets do you have? ")
	
	for i in range(0,numKid):
		kid=Person()
		kid.name=raw_input("What is your kids name? ")
		kid.age=raw_input("and {} is how old? ") .format(kid.name)
		numKpets=raw_input("How manny pets do they have? ")
		if numKpets>0:
			for i in range(0,numKpets):
				pet=Pet()
				pet.petType=raw_input("What kind of pet is it? ")
				pet.breed=raw_input("What breed is it? "
									
	
			
thirdex()
			



		




