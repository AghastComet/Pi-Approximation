import sys
import math
import random

try:
	itters, limit = int(sys.argv[1]), int(sys.argv[2])
except ValueError:
	print("python piAprox.py [itterations] [upper limit]")
	exit()

noCommon=0
for i in range(itters,0,-1):
	if math.gcd(random.randint(1,limit), random.randint(1,limit))==1:
		noCommon+=1 #counts how many times two random numbers don't share a common denominator
pi = math.sqrt(6*itters/noCommon)
print(pi)
