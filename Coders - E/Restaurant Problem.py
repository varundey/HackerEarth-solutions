num=raw_input()
l=len(num)
ans=0
for i in range (l):
	for j in range (1,l-i+1):
		n=int(num[i:i+j])
		if (num[i:i+j][0]=='0' and len(num[i:i+j])!=1):
			ans+=0
		else:
			#print n
			if (n%8==0):
				ans+=1;
print ans
