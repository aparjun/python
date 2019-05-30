#OOPR-Assgn-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        self.__vehicle_type=None
        self.__vehicle_cost=0
        self.__vehicle_id=0
        self.__premium_amount=0
        
    def get_premium_amount(self):
        return self.__premium_amount
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
        
    def get_vehicle_type(self):
        return self.__vehicle_type    
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost    
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def get_vehicle_id(self):
        return self.__vehicle_id    
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    
    def calculate_premium(self):
        if(self.__vehicle_type=="TwoWheeler"):
            self.__premium_amount=self.__vehicle_cost*2/100
            return self.__premium_amount
        elif(self.__vehicle_type=="FourWheeler"):
            self.__premium_amount=self.__vehicle_cost*6/100
            return self.__premium_amount
        else:
            print("vehicle type is invalid")
    
    def display_vehicle_details(self):
        print("Vehicle ID:",self.__vehicle_id)
        print("Vehicle Cost:",self.__vehicle_cost)
        print("Vehicle Type:",self.__vehicle_type)
        print("Premium Amount:",self.__premium_amount)
    

Car=Vehicle()
Car.set_vehicle_type("TwoWheeler")
Car.set_premium_amount(1000)
Car.set_vehicle_cost(50000)
Car.calculate_premium()
Car.set_vehicle_id(111)
Car.display_vehicle_details()
            
