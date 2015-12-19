t=input()
while t!=0:
	t-=1
	n,m = map(int,raw_input().split())
	while m!=0:
		m-=1
		x=0
		while n>0:
			x+= ((n%10)**2)
			n//=10
		n=x
	print x