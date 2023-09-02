# Las listas son estructutas de datos lineales
# Se crean usando brackets ej: my_list = []
# Las listas son ordenadas (orden de incercion), esto quiere decir qie el ultimo dato ingresado ocupara la ultima posicion
# Emplea métodos para manipular los items de la misma
# Como los arrays la primera posicion inicia en cero
# Permite items duplicados 
# Las listas son mutables, es decir podemos agregar, actualizar o remover items
# Puede contener distintos tipos de datos

materias = ["Matematica", "Español", "Ciencias", "Sociales", "Física", "Quimica"]

# Para determinar el tamaño de la lista podemos usar len()
#print(len(materias))

#print(dir(materias))

# Podemos acceder a los elementos indicando la posicion
print(materias[2])

#Slicing muestra las posiciones en un rango

print(materias[2:5])

print(materias[:5])

print(materias[-5:-1])

# Tipos de datos en las listas

edades = [17, 27, 42, 31, 56, 68]

print(type(edades))

# Actualizar un elemento de la lista 
materias[2] = "Biologia"

print(materias[0:])

materias[1:3] = "Lenguaje", "Ciencias Naturales"

print(materias[0:])

# Agregando elementos a la lista

materias.append("Religion")
print(materias[0:])

materias.insert(0, "Etica")
print(materias[0:])

#Quitar elementos a la lista

materias.pop(5)
print(materias[0:])

materias.remove("Etica")
print(materias[0:])

#del materias[4]
print(materias[0:])

materias.clear()
print(materias[0:])

#del materias[]
print(materias[0:1])

# Iterar las listas con el ciclo for

materias = ["Matemáticas", "Ciencias", "Historia", "Lenguaje"]

print("-" * 50)

for i in materias:
    print(i)

print("-" * 50)

for i, materia in enumerate(materias):
    print(i, materia)

print("-" * 50)

# Usando ciclo while
i= 0

while i < len(materias):
    print(i, materias[i])
    i += 1

print("-" * 50)

# List comprehension
[print(i) for i in materias]

#crear lista numero

     









