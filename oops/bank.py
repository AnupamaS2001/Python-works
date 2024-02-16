class bank:
    acc_no:int
    acc_type:str
    balance:int
    bank_name:str="sbi"  #static variable
    person_name: str
    ifsc_code:str

    def __init__(self,acc_no,acc_type,balance,person_name,ifsc_code):
        self.acc_no=acc_no
        self.acc_type=acc_type
        self.balance=balance
        self.person_name=person_name
        self.ifsc_code=ifsc_code

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance -= amount
            print(f"your {self.bank_name} account debited with amount {amount} available balance {self.balance}")
        else:
            print("transaction declined......")
    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} account credited with amount {amount} available balance {self.balance}")
    def balance_enq(self):
        print(f"your {bank.bank_name} account balance {self.balance}")



obj1=bank(467823,"savings",4900,"anu","abc001")
obj1.balance_enq() 
