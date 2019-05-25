#PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        s=i[2:len(i)]
        if(i[0]=="D"):
            net_amount+=int(s)
        else:
            net_amount-=int(s)
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))
