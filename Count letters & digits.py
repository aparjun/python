#PF-Prac-5
def count_digits_letters(sentence):
    a=0
    d=0
    result_list=[]
    for i in range(0,len(sentence)):
        if(sentence[i].isalpha()):
            a+=1
        elif(sentence[i].isdigit()):
            d+=1
    result_list.append(a)
    result_list.append(d)
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
