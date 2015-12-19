t=int(raw_input())
while(t!=0):
    t-=1
    a,b=map(int,raw_input().split())
    a=a*(10**18)
    if a%b==0:
        print "TCET Rocks!"
    else:
        print "It's Ok!"
