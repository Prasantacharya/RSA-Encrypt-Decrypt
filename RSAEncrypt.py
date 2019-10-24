# program for encyrpting my cribsheets and quiz answers
import sys
import random
import threading
sys.setrecursionlimit(1000000)
# take in the file text file
texFile = "https://www.overleaf.com/project/5dafb506de63b200015dec79"
# texFile = sys.argv[1]
# generate a public and private key
def gcd(a, b):
	# euclid gcd function
	if(b == 0):
		return a
	return gcd(b, a%b)

def modex(base, exp, mod):
    # input: n bit numbers base and exp, and integer exponent exp
    # output: X^{y} mod (mod)
    if exp == 0:
        return 1
    z = modex(base, int(exp//2), mod)
    if exp & 1:
        return base * (z * z) % mod
    else:
        return (z*z) % mod

def isPrime(num, k):
    # uses fermat's little theorem to find if a number is prime
    # recall: if n is prime, (1 <= a < p), then [(a)^(n-1) equivilant 1 mod a]
    for i in range(k):
        a = random.randint(1, num - 1)
        if modex(a, (num - 1), num) != 1:
            return False;
    return True

def randomPrime(randLow,randUpper): # gives really big prime numbers
	r = random.randint(randLow, randUpper)
	prime = 2
	for i in range(randLow, r):
		if isPrime(i, 1000): # checks if it is prime or not
			prime = i
	return prime

p = 2
q = 2
p = randomPrime(1000,1500)
q = randomPrime(1501,2000)
print("Prime one: ", p)
print("Prime two: ", q)
p = (2 ** p) - 1
q = (2 ** q) - 1

N = p * q # N
phi = (p - 1)* (q - 1) # phi
e = 0 # e has to be relatively prime to phi

temp = 3
for i in range(181, max(p, q)):
	if(gcd(i, phi) == 1):
		e = i # generates an e
		temp -= 1
		if(temp == 0):
			break
d = e + 1 # decryption key
print("Public key: ",N, ",", e)
from math import log2
print("Size of N in bits: ", log2(N))
print("Size of primes p and q in bits: ", log2(p), ",", log2(q))
'''
while((d*e) % phi is not 1):
	d += 1; # works but stupidly slow
'''
# hopefully a better algorithm for finding d:
def inverseMod(a,m):
	m0 = m
	y = 0
	x = 1

	if m == 1:
		return 0
	while a > 1:
		q = a // m
		t = m
		m = a % m
		a = t
		t = y
		y = x - q * y
		x = t
	if x < 0:
		x += m0
	return x

d = inverseMod(e, phi)
print("Private key: ", d)
