//
Input:
load
3
app lol
old tip
odd itt
Output:
piot
Explanation: app is plain word. lol is secret key. p & l two times, so p is l.
//


Code:

d={}
o=input()
n=int(input())
for i in range(n):
	li=input().split(" ")
	p=li[0]
	s=li[1]
	for j in p:
		d[j]="0"
	for j in d:
		if(d[j]=="0"):
			for k in s:
				if(p.count(j)==s.count(k)):
					d[j]=k
ans=""
for i in o:
	ans=ans+d[i]
print(ans)
