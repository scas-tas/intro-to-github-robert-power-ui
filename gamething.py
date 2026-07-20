class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
def deposit(self):
    accountinput = int(input("What is your account number?"))
    deposit = int(input("How much would you like to deposit into your account?"))
    self.balance = self.balance + deposit
    return(f"{person.owner} now has ${person.balance} in their bank account.")
    #Mainline
Robert = Account("1", 1, "Robert")
Hugo = Account("2", 67, "Hugo")
for person in (Robert, Hugo):
    print(f"{person.owner} has {person.balance}.")
persontalking = input("Who are you?").title()
decision = input(f"What would you like to do, {persontalking}?")
print(deposit(persontalking))
