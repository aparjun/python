li=list(input().split())
for i in li:
	n=len(i)
	for j in range(n):
		ch=chr(ord(i[j])+n-j-1)
		if(ch>'z'):
			ch=chr(ord('a')+ord(ch)-ord('z')-1)
		print(ch,end="")
	print(end=" ")	
//input= yum feed 
//output=avm igfd
