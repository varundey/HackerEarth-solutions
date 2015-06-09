t=int(raw_input())
while(t!=0):
    t-=1
    n=int(raw_input())+1
    while (True):
        flag=0
        for i in range(2,n):
            if (n%i==0):
                flag+=1
                n+=1
                break
        if flag==0:
            print n
            break
