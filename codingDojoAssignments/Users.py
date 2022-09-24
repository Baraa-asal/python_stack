from bankAccount import BankAccount

class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0,0)   #we instantiated an object of type bank account in account property, important
    def make_deposit(self, amount):	
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print("User:", self.name,"balance:",self.account.balance)
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)
    

        
bara = User("Bara","bara@gmail.com") 
bara.make_deposit(150)
bara.display_user_balance()

maryam = User("Maryam","maryam@gmail.com")
aseel = User("aseel","maryam@gmail.com")
osaid = User("osaid","maryam@gmail.com")

maryam.make_deposit(1000)
maryam.make_deposit(1000)
maryam.make_deposit(1000)
maryam.make_withdrawal(1500)
maryam.display_user_balance()   

aseel.make_deposit(1200)
aseel.make_deposit(1700)
aseel.make_withdrawal(500)
aseel.make_withdrawal(1000)
aseel.display_user_balance()

osaid.make_deposit(3000)
osaid.make_withdrawal(400)
osaid.make_withdrawal(700)
osaid.make_withdrawal(500)
osaid.display_user_balance()

maryam.transfer_money(osaid,500) 
osaid.display_user_balance()