t=input()
while(t!=0):
	t-=1
	n=raw_input()
	x= n[::-1]
	if(int(x)%2 == 0):
		print "EVEN"
	else:
		print "ODD"
