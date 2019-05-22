def prime(x):
	for i in range(2,(x//2)+1):
		if(x%i==0):
			return False
	return True		
def fi(x):
    for j in range(2,x+1):
        if(prime(j) and x%j==0):
	        print(j)
x=12
fi(x)
