t=input()
while(t!=0):
    t-=1
    n=int(raw_input())
    x=list(bin(n)).count('1')
    while True:
        n+=1
        y=list(bin(n)).count('1')
        if (y==x):
            print n
            break
