n=int(input())
li=[]
for i in range(n):
	for j in range(n):
		if(j%2==0):
			print((j*n)+1+i,end=" ")
		else:
			print(((j+1)*n)-i,end=" ")
	print()	
