t=input()
while(t!=0):
    n=[]
    o=[]
    t-=1

    s=raw_input()
    s=s[::-1]
    if len(s)==1:
        print s
    else:
        for i in range(0,len(s),2):
            n.append(s[i])
        n= map(int,n)

        for j in range(1,len(s)-1,2):
            o.append(s[j])
        if o[0]=='/':
            x=n[0]/n[1]
        elif o[0]=='*':
            x=n[0]*n[1]
        elif o[0]=='+':
            x=n[0]+n[1]
        elif o[0]=='-':
            x=n[0]-n[1]
        l=2
        for k in range(1,len(o)):
            if o[k]=='+':
                x=x+n[l]
                l+=1
                continue
            elif o[k]=='-':
                x=x-n[l]
                l+=1
                continue
            elif o[k]=='*':
                x=x*n[l]
                l+=1
                continue
            elif o[k]=='/':
                x=x/n[l]
                l+=1
                continue
        print x
