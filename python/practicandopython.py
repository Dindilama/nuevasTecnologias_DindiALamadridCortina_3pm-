height = 200

age = 10

if height < 150 or age >= 17:
    print("Puede ingresar")

#comentarios de una linea
"""Comentario multilinea"""

#Estructura de control IF - ELSE, INGRESAR DATOS POR CONSOLA EN  PYTHON: con input
"""pay = input("Valor a pagar")

print(type(pay))"""

#como hago un parseo para que el valor no sea string si no entero y despues pasarlo a string otra vez:

"""pay = int(input("Valor a pagar"))

print(type(pay))

print("El valor recibido fue de " + str(pay) )"""

"""Hacer un programa que pregunte: ¿desea hacer su pago? si dice que si, que pregunte si desea agregar el servicio, si dice que si, se le agrega el 10% al valor total y le dice muchas gracias, si dice que no que pregunte si desea hacer otro servicio, si dice que no que le diga muchas gracias con if-else"""

def main():
    print("Bienvenido al sistema de pagos")
    respuesta_pago = input("¿Desea hacer su pago? (si/no): ")

    if respuesta_pago.lower() == "si":
        respuesta_servicio = input("¿Desea agregar el servicio? (si/no): ")

        if respuesta_servicio.lower() == "si":
            valor_total = calcular_valor_con_servicio()
            print("Se ha agregado el servicio.")
        else:
            valor_total = calcular_valor_sin_servicio()
            print("No se ha agregado el servicio.")

        print(f"El valor total a pagar es: ${valor_total:.2f}")
        print("¡Muchas gracias!")

    else:
        respuesta_otro_servicio = input("¿Desea hacer otro servicio? (si/no): ")

        if respuesta_otro_servicio.lower() == "si":
            print("Vuelva cuando esté listo para hacer un pago.")
        else:
            print("¡Muchas gracias por su visita!")

def calcular_valor_con_servicio():
    valor_base = float(input("Ingrese el valor base: "))
    valor_total = valor_base * 1.10
    return valor_total

def calcular_valor_sin_servicio():
    valor_base = float(input("Ingrese el valor base: "))
    return valor_base

if __name__ == "__main__":
    main()
