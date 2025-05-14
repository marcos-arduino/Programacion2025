import multiprocessing
import os
import time

def proceso_hijo():
	print(f"Proceso hijo: PID = {os.getpid()}, Padre = {os.getppid()}")
	time.sleep(2)
	print(f"Proceso hijo terminado")

if __name__ == "__main__":
	procesos = [multiprocessing.Process(target=proceso_hijo) for _ in range(3)]
	for _ in procesos:
		_.start()
	for _ in procesos:
		_.join()
	time.sleep(2)
	print(f"Procesos terminados")
