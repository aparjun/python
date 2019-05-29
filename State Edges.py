#PF-Prac-41
# Part-1
def get_edges(pollsters_stateedge_dict,state):
    result_list=[]
    for i in pollsters_stateedge_dict:
        li=[]
        li.append(i)
        if(state in pollsters_stateedge_dict[i]):
            li.append(pollsters_stateedge_dict[i][state])
        else:
            li.append(None)
        li=tuple(li)
        result_list.append(li)
    return result_list

# Part-2
def find_pollster_states(pollsters_stateedge_dict):
    result_dict={}
    for i in pollsters_stateedge_dict:
        li=[]
        for j in pollsters_stateedge_dict[i]:
            li.append(j)
        result_dict[i]=li    
    return result_dict

pollsters_stateedge_dict = { 
              "Gallup": { "WA": 7, "CA": 15, "UT": -30 }, 
              "SurveyUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0 }, 
              "Omniscient": { "AK": -14.0, "WA": -2.3, "CA": 20.9 }
             } 
state='WA'
print("Pollsters, States and its edge details:",pollsters_stateedge_dict)
print("Given State:",state)
output=get_edges(pollsters_stateedge_dict,state)
print("Pollster Edge details for the given state:", output)  

output1=find_pollster_states(pollsters_stateedge_dict)
print("Pollster and their entire state details:",output1)
