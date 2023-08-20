#generar en este caso con un while crear un menu (en menu utilizar un switch) que arroje 3 opciones: 1. registro, 2. login, 3. salir, en caso de que elija la opcion 2, cuando se loguee que muestre otro menu con las opciones 1. tarjeta de credito, 2.Juego, 3. Volver. 

import random

usuarios = {}

def main_menu():
    print("===== Menú Principal =====")
    print("1. Registro")
    print("2. Login")
    print("3. Salir")

def login_menu():
    print("===== Menú de Juego =====")
    print("1. Jugar")
    print("2. Volver")

def registro():
    nombre = input("Ingrese su nombre: ")
    usuarios[nombre] = {"vida": 100, "puntaje": 0}
    print(f"Registro exitoso para {nombre}.")

def login():
    nombre = input("Ingrese su nombre: ")
    if nombre in usuarios:
        print(f"Bienvenido, {nombre}!")
        return nombre
    else:
        print("Usuario no encontrado.")
        return None

def jugar(nombre):
    print("¡Comienza el juego!")
    while True:
        numero_random = random.randint(-10, 10)
        print(f"Número generado al azar: {numero_random}")
        accion = input("¿Quieres sumar (+) o restar (-) este número a tu vida? (q para salir): ")

        if accion == 'q':
            break
        elif accion == '+' or accion == '-':
            usuarios[nombre]["vida"] += numero_random if accion == '+' else -numero_random
            usuarios[nombre]["puntaje"] += abs(numero_random)
            print(f"Vida actual: {usuarios[nombre]['vida']}")
        else:
            print("Acción no válida. Ingresa '+' para sumar o '-' para restar.")

# Programa principal
while True:
    main_menu()
    opcion_main = input("Elige una opción: ")

    if opcion_main == '1':
        registro()
    elif opcion_main == '2':
        nombre_logueado = login()
        if nombre_logueado:
            while True:
                login_menu()
                opcion_login = input("Elige una opción: ")

                if opcion_login == '1':
                    jugar(nombre_logueado)
                elif opcion_login == '2':
                    break
                else:
                    print("Opción no válida. Introduce una opción válida.")
    elif opcion_main == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Introduce una opción válida.")
