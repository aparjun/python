#PF-Assgn-60
from collections import OrderedDict 

def remove_duplicates(value):
    d = OrderedDict()
    st=""
    for i in value:
        d[i]=0
    for i in d:
    	st+=i
    return st    

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
