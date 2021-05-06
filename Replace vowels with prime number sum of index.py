def replacer(s, newstring, index):
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring
    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]
    
def prime(x):
	for i in range(2,(x//2)+1):
		if(x%i==0):
			return False
	return True		

def digitsum(x):
	sum=0
	for digit in str(x):
		sum += int(digit)
	return sum

s=input()
for i in range(len(s)):
	if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
		num=i*100
		primesum=0
		for j in range(1,num):
			if prime(j):
				primesum+=j
		while(len(str(primesum))>1):
			primesum=digitsum(primesum)
		s=replacer(s, str(primesum), i)
print(s)
		
		
		
		

