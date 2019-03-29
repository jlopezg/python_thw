# create a mappin of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities = {
     'CA': 'san francisco',
	 'MI': 'detroit',
	 'FL': 'jacksonville'
}

# add some more cities
cities['NY'] = 'new york'
cities['OR'] = 'porland'

# print out some cities
print '_' * 10
print "NY states has: ", cities['NY']
print "OR states has: ", cities['OR']

# print some states
print '_' * 10
print "Michigan'S abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '_' * 10
for state, abbrev in states.items():
    print "%s is abbbreviated %s" % (state, abbrev)
	
# print every city in state
print '_' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '_' * 10
for state, abbrev in states.items():
    print "%s states is abbbreviated %s and has city %s" % (
	    state, abbrev, cities[abbrev])
		
print '_' * 10
# safely get an abbreviation by state that might not be there
state = states.get('texas', None)

if not state:
    print "sorry, no texas."
	
# get a city wiht a default value
city = cities.get('TX', 'does not Exist')
print "the city for the state 'TX' is: %s" % city 