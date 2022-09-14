class BankAccount: 
	def __init__(self, int_rate, balance=0):
		self.balance = balance
		self.int_rate = int_rate

	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
		else:
			print("Insufficient funds: Charging a $5 fee")
			self.balance -= 5
		return self

	def display_account_info(self):
		print("Balance: $" + str(self.balance))
		return self 

	def yield_interest(self):
		if self.balance > 0:
			self.balance *= 1 + self.int_rate
		return self


Baraa = BankAccount(0.02, 7000)
Bayan = BankAccount(0.03, 2300)
Afnan = BankAccount(0.02, -100)

Baraa.deposit(200).deposit(100).deposit(100).withdraw(1000).yield_interest().display_account_info()
Bayan.deposit(3400).deposit(1000).withdraw(200).withdraw(100).withdraw(200).withdraw(700).yield_interest().display_account_info()