# AI for Game of Pig


Game of Pig, originally developped for Prof. Aaron Courville's IFT1015 class, at University of Montreal in the Fall of 2014.

## Why?

The AI-strategy was first imagined as a lazy solution to finding a good strategy for the class assignment.

## Strategies (Hard-coded)

The hard-coded strategies taken from http://nifty.stanford.edu/2010/neller-pig/. 
let i=players score, j=opponents score, k=current turn total

Strategy 1: 	Holds at k > 25	or k >= 100-i \n
Strategy 2: 	If i >= 69 or j >= 69, roll for the goal.  Otherwise, hold at the greater of 19 and j - 14. \n
Strategy 3: 	If i >= 71 or j >= 71, roll for the goal.  Otherwise, hold at 21 + round((j - i) / 8). \n
Strategy 4: 	Holds when you have rolled 4 times \n


## Pig AI
Generate a 3d matrix of size (100,100,100), with every coordinate symbolizing (i = player's score,j = opponent's score,k = current turn total)
Each slot contains a threshold. For each decision: roll a random number between [0,1]. If the roll > threshold, then roll, otherwise hold.

The learning: 
Play many games. Record all moves. Penalize moves that resulted in a loss. Bonify moves that resulted in a win.

## Performance
After 100000 training steps, AI_pig outperforms strategies 2,3,4 but not 1.
Will be doing more testing....
