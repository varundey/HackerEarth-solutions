
a,b = map(int,raw_input().split())
x=a-b
if x%10 == 9:
	print x-1
else:
	print x+1