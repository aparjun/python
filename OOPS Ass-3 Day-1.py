#OOPR-Assgn-3
#Start writing your code here
class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = 0

    def purchases(self):
        self.bill_amount=self.bill_amount- self.bill_amount*2/100
        
    def pays_bill(self,amount):
        print(self.customer_name,"pays bill amount of Rs.",self.bill_amount)
s=Customer()
s.purchases()
s.pays_bill(500)
