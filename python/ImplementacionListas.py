# Hacer ejercicio que guarde una lista de ingresos  y que guarde en otra lista los egresos y que al final haga una especie de balance en donde diga la lista de ingresos y egresos y que diga saldos insuficientes o el saldo que tenga en la cuenta         


def main():
    ingresos = []
    egresos = []
    balance = 0
    
    while True:
        print("1. Registrar ingreso")
        print("2. Registrar egreso")
        print("3. Mostrar balance")
        print("4. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            ingreso = float(input("Ingrese el monto del ingreso: "))
            ingresos.append(ingreso)
            balance += ingreso
            print("Ingreso registrado.")
        elif opcion == 2:
            egreso = float(input("Ingrese el monto del egreso: "))
            egresos.append(egreso)
            balance -= egreso
            print("Egreso registrado.")
        elif opcion == 3:
            print("Ingresos:")
            for i, ingreso in enumerate(ingresos, start=1):
                print(f"{i}. {ingreso}")
                
            print("Egresos:")
            for i, egreso in enumerate(egresos, start=1):
                print(f"{i}. {egreso}")
                
            print(f"Balance actual: {balance}")
            if balance < 0:
                print("Saldo insuficiente.")
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
