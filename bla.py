class Bank:
    def __init__(self, Bank_bal,Passcode):
        self.Bank_bal = Bank_bal 
        self.Passcode = Passcode

    def deposite(self, value):
        self.Bank_bal +=value
        print(f"Your Balance = {self.Bank_bal}")
    
    def view(self):
        print(f"Your Balance = {self.Bank_bal}")

    def Withdraw(self, value):
        if(self.Bank_bal<value):
            print("Not Enough Money")
            return
        self.Bank_bal -=value
        print(f"Your Balance = {self.Bank_bal}")


class Person(Bank):
    def __init__(self,Name , Age, Bank_paisaa, Passcode):
        Bank.__init__(self,Bank_paisaa,Passcode)
        self.Name = Name
        self.Age = Age


p1= Person("Khushi",20,7000000000,12345678)
# print(f"{p1.Name} {p1.Age} {p1.Bank_bal} {p1.Passcode}")

while True:
    print("Enter 1 to View , 2 to deposite , 3 to withdraw , any other value to quit :")
    a=int(input("enter your Choice :"))
    if(a>=1 and a<=3):
        passcode = int(input("Enter Your passcode:"))
        if(passcode==p1.Passcode):
            match a:
                case 1:
                    p1.view()
                case 2 :
                    value = int(input("enter amount to deposite:"))
                    p1.deposite(value)
                case 3 :
                    value = int(input("enter amount to withdraw:"))
                    p1.Withdraw(value)
        else:
            print("You Can't enter. So, GET OUT!!")
    
    else:
        print("Never Come Again")
        break