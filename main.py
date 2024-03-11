nombre = "joan"
edad = 25
medicion = 10.5
print(type(nombre))
print(type(edad))
print(type(medicion))

#todo lo que tiene comillas es str 
#todo lo que no tiene comilla y no son decimales es int
#todo lo que no tiene comillas y no son numeros enteros es float
#str = letras
#int = numero
#float = decimal



#como pasarle cosas a la consola y que te las devuelva con un imput
#con un int(input()) para poner numeros y lo detecte como int
print("Cual es tu nombre?")
nombre = input()
nombre2 = int(input())
print("tu nombre es")
print("nombre")

print("y el estilo es")
print(type(nombre))

#para mostrar tu nombre es y aparece alado de eso
print("su nombre es", nombre)

#casting = para cambiar distinto numero 
#parsing para cambiar cualquier tipo de str a int o float
#f = formato
#para poner el codigo mas correcto que salga por ejemplo tu nombre es joan alado no abajo
print(f"tu nombre es {nombre}") 
#f-string : f"hola {nombre}"
#siempre se ocupan en un split
#.uper(): "HOLA"(mayuscula)
#.lower(): "hola"(minuscula)
#.split(): [tu, edad, es, 17]

#print(mensaje.lower("").split(""))



listadecompras = ["leche", "huevos", "jamon"]
print(listadecompras)

#agregar el pan
listadecompras.append("pan")
print(listadecompras)

#eliminar el pan, tambien se puede con el orden del numero [0, 1, 2, 3] 
listadecompras.pop()
print(listadecompras)

#quito el jamon
listadecompras.remove("jamon")
print(listadecompras)

#borrar lista completa
listadecompras.clear()

#agrego entremedio 
listadecompras.insert(1, "huevos")
print(listadecompras)

lista = {"pan", "huevo", "jamon"}
print(lista)
#cambiar por el pan y se añade bebida
lista[0] = "bebidas"
print(lista)


#para cambiar de lista a tuple (class list la cambio a tuple)
lista = ["leche", "jamon", "pan"]
print(lista)
print(type(lista))

lista = tuple(lista)
print(lista)
print(type(lista))






#iterable = algo"recorrible"
#listas = [elementos, elementos]
#tuplas = no se puede modificar una lista 