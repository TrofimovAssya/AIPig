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
	either randomized or set to strategy 1 decision table
	"""
	if (random_probs):
		return numpy.random.rand(100,100,100)
	else:
		a = numpy.zeros((100,100,100))
		a[:,:,25:].fill(1.0)
		for i in xrange(100):
			a[:,:,100-i:].fill(1.0)
		return a


def AI_learn(decision_table,log,wins,lr=0.1):
	"""Player with a learned strategy 
	Function that teaches the AI player which were good decisions
	with an update according to preset learning rate(lr)
	"""
	if wins==True:
		for i in log:
				if decision_table[i[0], i[1], i[2]] < 0.5:
					decision_table[i[0], i[1], i[2]] = max(decision_table[i[0], i[1], i[2]] - lr,0)

				elif decision_table[i[0], i[1], i[2]] >= 0.5:
					decision_table[i[0], i[1], i[2]] = min(decision_table[i[0], i[1], i[2]] + lr,1)


	else:
		for i in log:
				if decision_table[i[0], i[1], i[2]] < 0.5:
					decision_table[i[0], i[1], i[2]] = min(decision_table[i[0], i[1], i[2]] + lr,1)
					
				elif decision_table[i[0], i[1], i[2]] >= 0.5:
					decision_table[i[0], i[1], i[2]] = max(decision_table[i[0], i[1], i[2]] - lr,0)
	

	return decision_table