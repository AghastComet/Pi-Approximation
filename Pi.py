from math import gcd, sqrt
from random import randint
looper=int(input("Iterations: "))
upper=int(input("Random Upper Bound: "))
upper+=1
total=looper
yes=0

def progPcentW(current,final):
	if int(current/final*100)==(current/final*100):
		print(int(current/final*100))

while looper > 0:
	
	progPcentW(total-looper,total)
	
	looper-=1
	
	if gcd(randint(1,upper),randint(1,upper))==1:
		yes+=1
print(sqrt(6*total/yes))