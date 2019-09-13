st=input()
num=int(input())
def ad(n):
    s=str(n)
    t=0
    for i in range(len(s)):
        t=t+int(s[i])
    if(len(str(t))>1):
        return ad(t) 
    else:
        return t
f=ord(st[0])
if(len(st)>1):
    for i in range(1,len(st)):
        if(st[i]>='A' and st[i]<='Z'):
            f=abs(f-ord(st[i]))
            break
f=ad(f)
se=0
th=0
for i in range(len(st)):
    if(st[i]>='a' and st[i]<='z'):
        se=se+1
    if(st[i]>='A' and st[i]<='Z'):
        th=th+1
se=ad(se)
th=ad(th)
num=ad(num)
if(num%2!=0):
    num=num+1
print(f,end="")
print(se,end="")
print(th,end="")
print(num)
    
