import threading
import time
import random
import multiprocessing

lock = threading.Lock()

cajeros = [multiprocessing.Process(target=cajero_automatico) for _ in range(5)]
clientes = [threading.Thread(target=cliente) for _ in range(5)]

for cajero in cajeros:
	cajero.start()
for cajero in cajeros:
	cajero.join()

for cliente in clientes:
	cliente.start()
for _ in clientes:
	cliente.join()
