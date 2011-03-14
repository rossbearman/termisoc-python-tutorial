import random

class Player:
	level = 1
	health = 10

	area = Area("Test", [Potion("Test Potion"), Poison("Test Poison")])
	inventory = []

	def pickupItem(index):
		area.inventory[index].
		inventory.append(area.inventory[index])
		del area.inventory[index]
	
	def useItem(index)
		inventory[index].consume(self)
		del inventory[index]

class Area:
	inventory = []

	def __init__(self, name, inventory):
		self.name = name
		self.inventory = inventory

	
class Consumable:
	def __init__(self, name):
		self.name = name
		
	def consume(player):
		player.level += 1

class Potion(Consumable):
	def consume(player):
		player.health += 1

class Poison(Consumable):
	def consume(player):
		player.health -= 1

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

	if userInput[0] == 'inventory'
		player.displayInventory()
	elif userInput[0] == 'pickup':
		player.pickupItem(userInput[1])
	elif userInput[0] == 'use':
		player.useItem(userInput[1])
	elif userInput[0] == 'quit':
		quit()
	elif userInput[0] == 'help':
		output.printHelp()
