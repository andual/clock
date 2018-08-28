import time
import random

print("responde lo mas rapido posible")
jugar=True
while jugar=True:
	inicio=time.time()
	numazar.random.randint(1,5)
	repuesta=int(input("cuanto es 2x "+str(numazar)+"?"))
	final=time.time()
	tiempo=round(fina-inincio,0)
	if respuesta==numazar:
		print("Felicidades resultado correcto", end="")
		if time<4:
			print ("el tiempo fue menor de 4: "+ tiempo)
			break
		if time=>4:
			print ("el tiempo fue mayor de 4: "+ tiempo)
			break
	else:
		print("suerte la proxima")




	