#PF-Assgn-61
def validate_name(name):
    if(name=="" or len(name)>15 or (not name.isalpha())):
        return False
    else:
        return True

def validate_phone_no(phno):
    c=phno.count(phno[0])
    if(len(phno)!=10 or (not name.isdigit()) or c==len(phno)):
        return False
    else:
        return True

def validate_email_id(email_id):
    if(email_id.count("@")!=1 or email_id.count(".com")!=1 or (not email_id.endswith("@gmail.com") and not email_id.endswith("@gmail.com") and not email_id.endswith("@gmail.com"))):
        return False
    else:
        return True

def validate_all(name,phone_no,email_id):
    if(not validate_name(name)):
        print("Invalid Name")
    if(not validate_phone_no(phone_no)):
        print("Invalid phone number")
    if(not validate_email_id(email_id)):
        print("Invalid email id")
    if(validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id)):
        print("All the details are valid")
        
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")
