import random
from random import randint
import decimal

# Event object
class Event:

	# Params:
	# coords: coordinates of the event
	# id: id of the event
	# tickets: tickets for the event
	# distance: distance to the origin (defaults to -1 on creation)
	def __init__(self, coords, id, tickets, distance=-1):
		self.coords = coords
		self.id = id
		self.tickets = tickets
		self.distance = distance

	def __str__(self):
		return "Event " + str(self.id) + " - " + str(self.cheapestTicket()) + ", Distance: "+  str(self.distance)

	def __lt__(self, other):
		return self.distance > other.distance		

	# Find cheapest ticket for the event
	def cheapestTicket(self):
		if(len(self.tickets) == 0): return
		cheapestTicket = self.tickets[0]
		for t in self.tickets:
			if(t.price < cheapestTicket.price):
				cheapestTicket = t
		return cheapestTicket

# Coordinate object
class Coords:

	# Params:
	# x: x position
	# y: y position
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __str__(self):
		return "(" +str(self.x) +", " + str(self.y)+")"

	# Find the Manhattan distance between two points
	def findDistance(self, other):
		xDistance = abs(self.x - other.x)
		yDistance = abs(self.y - other.y)
		return xDistance + yDistance


# Ticket object
class Ticket:
	
	# Params:
	# price: Price of ticker
	# eventId: Id of the event 
	def __init__(self, price, eventId):
		self.price = price
		self.eventId = eventId

	def __str__(self):
		if(self):
			return "$"+str(self.price)
		else:
			return "None"


# Generate seed data
def generateSeedData(num=10):
	maxTix = 10
	events = []
	coords = []
	for i in range(num):
		 newCoord = newCoords(coords)
		 coords.append(newCoord)
		 tickets = generateTickets(i,randint(0,maxTix))
		 event = Event(newCoord, i, tickets)
		 events.append(event)
	return events


# Generate new coordinates
def newCoords(coords):
	maxCoord = 10
	x = randint(-maxCoord,maxCoord)
	y = randint(-maxCoord, maxCoord)
	c = Coords(x,y)
	# Check if an event already exist at the coordinate
	if(checkCoords(coords, c)):
		return c
	else:
		return newCoords(coords)

# Generate tickets for an event
def generateTickets(eventId, numTix):
	maxPrice = 100
	tickets = []
	for i in range(numTix):
		price = decimal.Decimal(random.randrange(maxPrice*100))/100
		# price = randint(1,maxPrice)
		ticket = Ticket(price, eventId)
		tickets.append(ticket)
	return tickets

# Check if a coordinate already has an event 
def checkCoords(coords, current):
	for i in range(len(coords)):
		if(current == coords[i]):
			return False
	return True

def getUserInput():
	# Size of world
	maxCoord = 10
	coord = input("Please enter coordinates (eg. x,y): ")
	try:
		x = coord.split(",")[0]
		y = coord.split(",")[1]
		x = int(x)
		y = int(x)
	except:
		print("Invalid data type")
		return getUserInput()
	while(x < -maxCoord or x > maxCoord):
		print("Invalid x value. Must be between " + str(-maxCoord) + " and " + str(maxCoord))
		return getUserInput()
	while(y < -maxCoord or y > maxCoord):
		print("Invalid y value. Must be between " + str(-maxCoord) + " and " + str(maxCoord))
		return getUserInput()
	return Coords(x,y)

def findEvents(events):
	# List of closest events
	close = []
	# Number of events to return
	maxEvents = 5
	# Get user input
	origin = getUserInput()
	for e in events:
		# Find and set the distance from the origin to each event
		distance = e.coords.findDistance(origin)
		e.distance = distance
		close.append(e)
	# Sort the list of events and return the closest events
	close = sorted(close)
	print("Closest Events To " + str(origin))
	return close[len(close)-maxEvents:]


for e in findEvents(generateSeedData()):
	print(e)


