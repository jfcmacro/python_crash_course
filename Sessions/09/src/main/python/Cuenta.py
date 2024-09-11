class Cuenta:
    def __init__(self,nombre,saldo):
        self._nombre = nombre
        self._saldo = saldo
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,saldo):
        self._saldo = saldo
