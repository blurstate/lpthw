parent = {'name': '', 'spouse': '', 'kids': []}











print "What is your name?"
parent['name'] = raw_input()

print "What is your spouse's name?"
parent['spouse'] = raw_input()

print "How many kids do you have?"
number_of_kids = int(raw_input())
	
print "What are their names?"

for i in range(0, number_of_kids):
	kid = {}
	kid['name'] = raw_input('Child name {}? > '.format(i + 1))
	kid['age'] = int(raw_input('What is their age{}? > '.format(i + 1)))
	parent['kids'].append(kid)
	
print "{} and {} have {} children".format(parent['name'], parent['spouse'], number_of_kids)

print "Their kids are" 

for k in parent['kids']:
	print "{name} age {age}".format(name=k['name'], age=k['age'])
	
	