prime=[67,71,73,79,83,89,97,101,103,107,109,113]
t=input()
while(t!=0):
    t-=1
    x=''
    s=list(raw_input())
    for i in s:
        if ord(i) not in prime:
            x+=i
    if len(x)!=0:
        print x
    else:
        print "NULL"
