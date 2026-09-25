class Bank() :
    def __init__(self,customer_id,account_number, IFSC_code, minimum_balance):
        self.customer_id = customer_id
        self.account_number = account_number
        self.IFSC_code = IFSC_code
        self.minimum_balance= minimum_balance
    def display(self):
        print("Customer ID:", self.customer_id)
        print("Account Number:", self.account_number)
        print("IFSC code:", self.IFSC_code)
        print("Minimum balance:", self.minimum_balance)
cus1 = Bank(101, 123456, "SBIN0001234", 1000)
cus2 = Bank(102, 234567, "SBIN0005678", 2000)

print("Customer 1 details:")
cus1.display()
print("Implemented concepts: Encapsulation, Abstraction, Inheritance, Polymorphism")