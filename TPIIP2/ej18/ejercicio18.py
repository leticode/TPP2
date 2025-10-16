'''18. Una cuenta bancaria administra una colección de transacciones. 
Los depósitos y retiros son tipos de transacciones que modifican el saldo de la cuenta. '''
from cuenta import Cuenta
from deposito import Deposito
from retiro import Retiro
from transaccion import Transaccion

cuenta = Cuenta("Lucia Bide", 50000)
cuenta.hacer_transaccion("deposito", 2000)
cuenta.hacer_transaccion("retiro", 4000)
cuenta.hacer_transaccion("retiro", 60000)

cuenta.transacciones_mostrar()