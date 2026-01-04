zero knowledge chess engine
use neural network to prune search tree

Concepts:
- MinMax
- https://en.wikipedia.org/wiki/Bellman_equation
- png data set: https://archive.org/details/KingBase2018
- https://docs.h5py.org/en/stable/index.html



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

How Make `Serializer` faster:
1. Multiprocessing:
    - Rule (very important)
    - ❌ Workers do NOT write to the same file
    - ✅ Workers return small chunks
    - ✅ Main process writes to disk
2. Stream to disk instead of keeping X/Y in RAM


# Multi process / Multi thread / Gpu Process
## Multi process:


## Multi thread:
Python threads:

```
Time →
[ Thread A ] ██████░░░░████░░░░████
[ Thread B ] ░░░░████░░░░████░░░░
```
Because of the GIL:
- Only one thread runs Python code at a time
- Threads take turns
- No real parallelism

** Threads help only when waiting, not computing. **


## Gpu process:
**🚫 GPUs are bad at:**
- Text parsing
- Python objects
- Branch-heavy logic
- Sequential state updates
- Variable-length loops

** ✅ GPUs are good at: **
- Large numeric arrays
- Same operation on millions of elements
- Matrix / tensor math
- Neural network operations

