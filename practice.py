#Getting plenty of practice is a good thing for confidence in programming
#Documentation is good not only for the one doing the work, but also the one looking at the work





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Purpose 1-3: Tell me if I'm old enough to drink, smoke, or date. 
# Purpose 4: Ask me if I'm married or not.
# Purpose 5-7: Tell me how many more years until I can (drink, smoke, date) or how many years I've been able to.
# Purpose 8: Tell me if I can get married or not. (cant get married if you already are)
# Purpose 9-11: Tell me if Im allowed to (drink, smoke, date), if not allowed, how long until I'm able to.
# Purpose 12: Tell me if I can smoke OR drink
# Purpose 13: Tell me if I can smoke AND drink
# Purpose 14: Tell me if I have the same name as you.
# Purpose 15: Tell me if we are the same age.
# --------------
# Purpose 16: Keep asking me my age until I tell you I'm 29 and tell me how many times it took.
# Purpose 17: Ask me my age 5 times.
# Purpose 18: Ask me my age 5 times or until I tell you I'm 29 and tell me how many times it took.
# Purpose 19: Print out every number from 1 to 100 and tell me how many there are.
# Purpose 20: Divide every number from 1 to 100 by 3 and print out the remainder of that division operation. 
# Purpose 20.1: Tell me how many have a remainder of 2.
# Purpose 21: Tell me what foods I said I liked.
# Purpose 22: Tell me which foods that you and I both like.
# --------------
# Purpose 23: Tell me which of my kids can drink.
# Purpose 24: Tell me which of my pets are dogs.
# Purpose 25: Tell me the names of my kids who have dogs that are labs.
# --------------
# Purpose 26: Make a person class and redo the exercises using methods of the class 
# class Person(object):
#	def __init__(self):
#		self.age = 0
#
#	def can_drink(self):
#		return self.age>=21
#
#	p = Person()
#	p.age = 59
#	p.can_drink()
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# I'll set the drinking age to 21.
drinking_age = 21
# I'll set the smoking age to 18
smoking_age = 18
# I'll set the dating age to 16
dating_age = 16

# going to run a while loop to make sure that you answer the question with a real number.
# While true says that whatever we say next is true (this is a loop)
while True:
# Telling the program to ask for your age
	try:
		age = int(raw_input("How old are you? > "))
		# break says that if the thing you just did worked, then break the loop
		break
# Telling the program that if the answer to the previous question was false to give this error message.		
	except ValueError:
		print "You are a magical creature with no age. Try again."
married = 
# now for the if statements to tell you if you are old enough to drink or not
# if your age is greater than or equal to the drinking age then you are old enough to drink
if age >= drinking_age:
	print "You are old enough to drink."
# otherwise, you are not old enough to drink	
else:
	print "You are not old enough to drink."

# again with smoking
if age >= smoking_age:
	print "You are old enough to smoke."
else:
	print "You are not old enough to smoke."

# yet again with dating
if age >= dating_age:
	print "You are old enough to date."
else:
	print "You are not old enough to date."

