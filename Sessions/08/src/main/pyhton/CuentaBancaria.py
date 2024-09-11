class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre, saldo):
        self.__dict__["numero_cuenta"] = numero_cuenta
        self.__dict__["nombre"] = nombre
        self.__dict__["saldo"] = saldo 


def visited_mark(lst):
    for e in lst:
        if e.numero_cuenta % 2 == 0:
            e.__dict__["visited"] = True
        else:
            e.__dict__["visited"] = False
