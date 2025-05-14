class Persona:
	def __init__(self, dni, nombre, nacionalidad):
		self.dni = dni
		self.nombre = nombre
		self.nacionalidad = nacionalidad

	def emitir_informe(self, archivo):
		with open(archivo, "w", encoding="utf-8") as f:
			f.write("")
		pass
