import threading
import time
import random


saldo = 100

def cajero_automatico():
	with threading.Lock():
		global saldo
		if saldo>0:
			saldo -= 50
			print("retiro exitoso")
		else:
			print("fondos insuficientes")

hilos = [threading.Thread(target=cajero_automatico) for i in range(3)]

for i in hilos:
	i.start()

for i in hilos:
	i.join()
		
print(saldo)


