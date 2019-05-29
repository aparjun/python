#PF-Prac-45

def longest_common_substring(string1, string2):
    x_longest=0
    longest=0
    l=len(string1)
    for i in range(0,l):  
        for j in range(l-i,0,-1): 
            if(string1[i:i+j] in string2):
                if(longest<j):
                    longest=j
                    x_longest=i+j
    
    return string1[x_longest - longest: x_longest]

output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)
