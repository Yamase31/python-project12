INFINITY = "-"



def addWithInfinity(a, b):
   """Adds a and b, with the possibility that either might be infinity."""
   if a == INFINITY or b == INFINITY:
      return INFINITY
   else:
      return a + b
    
def minWithInfinity(a, b):
   """Finds the minimum of a and b, with the possibility that either might be infinity."""
   if a == INFINITY and b != INFINITY:
      return b
   elif a != INFINITY and b == INFINITY:
      return a
   elif a > b:
      return b
   elif b > a:
      return a
   else:
      return INFINITY
    

def lessThanWithInfinity(a, b):
   """Returns a < b, with the possibility that either might be infinity."""
   if a == INFINITY and b != INFINITY:
      return a
   elif a != INFINITY and b == INFINITY:
      return b
   elif a > b:
      return a
   elif b > a:
      return b
   else:
      return INFINITY
