print()
print("     bankomati  ")
print("dziritadi operaciebi : ")
print("1 - tanxis shetana")
print("2 - tanxis gamotana")
print("3 - balansis shemowmeba")
print()


class BankAccount:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return f"balansia {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return "OPERACIA WARMATEBIT DASRULDA. axali balansia: " + str(self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return "OPERACIA WARMATEBIT DASRULDA. axali balansia:" + str(self.balance)
        else:
            return "Sakmarisi tanxa ar aris angarishze!"


user_account = BankAccount()


while True:
    choice = int(input("airchiet sasurveli operacia - "))

    if choice == 1:
        print(user_account.check_balance())
        shesatani_tanxa = float(input("shesatani tanxa - "))
        saboloo_tanxa =  0 + shesatani_tanxa     
        print(f"BALANSI GANAXLDA. axali balansi = {saboloo_tanxa} lari.")
        break
    elif choice == 2:
        amount = float(input("gamosatani tanxa - "))
        if amount > 0:
            print("angarishze ar gaqvt sakmarisi tanxa!")
        elif amount + 0:
            print(f"BALANSI GANAXLDA. axali balansi = {user_account.deposit(amount)} lari.")
        break
    elif choice == 3:
        amount = float(input("Dasrulebuli tanxa - "))
        print(f"BALANSI GANAXLDA. axali balansi = {user_account.withdraw(amount)} lari.") 
        break  


    with open('bankomati.txt', 'r+') as file:
        a = file.read()     
        print(a)  