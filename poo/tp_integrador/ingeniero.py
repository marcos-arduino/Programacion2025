from persona import Persona

class Ingeniero(Persona):
	def __init__(self, dni, nombre, nacionalidad):
		super().__init__(dni, nombre, nacionalidad)
		self.sistemas = []

	def registrar_sistema(self, sistema, estado):
		self.sistemas.append((sistema, estado))

	def emitir_informe(self):
		archivo = f"informe-ingeniero-{self.nombre}.txt"
		super().emitir_informe(archivo)
		with open(archivo, "a", encoding="utf-8") as f:
			f.write(f"El nombre de la persona es {self.nombre}\n")
			f.write(f"El dni de la persona es {self.dni}\n")
			f.write(f"La nacionalidad de la persona es {self.nacionalidad}\n")
			f.write(f"Los sistemas que ha utilizado el ingeniero son:\n")
			for sistema in self.sistemas:
				f.write(f"{sistema[0]} {sistema[1]}\n")
		return archivo
