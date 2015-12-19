n=input()
while(n!=0):
    n-=1
    s=raw_input()
    t=''
    t+=s[0]
    for i in range(0,len(s)-1):
        if s[i]!= s[i+1]:
            t+=s[i+1]
    print t
