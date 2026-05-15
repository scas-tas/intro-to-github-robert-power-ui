class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
    #Mainline
robert = Account("2622010", 1, "Robert")
hugo = Account("1", 67, "Pumpkin")
print(f"{robert.owner} has {robert.balance}.")
print(f"{hugo.owner} has {hugo.balance}.")
