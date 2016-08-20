#### Whip staking simulator ###
###############################
# Written by Levon Dovlatyan ##
# Last updated 20 Aug. 2016 ###
###############################

import numpy as np
import matplotlib.pyplot as plt

# set combat stats for attack strength defence and hp
a,s,d,h = 99,99,99,99

# equipment bonus
Ba = 90 # attack slash bonus for whip
Bs = 86 # strength bonus for whip
Bd = 0 # defence slash bonus for whip

def changeStance(stance):
	""" calculates effective atk/str/def levels based on stance """
	# controlled stance gives +1 to all 3 skills
	# aggresive gives +3 to respective skill
	# use keywords for argument 'control','atk','str','def'
	Aa,As,Ad = a+8,s+8,d+8
	if stance == 'control':
		Aa,As,Ad = (Aa+1,As+1,Ad+1)
	elif stance == 'atk':
		Aa,As,Ad = (Aa+3,As,Ad)
	elif stance == 'str':
		Aa,As,Ad = (Aa,As+3,Ad)
	elif stance == 'def':
		Aa,As,Ad = (Aa,As,Ad+3)
	else:
		print 'unknown stance given'
	return (Aa,As,Ad)
def calcMaxRolls(stance):
	""" calculates max rolls for atk/str/def """
	Aa,As,Ad = changeStance(stance)

	AsMax = np.floor(0.5 + As*(Bs+64)/640)
	AaMax = Aa*(Ba+64)
	AdMax = Ad*(Bd+64)
	return (AaMax,AsMax,AdMax)

def calcHit(stance):
	""" calculate chance to hit """
	AaMax,AsMax,AdMax = calcMaxRolls(stance)
	if AaMax > AdMax:
		hitChance =  (1 - (AdMax+2.)/(2*(AaMax+1)))
	else:
		hitChance =  AaMax/(2.*(AdMax+1))
	roll = np.random.rand(1)[0]

	if roll < hitChance: # hit splash!
		dmg = np.random.randint(0,26,size=1)[0]
	else:
		dmg = 0
	return dmg

def duel(styles=('atk','atk'),runs=1,info=False):
	P1win,P2win = 0,0 # number of wins
	for i in range(runs+1):
		print 'Duel %s/%s' % (str(i),str(runs))
		P1hp,P2hp = h,h # set health
		pid = np.round(np.random.rand(1)[0])

		while True:
			if pid: # player 1 wins pid
				# calculate player hits
				P1dmg = calcHit(styles[0])
				P2dmg = calcHit(styles[0])
				# calculate player hp after hit
				P2hp-=P1dmg
				if P2hp <= 0:
					P1win+=1
					if info:
						print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg%s' % (str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))
					break
				P1hp -= P2dmg
				if P1hp <= 0:
					P2win+=1
					if info:
						print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg%s' % (str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))
					break
				if info:
					print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg:%s' %(str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))
			else: # player 2 wins pid
				# calculate player hits
				P1dmg = calcHit(styles[0])
				P2dmg = calcHit(styles[0])
				# calculate player hp after hit
				P1hp-=P2dmg
				if P1hp <= 0:
					P2win+=1
					if info:
						print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg%s' % (str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))
					break
				P2hp -= P1dmg
				if P2hp <= 0:
					P1win+=1
					if info:
						print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg%s' % (str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))
					break
				if info:
					print '(P1) hp:%s dmg:%s | (P2) hp:%s dmg:%s' %(str(P1hp),str(P1dmg),str(P2hp),str(P2dmg))			
	runs = runs + 0.0	
	return 	(P1win/runs,P2win/runs)
		

print duel(('def','atk'),10000,False)


