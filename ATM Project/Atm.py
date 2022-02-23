class atm :
    def __init__(self,cardNumber,pinNumber) :
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = 50000

    def withdraw(self,withdrawAmt) :
        print("withdrawing :",withdrawAmt)
        self.balance = self.balance - withdrawAmt
        print("Your new amount is :",self.balance)
    def deposit(self,depositAmt) :
        print("depositing...",depositAmt)
        self.balance = self.balance + depositAmt
        print("Your new amount is :",self.balance)
    def balanceInquiry(self) :
        print("balance : ",self.balance)

cardNumber = input("Card number :")
pinNumber = input("Pin number :")
money = atm(cardNumber,pinNumber)
choice = input("Enter choice : 1. Cash withdrawal, 2. Cash deposit, 3. Balance Inquiry")
print(choice)
if(choice == "1" ) :
    amount = int(input("Enter the amount to withdraw :"))
    money.withdraw(amount)
elif(choice == "2" ) :
    amount = int(input("Enter the amount you want to deposit :"))
    money.deposit(amount)
elif(choice == "3" ) :
    money.balanceInquiry()
else :
    print("Enter a valid choice")


