t=input()
while(t!=0):
	t-=1
	map(int,raw_input().split())
	print len(set(list(map(int,raw_input().split())))&set(list(map(int,raw_input().split()))))
