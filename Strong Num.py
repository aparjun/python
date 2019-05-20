#PF-Exer-26

def factorial(number):
    f=1
    while(number>0):
        f=f*number
        number-=1
    return f    


def find_strong_numbers(num_list):
    for n in num_list:
        s=0
        print(n)
        if(n==0):
            s=1
        m=n
        while(m>0):
            s=s+factorial(m%10)
            m=m//10
        if(s!=n):
            num_list.remove(n)
    return num_list        


num_list=[145,375,0,100,2]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
