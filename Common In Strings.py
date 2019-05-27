#PF-Prac-45

def longest_common_substring(string1, string2):
    n=len(string1)
    s=""
    longest=0
    x_longest=0
    for i in range(0,n):  
        for j in range(1,n-i+1):
            if(len(s)<len(string1[i:j+1]) and string1[i:j+1] in string2):
                s=string1[i:j+1]
                longest=i
                x_longest=j+1
            
    
    return string1[longest: x_longest]

output=longest_common_substring("discatenation","concatenation")
print("The longest overlap of characters between string1 and string2:",output)
output1=longest_common_substring("assured","measured")
print("The longest overlap of characters between string1 and string2:",output1)
