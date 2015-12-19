from math import sqrt as s
def isprime(n):
	count=0
	if n<=1:
		return False
	
	if n==2 or n==3:
		return True


	else:
		for i in range(2, int(s(n))+1 ):
			if(n%i == 0):
				count=0
				return False
			elif (n%i != 0):
				count+=1
			if count == int(s(n))-1:
				count=0
				return True

n=input()
while n!=0:
	n-=1
	a,b=map(int,raw_input().split())
	sum=0
	for i in range(a,b+1):
		if(isprime(i)):
			sum+=i

	print sum