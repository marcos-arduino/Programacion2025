from astronauta import Astronauta
from director import Director
from mision import Mision
from ingeniero import Ingeniero


if __name__ == "__main__":
	director = Director()
	ingeniero = Ingeniero("12345678", "Lucas", "Mexicano")
	astronauta = Astronauta("12345678", "Ochoa", "Mexicano")
	astronauta2 = Astronauta("47347934", "Marcos", "Argentino")

	director.asignar_mision(astronauta)
	ingeniero.registrar_sistema("Motor", "Funcionando")

	archivo_ingeniero = ingeniero.emitir_informe()
	with open(archivo_ingeniero, "r", encoding="utf-8") as f:
		print(f.read())

	archivo_astronauta2 = astronauta2.emitir_informe()
	with open(archivo_astronauta2, "r", encoding="utf-8") as f:
		print(f.read())

	archivo_astronauta = astronauta.emitir_informe()
	with open(archivo_astronauta, "r", encoding="utf-8") as f:
		print(f.read())
	
