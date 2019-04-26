#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172


from lab4_monsters import *
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	#####TODO######
	m1.resetHealth()
	m2.resetHealth()

	#next print out who is battling
	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())

	
	#Whose turn is it?
	attacker = None
	defender = None
	draw = random.random()
	if (draw >= 0.5):
		attacker = m1
		defender = m2
	else:
		attacker = m2
		defender = m1

	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	######TODO######
	
	
	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		before_health=defender.getHealth()
		
		#for each of these options, apply the appropriate attack and 
		#print out who did what attack on whom
		if(move >=1 and move <= 60):
			attacker.basicAttack(defender)
			print("{} used {} on {}".format(attacker.getName(), attacker.basicName(), defender.getName()))
		elif(move>=61 and move <= 80):
			#Defend!
			attacker.defenseAttack(defender)
			print("{} usef {} on {}".format(attacker.getName(), attacker.defenseName(), defender.getName()))
		else:
			#Special Attack!
			attacker.specialAttack(defender)
			print("{} used {} on {}".format(attacker.getName(), attacker.specialName(), defender.getName()))
		
		
		#Swap attacker and defender
		######TODO######
		temp = attacker
		attacker = defender
		defender = temp
		#Print the names and healths after this round
		######TODO######
		print("{} health: {}\n{} health: {}".format(attacker.getName(), attacker.getHealth(), defender.getName(), defender.getHealth()))
	#Return who won
	######TODO######
	if m1.getHealth() <= 0:
		return "{} wins".format(m2.getName())
	else:
		return "{} wins".format(m1.getName())
#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed
	
	random.seed(0)
	first = bear()
	second = lapras()
	
	winner = monster_battle(first,second)
	
	#Print out who won
	####TODO####
	print(winner)