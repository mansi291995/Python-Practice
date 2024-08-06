#enacapsuation hidding the data
#binding data
class Bank:
    def __init__(self,bal):
        self.__bal=bal
    def credit(self,amount):
        self.__bal+=amount
        print("your balance is",self.check_bal())
    def debit(self,amount):
        self.__bal-=amount
        print("your balance is",self.check_bal())
    def check_bal(self):
       return self.__bal

acc=Bank(10000)
acc.credit(1000)
acc.debit(1000)
