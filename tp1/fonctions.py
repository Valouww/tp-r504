def puissance(a,b):
   if not type(a) is int or not type(b) is int:
      raise TypeError("Only integers are allowed")
   elif a==0:
      if b > 0:
          return 1
      else:
         return False
   else:
      result=1
      for i in range(abs(b)):
         result *= a
      return result
