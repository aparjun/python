#PF-Prac-20
import math
def ducci_sequence(test_list,n):
    while(n>=0):
        t=test_list[0]
        l=len(test_list)
        for i in range(0,l-1):
            test_list[i]=abs(test_list[i+1]-test_list[i])
        test_list[l-1]=abs(test_list[l-1]-t)  
        n-=1
    final_list=test_list    
    return final_list

ducci_element=ducci_sequence([7, 60, 861, 3070] , 3)
print(ducci_element)
