l = 300000000
n= input()
c=0
x=map(int,raw_input().split())
for i in x:
    if i<l:
        c+=1
print c
