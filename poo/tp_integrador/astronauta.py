from persona import Persona
from mision import Mision

class Astronauta(Persona):
	def __init__(self, dni, nombre, nacionalidad):
		super().__init__(dni, nombre, nacionalidad)
		self.misiones = []
		# misiones = [{nombre de la mision, destino, duracion, resultado}, ...]

	def agregar_mision(self, dict_mision):
		mision = Mision(dict_mision)
		self.misiones.append(mision)

	def emitir_informe(self):
		archivo = f"informe-astronauta-{self.nombre}.txt"
		super().emitir_informe(archivo)
		with open(archivo, "a", encoding="utf-8") as f:
			f.write(f"El nombre de la persona es {self.nombre}\n")
			f.write(f"El dni de la persona es {self.dni}\n")
			f.write(f"La nacionalidad de la persona es {self.nacionalidad}\n")
			f.write(f"Las misiones que ha realizado el astronauta son:\n")
			for mision in self.misiones:
				f.write(f"{mision.nombre} {mision.destino} {mision.duracion} {mision.resultado} {mision.evaluacion}\n")
		return archivo

