#CREAR UN PROGRAMA QUE PRIMERO LE IDA AL USUARIO QUE INGRESE UN TEXTO
#LUEGO EL PROGRAMA LE PEDIRA QUE INGRESE 3 LETRAS A SU ELECCION
#LUEGO EL PROGRAMA LE DIRA CUANTAS VECES APARECE CADA LETRA QUE ELIGIO
#LE DIRA AL USUARIO CUANTAS PALABRAS HAY A LO LARGO DE TODO EL TEXTO
#NOS VA A DECIR CUAL ES LA PRIMERA LETRA DEL TEXTO Y LA ULTIMA
# EL SISTEMA NOS VA A MOSTRAR COMO QUEDARIA EL TEXTO SI INVIRTIERAMOS EL ORDEN DE LAS PALABRAS
#EL SISTEMA NOS VA A DECIR SI LA PALBRA PYTHON SE ENCUENTRA DENTRO DEL TEXTO

texto = input("Ingrese un texto: ")
letra1= input("Ingrese una letra: ")
letra2= input("Ingrese una segunda letra: ")
letra3= input("Ingrese una tercera letra: ")

#contador para saber cuantas letras elegidas se repiten
contador_letras = texto.count(letra1)
contador_letras2 = texto.count(letra2)
contador_letras3 = texto.count(letra3)

print(f"Número de veces que la letra {letra1} se repite en el texto:", contador_letras)
print(f"Número de veces que la letra {letra2} se repite en el texto:", contador_letras2)
print(f"Número de veces que la letra {letra3} se repite en el texto:", contador_letras3)

#contador para saber cuantas palabras tiene el texto
palabras =texto.split()
contador_palabras =len(palabras)
print(f" El texto tiene {contador_palabras} palabras")

#Saber cual es la primera letra del texto y la ultima

primera_letra = texto[0]
segunda_letra = texto[-1]
print(f"La primera letra del texto es {primera_letra} y la ultima {segunda_letra}")

#COMO ES EL TEXTO SI INVERTIMOS LAS PALABRAS

texto_invertido= texto[::-1]
print(f"El texto con las palabras invertidas quedaria asi: {texto_invertido}")

print("python" in texto)

