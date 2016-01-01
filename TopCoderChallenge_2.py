class AddMultiply:

  def makeExpression(y):
     for i in range(2, 1000):
         x2 = y - i * i
         if x2 >= -1000 and x2 <= 1000 and x2 is not 0 and x2 is not 1:
             return [i, i, x2]


  print makeExpression(10)
