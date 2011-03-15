import random

class Area:
	inventory = []

	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory

	def displayInventory(self):
		i = 0
		print "You look around, and see:"
		for item in self.inventory:
			print str(i) + ": " + item.name
			i += 1

class Consumable:
	def __init__(self, name):
		self.name = name
		
	def consume(self, player):
		player.level += 1

class Potion(Consumable):
	def consume(self, player):
		player.health += 1

class Poison(Consumable):
	def consume(self, player):
		player.health -= 1

class Player:
	level = 1
	health = 10

	area = Area("Test", [Potion("Test Potion"), Poison("Test Poison")])
	inventory = []

	def pickupItem(self, index):
		self.area.inventory[index]
		self.inventory.append(self.area.inventory[index])
		del self.area.inventory[index]
	
	def useItem(self, index):
		self.inventory[index].consume(self)
		del self.inventory[index]
	
	def displayInventory(self):
		i = 0
		print "Your inventory:"
		for item in self.inventory:
			print str(i) + ": " + item.name
			i += 1
	
	def displayStatus(self):
		print "Level: " + str(self.level)
		print "Health: " + str(self.health)

class Output:
	def printHelp(self):
		print "Known commands are:"
		print "inventory"
		print "pickup <item>"
		print "use <item>"
		print "quit"
		print "help"

player = Player()
output = Output()

while(True):
	userInput = raw_input("Please enter a command:")
	userInput = userInput.split()

	if userInput[0] == 'inventory' or userInput[0] == 'i':
		player.displayInventory()
	elif userInput[0] == 'status' or userInput[0] == 's':
		player.displayStatus()
	elif userInput[0] == 'pickup' or userInput[0] == 'p':
		try:
			player.pickupItem(int(userInput[1]))
		except:
			print "That item doesn't exist!"
	elif userInput[0] == 'use' or userInput[0] == 'u':
		try:
			player.useItem(int(userInput[1]))
		except:	
			print "That item doesn't exist!"
	elif userInput[0] == 'look' or userInput[0] == 'l':
		player.area.displayInventory()
	elif userInput[0] == 'quit' or userInput[0] == 'q':
		quit()
	elif userInput[0] == 'help' or userInput[0] == 'h':
		output.printHelp()
	else:
		print "Uh oh! I can't find the command '" + userInput[0] + "', please enter another command."
