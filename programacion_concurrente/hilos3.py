import random
import threading
import time
import queue

cola = queue.Queue()

def productor():
	for _ in range(10):
		cola.put(random.randint(1, 5))

def consumidor():
	while not cola.empty():
		print(cola.get())
		time.sleep(0.5)
	

hilo_productor = threading.Thread(target=productor)
hilo_consumidor = threading.Thread(target=consumidor)

hilo_productor.start()
hilo_consumidor.start()
hilo_productor.join()
hilo_consumidor.join()

print("Fabrica terminada")
