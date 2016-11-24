import numpy
from pig_strategies_hardcoded import Strategy1_Decision, Strategy2_Decision, Strategy3_Decision, Strategy4_Decision
from pig_AI import AI_Decision, AI_create, AI_learn
"""

Game of Pig, developped for IFT1015 class, at University of Montreal, Fall of 2014
by Assya Trofimov
petitkalimero@gmail.com 
Hard-coded strategies taken from http://nifty.stanford.edu/2010/neller-pig/

Couple of notes:

AIplayer was first imagined after not having enough inspiration to find the best strategy
The code works entirely as functions, no OOP (to stay true to my Fall 2014 knowledge)
Original code was lost, but was in JS (according to school language of choice fot IFT1015 class)

"""

def roll():
	return numpy.random.randint(1,6)


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

def test_game(decision_table, strategy_opponent):
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
			j,i,k,log2 = turn(j,i,strategy_opponent,decision_table = dt, log=log2,verbose=False)
			if (verbose):
				print "Player 1: " + str(i)
				print "Player 2: " + str(j)
			if j>=100:
				break

		if i > j:

			#print ("**************  Winner: player 1")
			AIwins+=1
	#	else:
	#		print ("**************  Winner: player 2")
	print AIwins
	print ("AI has won " + str(float(AIwins)/1000*100) + " percent of games")
	return AIwins



"""Game of Pig
i_1 and i_2 are the player's totals
j_1 and j_2 are the opponant's totals
yes, yes i_1 = j_2 and vice-versa...

k_1 and k_2 are the in hand values
"""


verbose=False
dt = AI_create(random_probs=False)
results = []
for game_number in xrange(1000000):
	print ("game number "+ str(game_number))
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
		j,i,k,log2 = turn(j,i,Strategy1_Decision,verbose=False, decision_table=dt,log = log2)
		if (verbose):
			print "Player 1: " + str(i)
			print "Player 2: " + str(j)
		if j>=100:
			break
	if i > j:
		AI_learn(decision_table=dt,log = log1,wins=True,lr=0.3)
		AI_learn(decision_table=dt,log = log2,wins=False,lr=0.3)
	else:
		AI_learn(decision_table=dt,log = log2,wins=True,lr=0.3)
		AI_learn(decision_table=dt,log = log1,wins=False,lr=0.3)
	if numpy.log10(game_number)%1 == 0 or (game_number%1000==0):
		number_of_wins1 = test_game(dt, Strategy1_Decision)
		number_of_wins2 = test_game(dt, Strategy2_Decision)
		number_of_wins3 = test_game(dt, Strategy3_Decision)
		number_of_wins4 = test_game(dt, Strategy4_Decision)
		results.append([game_number, number_of_wins1, number_of_wins2, number_of_wins3, number_of_wins4])
