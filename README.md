zero knowledge chess engine
use neural network to prune search tree

Concepts:
- MinMax
- https://en.wikipedia.org/wiki/Bellman_equation
- png data set: https://archive.org/details/KingBase2018
- 



Definition: Value Network
v = f (state)  function will get board and return the value
v = -1 : black wins board state 
v = 0 : draw board state
v = 1: white board win state 

state:

extra states:
* castle available * 4 
* to move * 2 

pieces(2 + 2*7 = 16):
blank
pawn
bishop
knight 
rock
queen
king


8*8*4 + 1(who is next) = 257 bits vector of 0 and 1 