# create a mapping of state to abbreviation without hashmap
#states = {
#	'Oregon': 'OR',
#	'Florida': 'FL',
#	'California': 'CA',
#	'New York': 'NY',
#	'Michigan': 'MI'
#}

# create a mapping of state to abbreviation with hashmap
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')


# create a basic set of states and some cities in them without hashmap
#cities = {
#	'CA': 'San Francisco',
#	'MI': 'Detroit',
#	'FL': 'Jacksonville'
#}

# create a basic set of states and some cities in them with hashmap
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')


# add some more cities without hashmap
#cities['NY'] = 'New York'
#cities['OR'] = 'Portland'

# add some more cities with hashmap
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')


# print out some cities
print '_' * 10
print "NY State has: %s", hashmap.get(cities, 'NY')
print "OR State has: %s", hashmap.get(cities, 'OR')

# print some states
print '_' * 10
print "Michigan's abbreviation is: %s", hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s", hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: %s", (cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s", (cities, hashmap.get(states, 'Florida'))

# print every state abbreviation
print '_' * 10
hasmap.list(states)
#for state, abbrev in states.items():
#	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
hashmap.list(cities)
#for abbrev, city in cities.items():
#	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '_' * 10
hashmap.list(cities, states)
#for state, abbrev in states.items():
#	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
# safely get an abbreviation by state that might not be there
state = hashmap.get('Texas')

if not state:
	print "Sorry, no Texas."


# default values using //= with the nil result
# get a city with a default value
city = hashmap.get(citgies, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

