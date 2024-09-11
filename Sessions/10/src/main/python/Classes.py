
# class A: # --> object
#     def m(self):
#         print("method A.m()")
        
# class B: # --> object
#     def m(self):
#         print("method B.m()")


# class C(B,A):
#     def m2(self):
#         m() # Se invoca de cual de las super class el correspodiente


# # abstract 
# class Animal:
#     def __init__(self):
#         print("Constructor de Animal")

# # abstract
# class Mamiferos(Animal):
#     def __init__(self):
#         super.__init__()
#         print("Constructor de Mamiferos"); printf("Segunda linea")
from abc import ABCMeta,abstractmethod

class Closeable:
    @abstractmethod
    def close(): pass

# Duck Type System

class Cuenta(metaclass=ABCMeta):
    def __init__(self, saldo):
        self._saldo = saldo

    @abstractmethod
    def retiro(self, monto):
        pass
    @abstractmethod
    def consignacion(self, monto):
        pass
    @property
    def saldo(self):
        return saldo

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, interes):
        super().__init__(saldo)
        self._interes = interes
    def retiro(self, monto):
        if (self._saldo >= monto):
            self._saldo -= monto
    def consignacion(self, monto):
        self._saldo += monto


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, sobregiro):
        super().__init__(saldo)
        self._sobregiro = sobregiro
    def retiro(self, monto):
        if ((self._saldo + self._sobregiro) >= monto):
            self._saldo -= monto
    def consignacion(self, monto):
        self._saldo += monto
    
