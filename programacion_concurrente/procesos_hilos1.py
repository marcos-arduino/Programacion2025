import threading
import time
import random

lock = threading.Lock()

class ImpresoraCompartida:
	def imprimir(self):
		while True:
			if not lock.locked():
				lock.acquire()
				print("Imprimiendo")
				if random.randint(0, 10)>5:
					print("Error")
					lock.release()
					raise Exception("Error")
				time.sleep(random.randint(1, 7))
				lock.release()
				print("Listo")
				break
			else:
				print("Esperando")
				time.sleep(random.randint(1, 3))

def main_thread():
	aux = 0

	for i in usuarios:
		try:
			i.start()
		except Exception as e:
			print(e)

	for i in usuarios:
		i.join()

	while True:
		for i in usuarios:
			if i.is_alive():
				continue
			else:
				aux+=1
		if aux == 5:
			print("Hilo principal terminado")
			break

usuarios = [threading.Thread(target=ImpresoraCompartida().imprimir) for i in range(5)]
hilo_principal = threading.Thread(target=main_thread)
hilo_principal.start()
hilo_principal.join()

