import numpy

"""

Game of Pig, developped for IFT1015 class, at University of Montreal, Fall of 2014
by Assya Trofimov
petitkalimero@gmail.com 
Prof. Aaron Courville
Hard-coded strategies taken from http://nifty.stanford.edu/2010/neller-pig/

Couple of notes:

AIplayer was first imagined after not having enough inspiration to find the best strategy
The code works entirely as functions, no OOP (to stay true to my Fall 2014 knowledge)
Original code was lost, but was in JS (according to school language of choice fot IFT1015 class)

"""

def roll():
	return numpy.random.randint(1,6)

def Strategy1_Decision(i,j,k):

	"""Player with a set strategy 
	strategy1:
	let i=players score, j=opponents score, k=current turn total
	Holds at k > 25	or k >= 100-i

	"""
	if k>25 or k >= 100-i:
		return "hold"

	else:
		return "roll"


def Strategy2_Decision(i,j,k):

	"""Player with a set strategy 
	strategy2:
	If i >= 69 or j >= 69, roll for the goal.  Otherwise, hold at the greater of 19 and j - 14.

	"""

	if i>=69 or j >= 69:
		return "roll"

	elif k > (max(19,j-14)):
		return "hold"

	else:
		return "roll"


def Strategy3_Decision(i,j,k):

	"""Player with a set strategy 
	strategy3:
	If i >= 71 or j >= 71, roll for the goal.  Otherwise, hold at 21 + round((j - i) / 8).

	"""

	if i>=71 or j >= 71:
		return "roll"

	elif k >= (21+round((j-i)/8)):
		return "hold"

	else:
		return "roll"

def Strategy4_Decision(i,j,k, number):

	"""Player with a set strategy 
	strategy4:
	Roll only 4 times

	"""

	if number < 4:
		return "roll"

	else:
		return "hold"

def AI_Decision(i,j,k,decision_table):
	"""Player with a learned strategy 
	strategyAI:
	The decision_table that is passed is learned through game play
	At first it is random, with values from [0,1] where value is the probability of a roll
	"""
	decide = numpy.random.rand()

	if decide < (decision_table[i,j,k]):
		return "hold"
	else:
		return "roll"

def AI_create(random_probs=False):
	"""Player with a learned strategy 
	Function that creates a decision_table for the AIplayer
	either randomized of at 0.5 each
	"""
	if (random_probs):
		return numpy.random.rand(100,100,100)
	else:
		a = numpy.zeros((100,100,100))
		a.fill((0.5))
		return a


def AI_learn(decision_table,log,wins,lr=0.1):
	"""Player with a learned strategy 
	Function that teaches the AI player which were good decisions
	with an update according to preset learning rate(lr)
	"""
	if wins==True:
		for i in log:
				if decision_table[i[0], i[1], i[2]] < 0.5:
					decision_table[i[0], i[1], i[2]] -= 0.1

				elif decision_table[i[0], i[1], i[2]] >= 0.5:
					decision_table[i[0], i[1], i[2]] += 0.1


	else:
		for i in log:
				if decision_table[i[0], i[1], i[2]] < 0.5:
					decision_table[i[0], i[1], i[2]] += 0.1
					
				elif decision_table[i[0], i[1], i[2]] >= 0.5:
					decision_table[i[0], i[1], i[2]] -= 0.1
	

	return decision_table

def turn(i,j,player,verbose=True, decision_table=None, roll_number=None, log=None):
	"""Game of Pig - one turn
	making the decision!

	"""
	action = "roll"
	k = 0

	while action=="roll":
		dice = roll()

		### roll counts for strategy 4
		if not(roll_number==None):
			roll_number+=1
		if (verbose):
			print "roll number "+ str(roll_number)


		### adding prints
		if (verbose):
			print ("Player rolled: " + str(dice))
		### if roll a 1, throw no points are scored!
		if dice==1:
			break
		### add up the points rolled to hand
		k+=dice

		### determine which Strategy is used
		if player==AI_Decision:

			action=player(i,j,k, decision_table)

		elif player==Strategy4_Decision:

			action=player(i,j,k, roll_number)
		else:
			action=player(i,j,k)

		if (verbose):
			print ("Player decided to: " + str(action))
			print ("Player has " + str(k) + " points in hand: ")

		log.append([i,j,k,action])


	if action == "hold":
		i+=k

	return i,j,k,log



def game():
	"""Game of Pig
	i_1 and i_2 are the player's totals
	j_1 and j_2 are the opponant's totals
	yes, yes i_1 = j_2 and vice-versa...

	k_1 and k_2 are the in hand values
	"""
	dt = AI_create(random_probs=True)
	log1 = []
	log2 = []
	i = 0
	j = 0
	while i<=100 and j<=100:
		i,j,k,log1 = turn(i,j,AI_Decision,decision_table=dt,log=log1)
		print "Player 1: " + str(i)
		print "Player 2: " + str(j)
		if i>=100:
			break
		j,i,k,log2 = turn(j,i,AI_Decision,decision_table=dt,log = log2)
		print "Player 1: " + str(i)
		print "Player 2: " + str(j)
		if j>=100:
			break
	print i, j	
	if i > j:

		print ("**************  Winner: player 1")
	else:
		print ("**************  Winner: player 2")

def test_game(decision_table):
	"""Game of Pig
	i_1 and i_2 are the player's totals
	j_1 and j_2 are the opponant's totals
	yes, yes i_1 = j_2 and vice-versa...

	k_1 and k_2 are the in hand values
	"""
	AIwins = 0
	verbose=False
	for game_ix in xrange(1000):
		dt = decision_table
		log1 = []
		log2 = []
		i = 0
		j = 0
		while i<=100 and j<=100:
			i,j,k,log1 = turn(i,j,AI_Decision,verbose=False, decision_table=dt,log=log1)
			if (verbose):
				print "Player 1: " + str(i)
				print "Player 2: " + str(j)
			if i>=100:
				break
			j,i,k,log2 = turn(j,i,AI_Decision,verbose=False, decision_table=dt,log = log2)
			if (verbose):
				print "Player 1: " + str(i)
				print "Player 2: " + str(j)
			if j>=100:
				break

		if i > j:

			print ("**************  Winner: player 1")
			AIwins+=1
		else:
			print ("**************  Winner: player 2")
	print AIwins
	print ("AI has won " + str(float(AIwins)/1000*100) + " percent of games")



"""Game of Pig
i_1 and i_2 are the player's totals
j_1 and j_2 are the opponant's totals
yes, yes i_1 = j_2 and vice-versa...

k_1 and k_2 are the in hand values
"""
verbose=False
dt = AI_create(random_probs=True)
for i in xrange(100000):
	print ("game number "+ str(i))
	log1 = []
	log2 = []
	i = 0
	j = 0
	while i<=100 and j<=100:
		i,j,k,log1 = turn(i,j,AI_Decision,verbose=False, decision_table=dt,log=log1)
		if (verbose):
			print "Player 1: " + str(i)
			print "Player 2: " + str(j)
		if i>=100:
			break
		j,i,k,log2 = turn(j,i,AI_Decision,verbose=False, decision_table=dt,log = log2)
		if (verbose):
			print "Player 1: " + str(i)
			print "Player 2: " + str(j)
		if j>=100:
			break
	if i > j:
		AI_learn(decision_table=dt,log = log1,wins=True,lr=0.1)
		AI_learn(decision_table=dt,log = log2,wins=False,lr=0.1)
	else:
		AI_learn(decision_table=dt,log = log2,wins=True,lr=0.1)
		AI_learn(decision_table=dt,log = log1,wins=False,lr=0.1)

