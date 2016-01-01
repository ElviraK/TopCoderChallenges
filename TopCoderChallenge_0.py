import operator

class CandidatesSelectionEasy:
 score = ["ACB", "BAC", "CBA"]
 x = 1
    
 def sort_method(sc, xx):
    tuples = []
    for i in range(len(sc)):
	   arr = list(sc[i])
	   tuples.append((arr[xx],i))
	
    tuples = sorted(tuples, key = operator.itemgetter(0))
    print [tuples[xx][1] for xx in range(len(tuples))]
	
 sort_method(score,x)
