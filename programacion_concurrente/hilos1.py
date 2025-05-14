import threading
import time
import random

def lavar_plato():
	print("Lavando plato")
	time.sleep(random.randint(1, 3))
	print("Plato listo")

def barrer_piso():
	print("Barrando piso")
	time.sleep(random.randint(1, 3))
	print("Piso listo")

def cocinar():
	print("Cocinando")
	time.sleep(random.randint(1, 3))
	print("Cocinado")

def main_thread():
	aux = 0

	for i in hilos:
		i.start()

	for i in hilos:
		i.join()

	while True:
		for i in hilos:
			if i.is_alive():
				continue
			else:
				aux+=1
		if aux == 3:
			print("Hilo principal terminado")
			break

hilo_principal = threading.Thread(target=main_thread)

hilos = []
hilos.append(threading.Thread(target=lavar_plato))
hilos.append(threading.Thread(target=barrer_piso))
hilos.append(threading.Thread(target=cocinar))

hilo_principal.start()
hilo_principal.join()
