n=int(input())
r=2*n-1
for i in range(r):
	for j in range(r):
		a=abs(i-r//2)
		b=abs(j-r//2)
		print(max(a,b)+1,end=" ")
	print()	
