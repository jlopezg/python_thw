#-*- coding: utf-8 -*-

#create a mapping of state to abbrevition 
states = {
	'Oregon' : 'OR',
	'Florida':  'FL',
	'California':'CA',
	'new york': 'NY',
	'Michigan': 'Mi'

}

#create basic set of states and some cities in them

cities = {
	'CA': 'San Francisco',
	'Mi': 'Detroit',
	'FL': 'jacsonville'

}

#add some more cities
cities ['NY'] = 'New York'
cities ['OR'] = 'Portland'

#print out some  cities
print '_' *10
print "Ny states has :", cities['NY']
print "OR State has:",cities['OR']

#print some state

print '_'*10
print "Michigan's abbreviatrion is ", states ['Michigan']
print "florida's abbreviation is", states['Florida']

#do  it by using the states then cities dict

print '_'*10
print "Michigan has:", cities[states['Michigan']]
print "Florida has:",cities[states['Florida']]

#print every state abbeviation

print '_'*10
for state,abbrev in states.items():
	print "%s is abbreviated %s" % (state,abbrev)

# print every city in states

print '_ '*10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

#now do both at same time

print '_'*10
for state,abbrev in states.items():
	print "%s states is abbreviated %s and city %s"%(
		state,abbrev, cities[abbrev])

print '_'*10
#safely get a abrevation by state taht might be there
state = states.get('texas',None)


if not state:
	print "Sorry, no texas."

	#get a city with a defaul value
	city = cities.get('tx,' 'Does Not exist')
	print "The city for the state 'tx' is %s" % city


