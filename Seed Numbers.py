#PF-Prac-7
def seed_no(number,ref_no):
    n=number
    p=1
    while(n>0):
        p=p*(n%10)
        n=n//10
    if(number*p==ref_no):
        return True
    else:
        return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))
