#Tell me if I can smoke or drink

#1 ask the age
#age = '15'
age = raw_input('what is your age? ')
age = int(age)

#2 define legal smoking age
smoking_age = 18

#3 define legal drinking age
drinking_age = 21

#4 decide if age is higher or lower than legal ages
if age >= smoking_age:
	#5 return the answer
	print "you can smoke"
else:
	print "you can't smoke"

if age >= drinking_age:
    print "you can drink"
else:
    print "you can't drink"