class LittleElephantAndBooks:

 def getNumber(pages, number):
   pages.sort()
   element = pages[number]
   pages = pages[:number-1]

   return sum(pages) + element
