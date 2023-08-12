"""Realizar un programa que realice el registro de una persona con name, email, password, captcha y telefono, las validaciones son: puede ingresar con mail o telefono y password y captcha(ej: 2+3*5), si pasa la validacion que aparezca Bienvenido + name, validar credenciales
"""

import re

# Función para generar un captcha
def generar_captcha():
    import random
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores)
    captcha = f"{num1} {operador} {num2}"
    resultado = eval(captcha)
    return captcha, resultado

# Función para registrar una persona
def registrar_persona():
    name = input("Ingrese su nombre: ")
    email = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    password = input("Ingrese su contraseña: ")

    captcha, resultado_esperado = generar_captcha()
    print(f"Resuelva el siguiente captcha: {captcha}")
    respuesta_captcha = float(input("Ingrese el resultado del captcha: "))
    
    if respuesta_captcha == resultado_esperado:
        print(f"Bienvenido, {name}! Registro exitoso.")
        return name, email, telefono, password
    else:
        print("Captcha incorrecto. Registro fallido.")
        return None, None, None, None

# Función para validar las credenciales
def validar_credenciales(name, email, telefono, password):
    print("Iniciar sesión:")
    login_email_telefono = input("Ingrese su correo electrónico o teléfono: ")
    login_password = input("Ingrese su contraseña: ")

    if (login_email_telefono == email or login_email_telefono == telefono) and login_password == password:
        print(f"Bienvenido, {name}! Sesión iniciada correctamente.")
    else:
        print("Credenciales incorrectas. Inicio de sesión fallido.")

# Main
def main():
    name, email, telefono, password = registrar_persona()
    if name and email and telefono and password:
        validar_credenciales(name, email, telefono, password)

if __name__ == "__main__":
    main()
