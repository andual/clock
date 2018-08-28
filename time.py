import time
import random

print("responde lo mas rapido posible")

while True:
	inicio=time.time()
	numazar=random.randint(1,5)
	respuesta=int(input("cuanto es 2x "+str(numazar)+"?"))
	multi=2*numazar
	final=time.time()
	tiempo=round(final-inicio,0)
	if respuesta==multi:
		print("Felicidades resultado correcto")
		if tiempo<5:
			print ("el tiempo fue menor de 5: "+ str(tiempo))
			break
		elif tiempo>=5:
			print ("el tiempo fue mayor de 5: "+ str(tiempo))
			break
	else:
		print("suerte la proxima")
		break




	