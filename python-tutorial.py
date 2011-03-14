import random

class Player:
	level = 1

class Output:
	@staticmethod
	def printHelp(self):
		print "Known commands are:\n"
		print "quit\n"
		print "help\n"

player = Player()

while(True):
	userInput = raw_input("Please enter a command:")
	
	if userInput == 'quit':
		quit()
	if userInput == 'help':
		Output.printHelp()
