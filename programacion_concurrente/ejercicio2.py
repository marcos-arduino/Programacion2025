import multiprocessing
import os
import time
import random

# Simular mediante un programa en Python el ciclo de vida de tres procesos
# hijos, representando los siguientes estados: Nuevo → Listo → En ejecución →
# Bloqueado → Listo → Terminado. Cada proceso debe mostrar en consola su
# transición por los estados utilizando print() y simular el tiempo de ejecución de cada
# estado usando time.sleep() con duraciones aleatorias.

def proceso_hijo(event):
	print(f"Nuevo {os.getpid()}")
	time.sleep(random.randint(1, 5))
	print(f"Listo {os.getpid()}")
	time.sleep(random.randint(1, 5))
	print(f"En ejecución {os.getpid()}")
	time.sleep(random.randint(1, 5))
	print(f"Bloqueado {os.getpid()}")
	event.wait()
	time.sleep(random.randint(1, 5))
	event.set()
	print(f"Listo {os.getpid()}")
	time.sleep(random.randint(1, 5))
	print(f"Terminado {os.getpid()}")

if __name__ == "__main__":
	q = multiprocessing.Queue()
	event = multiprocessing.Event()
	p = [multiprocessing.Process(target=proceso_hijo, args=(event,)) for _ in range(3)]

	for _ in p:
		_.start()

	for _ in p:
		_.join()
