class Conta:
    def __init__(self, holder, number, balance):
        self._balance = 0
        self._account_number = number
        self._holder = holder
        
    @property
    def balance(self):
        return self._balance

    @Balance.setter
    def balance(self, balance):
        if(balance < 0):
            print("o saldo nao pode ser negativo")
        else:
            self._balance = balance