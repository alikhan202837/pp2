class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, in_):
        self.in_ = in_
        self.balance += in_
        print(self.balance)

    def withdraw(self, out_):
        self.out_ = out_
        if(self.balance >= self.out_):
            self.balance -= out_
            print(self.balance)
        else:
            print(f"{self.owner}, your balance less than withdraw")
    def get_info(self):
        print(f"Owner name: {self.owner}, balance: {self.balance}")
name = input("Enter your name: ")

x = BankAccount(name)

x.deposit(1200)
x.withdraw(1201)

x.deposit(1000)
x.deposit(700)
x.withdraw(1200)

x.get_info()


