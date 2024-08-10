from random import randint as rnd

def gcd(x:int, y:int, ext:bool = False, dbug:bool = False) -> int:
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


def multInvXModN(x:int, n:int, dbug:bool = False) -> int:
  """ The Multiplicative Inverse of X Mod N """
  g,s,t = gcd(x, n, ext=True, dbug=dbug)
  if(dbug): print(f"g,s,t = {g},{s},{t}")
  if(g != 1): 
    if(dbug): print(f"{x} and {n} are not coprime, no inverse exists.")
    return n
  if(dbug): print(f"The multiplicative inverse of {x} mod {n} is {s % n}.")
  return s % n


def fastExp(x:int, y:int, N:int) -> int:
  """ Fast Integer Exponentiation for large numbers """
  p = 1 # p holds the partial result.
  s = x # s holds the current x**(2j).
  r = y # r is used to compute the binary expansion of y.  
  while(r > 0):
    if(r % 2 == 1):
      p = (p * s) % N
    s = (s * s) % N
    r //= 2
  return p


def crypt(k:int, N:int, m:int = None, c:int = None, dbug:bool = False) -> int:
  """ Encrypts and decrypts a coded message """
  #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z 
  # 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
  if(m != None):
    x = (m + k) % N
    if(dbug): print("Encrypted:", x)
    return x
  if(c != None):
    x = (c - k) % N
    if(dbug): print("Decrypted:", x)
    return x
  return 0


def privateKey(p:int, q:int, e:int = None, dbug:bool = False) -> int:
  """ Calculating keys for RSA Public Key Encryption """
  N = p * q
  phi = (p - 1) * (q - 1)
  g = 0
  once = (e != None)
  while(once or g != 1):
    if(not once) : e = rnd(2, phi) #859
    g, a, b = gcd(e, phi, ext=True)
    if(once and g != 1):
      if(dbug): print("Your choice of e is not coprime with phi.")
      return None, None, None
    once = False
  d = a % phi
  if(dbug): print(f"The public keys are {N} and {e}, and the private key is {d}.")
  return N, e, d


def rsa(m:int = None, c:int = None, N:int = None, p:int = None, q:int = None,
        e:int = None, d:int = None, dbug:bool = False) -> int:
  """ Encrypts and decrypts a coded message using RSA Public Key Encryption """
  if(N == None):
    if(p == None or q == None):
      if(dbug): print("Invalid Key configuration!")
      return 0
    else:
      N,e,d = privateKey(p,q,e,dbug)
  if(m != None):
    x = fastExp(m, e, N)
    if(dbug): print("Encrypted:", x)
    return x
  if(c != None):
    x = fastExp(c, d, N)
    if(dbug): print("Decrypted:", x)
    return x
  if(dbug): print("Empty message, nothing to encrypt or decrypt.")
  return 0

  


if __name__ == "__main__":
  #GCD(76, 26, dbug=True)
  #print(MultInvXModN(54,61, dbug=True))
  #print(fastExp(4, 14, 7))
  #crypt(m=6, k=7, N=73, dbug=True)
  #privateKey(p=13, q=17, e=67, dbug=True)
  #c = rsa(m=1211, e=859, N=1829, d=79, dbug=True)
  #rsa(e=7, N=33, d=3, dbug=True)
  rsa(c=8, p=13, q=7, e=59, d=11, dbug=True)
  