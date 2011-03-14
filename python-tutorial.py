import random

class Player:
	level = 1

class Output:
	def printHelp(self):
		print "Known commands are:"
		print "quit"
		print "help"

player = Player()
output = Output()

while(True):
	userInput = raw_input("Please enter a command:")
	
	if userInput == 'quit':
		quit()
	if userInput == 'help':
		output.printHelp()
