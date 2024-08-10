

def GCD(x: int, y: int, ext: bool = False, dbug: bool = False) -> int:
  """ Find the Greatest Common Divisor using Euclid's Algorithm. """
  # x and y are positive integers where x >= y
  if(x <= 1 or y <= 1): return 1
  a, b, swap = (int(x), int(y), False) if (x >= y) else (int(y), int(x), True)
  r0,r1,s0,s1,t0,t1 = a,b,1,0,0,1
  while(r1 > 0):
    d = r0 // r1
    r0, r1 = r1, r0 - d * r1
    s0, s1 = s1, s0 - d * s1
    t0, t1 = t1, t0 - d * t1
    if(dbug): print(f"{a} = {d} * {b} + {r1}")
    if(r1>0): a,b = b,r1
  if(swap): s0,t0,s1,t1 = t0,s0,t1,s1
  if(dbug):
    print(f"The GCD of {x} and {y} is {b}.")
    if(s0 * x > t0 * y):
      print(f"{b} = {s0} * {x} - {-t0} * {y}.")
    else:
      print(f"{b} = {t0} * {y} - {-s0} * {x}.")
  if(ext):
    return b,s0,t0
  else:
    return b


def MultInvXModN(x: int, n: int, dbug: bool = False) -> int:
  """ The Multiplicative Inverse of X Mod N """
  g,s,t = GCD(x, n, ext=True, dbug=dbug)
  if(dbug): print(f"g,s,t = {g},{s},{t}")
  if(g != 1): 
    if(dbug): print(f"{x} and {n} are not coprime, no inverse exists.")
    return n
  if(dbug): print(f"The multiplicative inverse of {x} mod {n} is {s % n}.")
  return s % n


def fastExp(x: int, y: int, n: int) -> int:
  """ Fast Integer Exponentiation for large numbers """
  p = 1 # p holds the partial result.
  s = x # s holds the current x**(2j).
  r = y # r is used to compute the binary expansion of y.  
  while(r > 0):
    if(r % 2 == 1):
      p = (p * s) % n
    s = (s * s) % n
    r //= 2
  return p


def crypt(k: int, N: int, m: int = 0, c: int = 0, dbug:bool = False) -> int:
  """ Encrypts and decrypts a coded message """
  #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z 
  # 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
  if(m == 0 and c == 0): return 0
  if(m != 0):
    x = (m + k) % N
    if(dbug): print("Encrypted:", x)
  if(c != 0):
    x = (c - k) % N
    if(dbug): print("Decrypted:", x)
  




if __name__ == "__main__":
  #GCD(76, 26, dbug=True)
  #print(MultInvXModN(54,61, dbug=True))
  #print(fastExp(4, 14, 7))
  crypt(m=6, k=7, N=73, dbug=True)