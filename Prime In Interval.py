def prime(x):
	for i in range(2,(x//2)+1):
		if(x%i==0):
			return False
	return True		
def fi(x,y):
    for j in range(x,y+1):
        if(prime(j)):
	        print(j)
x=2
y=12
fi(x,y)
