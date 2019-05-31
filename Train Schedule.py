#PF-Prac-17
train_list=[
{"train_no":16453,"name":"Prasanti Express","from":"SBC","to":"BBS","days_of_run":['Mo','We','Th'],"sleeper_fare":600,"ac_fare": 987},
{"train_no":25627,"name":"Karnataka Express","from":"SBC","to":"DEC","days_of_run":['Su','Tu'],"sleeper_fare":1600,"ac_fare": 2500},
{"train_no":22642,"name":"Trivandrum SF Express","from":"VSKP","to":"TVM","days_of_run":['Mo','Tu','We','Th','Fr','Sa'],"sleeper_fare":800,"ac_fare": 1256},
{"train_no":22905,"name":"Okha Howrah Express","from":"ST","to":"KOAA","days_of_run":['We','Sa'],"sleeper_fare":987,"ac_fare": 2879}]

def get_train_name (train_no):
    train_name=''
    for items in train_list:
        if(items['train_no']==train_no):
            train_name=items["name"]
    if(len(train_name)>0):
        return (train_name)
    else:
        return ("Invalid train_no")

def get_trains_for_day(day_of_run):
    list1 = []
    for items in train_list:
        temp_list = items["days_of_run"]
        if day_of_run in temp_list:
            list1.append(items['train_no'])
    return list1
    #start writing your code here
    
def get_total_fare(train_no,passenger_dict):
    
    sleeper_cost = 0
    ac_cost = 0
    for items in train_list:
        if  items["train_no"] == train_no:
            ac_cost = items["ac_fare"] * passenger_dict["ac"]
            sleeper_cost = items['sleeper_fare'] * passenger_dict["sleeper"]
    return ac_cost + sleeper_cost
       
print(get_train_name(25627))
print(get_trains_for_day("We"))
print(get_total_fare(25627,{"sleeper":10, "ac":10}))


