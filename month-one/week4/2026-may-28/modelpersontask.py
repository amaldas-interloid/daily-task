class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

     
class contact(person):
    def __init__(self,name,age,phone,email):
        super().__init__(name,age)
        self.phone = phone
        self.email = email
    def update_contact(self,phone ,email):
        self.phone  = phone
        self.email = email
        
    def __str__(self):
        return ( f"Name: {self.name}, " f"Age: {self.age}, " f"Phone: {self.phone}, " f"Email: {self.email}" )
        
        
class customer(contact):
    def __init__( self, name, age, phone, email, customer_id, balance ):
        super().__init__(name, age, phone, email)
        self.customer_id = customer_id
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
    def __str__(self):
        return ( f"Customer ID: {self.customer_id}, " f"Name: {self.name}, " f"Age: {self.age}, " f"Phone: {self.phone}, " f"Email: {self.email}, " f"Balance: {self.balance}" )
        







p1 = person("Amaldas",22)
print(p1)

print(repr(p1))


c1 =contact("vikram",22,8778516709,"das171018@gmail.com")
print(c1)

cust1 = customer("naveen",22,8778516709,"naveen@123","c101",5000)
print(cust1)
cust1.deposit(2000)
cust1.withdraw(1000)
print(cust1.balance)




    


