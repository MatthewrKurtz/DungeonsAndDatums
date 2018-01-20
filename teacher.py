# teacher bot - rock'em sock'em version
#
# teacher bot simulates a fight between two teams
# the robot will report the probability distribution that team 1 will be at 
# x health at the end of the match. The robot will also report a boolean 
# that team 1's health is within some margin at the end of the simulated match
#
# this is created in order to train a machine learning algorithm to tune 
# encounters for randomly generated attacking teams
#
# John Millner
# SwampHacks 2018 (MattHacks 2018) 1/20/2018
# https://github.com/johnmillner/Dungeons-Data

# inputs: 
#	csv file
#	list of names for team 1
#	list of names for team 2
#	team 1 health range 
#	team 1 ideal health percentage after match
#	ideal number of turns it takes for the encounter to finish

# outputs:
#	graphical representation of proability distribution of team 1's health afterwards
#	boolean value of whether the match was fair given the specified health range
#	number representing aproximated number of turns takes

# assumptions:
#	the fight is a direct confrontation - there are no sneak attack rounds at begining
#	all members of the encounter are equidistant apart and within attacking range
#	standard D&D rules are being used for encounters
#	characters have all spell slots available for the fight
#	bonus actions are not taken into account
#	everyone starts at full health

# how a fight is arranged:
#	each member is assigned an initiative probability
#	Turns[0->n] chosen being goes and follows the model of 
#		determine action probnability based on affinities
#		update probabilities of all beings affected
#	the encounter ends when the probabilities of an entire team are all below zero


import sys		 
import csv

class Being:
	def __init__ ( self, name, filename )
		
		#find the name in the csv file and set base stats
		with open( filename ), 'rb' ) as f:
			beings = csv.reader( f )
			for row in beings:
				if row[0] == name
					self.size 		= row[1]
					self.race 		= row[2]
					self.classy 	= row[3]
					self.typey 		= row[4]
					self.tag 		= row[5]
					self.alignment 	= row[6]
					self.AC 		= row[7]
					self.HP 		= row[8]
					self.STR 		= row[10]
					self.DEX 		= row[11]
					self.CON 		= row[12]
					self.INT 		= row[13]
					self.WIS 		= row[14]
					self.CHA 		= row[15]
					self.skills 	= row[16]
					self.items		= row[17]
					
		#find items
		#modify stats based on items
		#set probability desnity for initiative	: DEX + d20
		#set probability density for hitting	: prof + STR||DEX + d20
		#set probability density for attack		: STR||DEX + weaponDice
			

def main():
	filename	= sys.argv[1];
	team1 		= sys.argv[2];
	team2 		= sys.argv[3];
	health		= sys.argv[4];
	healthRange = sys.argv[5];
	turns		= sys.argv[6];
	
	
			

if __name__ == "__main__" : 
	main()
