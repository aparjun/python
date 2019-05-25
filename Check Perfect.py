def perfect(x):
	s=0
	for i in range(1,(x//2)+1):
		if(x%i==0):
			s+=i
	if(s==x):
		return True
	else:
		return False
x=497
print(perfect(x))
