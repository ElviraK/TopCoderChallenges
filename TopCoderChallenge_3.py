import collections

class ManySquares:
 
 def howManySquares(sticks):
     
    counter = 0
    y = collections.Counter(sticks)
	
    for x in y:
      
	   counter += y[x] / 4
	 
    return counter
