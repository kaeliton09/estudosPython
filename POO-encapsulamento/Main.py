class Main:
    pass

print("testeando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("kaka", "6299933-7799")
conta = Conta(c1.name, 1000, 0)

print(conta.holder, " numero: ", conta.account_number, " seu saldo: ", conta.balance)