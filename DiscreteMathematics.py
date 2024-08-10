

def GCD(x: int, y: int, dbug: bool = False) -> int:
  """ Find the Greatest Common Divisor using Euclid's Algorithm. """
  # x and y are positive integers where x >= y
  if(x <= 1 or y <= 1): return 1
  a, b = (int(x), int(y)) if (x >= y) else (int(y), int(x))
  r, g = 1, 0
  while(r > 0):
    r = a % b
    d = a // b
    if(dbug): print(f"{a} = {d} * {b} + {r}")
    
    if(r>0): a,b = b,r
  if(dbug): print(f"The GCD of {x} and {y} is {b}.")
  return b


GCD(156, 54, True)
