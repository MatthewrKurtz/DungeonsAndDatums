#!/usr/bin/python

import random
import sys
import operator
import mysql.connector 
import MySQLdb

class Monster:
	def __init__ ( self, name, hp, ac, attacks ):
		self.name 		= name
		self.hp 		= hp
		self.ac 		= ac
		self.attacks 	= attacks
		self.maxAttack 	= 0
		self.initiative = 0
		self.team		= None
		
		for attack in attacks:
			if attack.avg > self.maxAttack:
				self.maxAttack = attack.avg
		
class Attack:
	def __init__ ( self, rawAttack ):
		self.name 		= rawAttack[0]
		self.noDice 	= rawAttack[1]
		self.sizeDice 	= rawAttack[2]
		self.modifier 	= rawAttack[3]
		self.avg 		= rawAttack[4]
						

def simulate_manyMonsters ( team1, team2 ):
	counter = 0
	
	#assign team numbers
	for monster in team1:
		monster.team = 1	
	for monster in team2:
		monster.team = 2
		
	#assign initiative for each member
	for monster in team1 + team2:
		monster.initiative = random.random()
	
	#create fighting order
	order = sorted( team1+team2, key = operator.attrgetter('initiative') )
	
	while len( team1 ) > 0 and len( team2 ) > 0:
		#this guy attacks a random guy on the other team
		attacker = order[ counter % ( len( team) + len( team2 )) ]
		
		#determine which team the attacker and defender are on
		if attacker.team is 1:
	  		defense = team2
		else:
			defense = team1
			
		#pick random guy on defense to take the hit
		catcher = random.randin( 0, len( defense ) - 1 )
		
		#determine hit chance
		hit = random.randint( 1, 20 )			
		
		#see if it actually hit
		if hit > defense[ catcher ].ac:
			defense[ catcher ].hp = defense[ catcher].hp - attacker.maxAttack
			
		#determine if catcher died
		if defense[ catcher ].hp <= 0:
			defense.remove( catcher )
			
		counter = counter + 1 
		
	if ( len( team1 ) > 0 ):
		victor = "team 1"
	else:
		victor = "team 2"
	print "Victor is ", victor.name," and completed in ", counter, " turns!"
	
	
def main():
	raw1 = sys.argv[1]
	raw2 = sys.argv[2]
	
	#connect to database - yes i know how insecure this is - dont judge :'(
	conn = mysql.connector.connect(host='localhost',database='dungeonsAndData',user='root',password='Littlefoot')
	cursor = conn.cursor()
	
	team1 = list()
	team2 = list()
	#find the monsters
	for monster in raw1:
		# find the monster AC and HP in monsters
		# find the monsters attacks in monster_attacks
		# find the attack properties in attacks
		#	piece together a list of valid list of attacks
		# piece together a valid moster
		# add monster to list	
		
		# generate string for mySQL
		tmp = "SELECT * FROM monsters WHERE name LIKE '"+ monster +"'"		
		# grab the monsters file	
		cursor.execute( tmp )
		# go fetch it - now we have HP & AC									
		profile = cursor.fetchone()		
		
		# generate string for mySQL to find attacks									
		tmp = "SELECT * FROM monster_attacks WHERE monster LIKE '"+ monster +"'"	
		# find the attack files
		cursor.execute( tmp )
		# go fetch ALL of them
		rawAttacks = cursor.fetchall()
		
		# create list for attacks to fall into
		attacks = list()
		for attack in rawAttacks:
			# generate string for mySQL to derive attacks
			tmp = "SELECT * FROM attacks WHERE name LIKE '"+ attack[1] +"'"	
			# grab the attack file	
			cursor.execute( tmp )
			# go fetch it - now we have the full attack profile								
			move = cursor.fetchone()	
			attacks.append( Attack( move ) ) 
		m = Monster( profile[0], profile[1], profile[2], attacks)
		team1.append( m )
		
		#find the monsters
		for monster in raw2:
			# find the monster AC and HP in monsters
			# find the monsters attacks in monster_attacks
			# find the attack properties in attacks
			#	piece together a list of valid list of attacks
			# piece together a valid moster
			# add monster to list	
		
			# generate string for mySQL
			tmp = "SELECT * FROM monsters WHERE name LIKE '"+ monster +"'"		
			# grab the monsters file	
			cursor.execute( tmp )
			# go fetch it - now we have HP & AC									
			profile = cursor.fetchone()		
		
			# generate string for mySQL to find attacks									
			tmp = "SELECT * FROM monster_attacks WHERE monster LIKE '"+ monster +"'"	
			# find the attack files
			cursor.execute( tmp )
			# go fetch ALL of them
			rawAttacks = cursor.fetchall()
		
			# create list for attacks to fall into
			attacks = list()
			for attack in rawAttacks:
				# generate string for mySQL to derive attacks
				tmp = "SELECT * FROM attacks WHERE name LIKE '"+ attack[1] +"'"	
				# grab the attack file	
				cursor.execute( tmp )
				# go fetch it - now we have the full attack profile								
				move = cursor.fetchone()	
				attacks.append( Attack( move ) ) 
			m = Monster( profile[0], profile[1], profile[2], attacks)
			team2.append( m )
		
		
	
	simulate_manyMonsters( team1, team2 )
		
	
			
	
if __name__ == "__main__": 
	main()
	
