import numpy


"""

Game of Pig, developped for Prof. Aaron Courville IFT1015 class, at University of Montreal, Fall of 2014
by Assya Trofimov
petitkalimero@gmail.com 

Hard-coded strategies taken from http://nifty.stanford.edu/2010/neller-pig/

Couple of notes:

AIplayer was first imagined after not having enough inspiration to find the best strategy
The code works entirely as functions, no OOP (to stay true to my Fall 2014 knowledge)
Original code was lost, but was in JS (according to school language of choice fot IFT1015 class)

"""

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
