from astronauta import Astronauta

class Director:
	def __init__(self):
		self.evaluaciones = []
	
	def asignar_mision(self, astronauta):
		try:
			nombre_mision = input("Ingrese el nombre de la mision: ")
			destino = input("Ingrese el destino: ")
			duracion = int(input("Ingrese la duracion (en dias): "))
			if duracion<1:
				raise ValueError
			resultado = input("Ingrese el resultado: ")
		
			dict_mision = {"nombre": nombre_mision, "destino": destino, "duracion": duracion, "resultado": resultado}
			astronauta.agregar_mision(dict_mision)
		except ValueError:
			print("La duracion no puede ser menor a 1")
			print("No se pudo agregar la mision\n")
		except:
			print("No se pudo agregar la mision\n")
	
	def evaluar_mision(self, astronauta, mision):
		nombre_mision = input("Ingrese el nombre de la mision: ")
		evaluacion = input("Ingrese la evaluacion: ")
		try:
			mision.set_evaluacion(evaluacion)
			self.evaluaciones.append(mision.nombre, evaluacion)
		except:
			print("No se pudo evaluar la mision")
