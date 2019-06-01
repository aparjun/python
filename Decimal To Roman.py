n=input()
p=10**(len(n)-1)
li={10000:"H",5000:"G",1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
for i in n:
	j=int(i)
	if(j<=3):
		while(j>0):
		    print(li[p], end="")
		    j-=1
	elif(j==4):
		if(p==1000):
			while(j>0):
				print(li[p], end="")
				j-=1
		else:
			print(li[p], end="")
			print(li[p*5], end="")
	elif(j<=8):
	    j=j-5
	    print(li[p*5], end="")
	    while(j>0):
	        print(li[p], end="")
	        j-=1
	elif(j==9):
	    print(li[p], end="")
	    print(li[p*10], end="")
	p=p//10
