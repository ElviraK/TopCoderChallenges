from itertools import combinations

class LittleElephantAndBooks:

 books = [23,14,49,62,56,82,39,55,77,19,93]
 number = 2

 def getNumber(num, book_set):
   combination_set = []
   
   for var in combinations(book_set, num):
     combination_set.append(sum(var))
     
   combination_set.sort()
   
   return combination_set[1]
