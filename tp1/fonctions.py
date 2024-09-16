def puissance(a,b):
   if not type(a) is int or not type(b) is int:
      raise TypeError("Only integers are allowed")
   elif b <= 0:
       raise TypeError("La puissance doit être possitive")
   return a**b
