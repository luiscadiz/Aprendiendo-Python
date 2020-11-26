#La funcion str() sirve para covertir un numero a una cadena
#Graias a la funcion str podemos pasar un resultado entero a una funcion como una sola cadena
cateto_a = float (input("Ingresa la longitud del primer cateto: "))
cateto_b = float (input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2)**.5))
