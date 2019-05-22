def prime(x):
	for i in range(2,(x//2)+1):
		if(x%i==0):
			return False
	return True		
x=0
if(prime(x)):
	print("Yes")
else:
	print("No")
