class Mision:

	def __init__(self, dict_mision):
		self.nombre = dict_mision["nombre"]
		self.destino = dict_mision["destino"]
		self.duracion = dict_mision["duracion"]
		self.resultado = dict_mision["resultado"]
		self.evaluacion = "Pendiente"

	def set_evaluacion(self, evaluacion):
		self.evaluacion = evaluacion
