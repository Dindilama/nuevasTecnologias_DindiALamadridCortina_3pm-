#generar fucionalidad que tome una compra y pregunte: cual es el valor de la compra?, tambien que pregunte numero de cuotas teniendo esos dos datos que arroje un estado de cuenta que muestre el numero de cuotas que ha pagado, el saldo con el valor abonado y las que le hacen falta por pagar y el cupo liberado, con un ciclo while.

def calcular_estado_de_cuenta():
    valor_compra = float(input("Ingrese el valor de la compra: "))
    numero_cuotas = int(input("Ingrese el número de cuotas: "))
    
    saldo_restante = valor_compra
    cuotas_pagadas = 0
    
    while cuotas_pagadas < numero_cuotas:
        valor_cuota = saldo_restante / numero_cuotas
        cuotas_pagadas += 1
        saldo_restante -= valor_cuota
        cupo_liberado = valor_compra - saldo_restante
        
        print(f"\nEstado de cuenta después de {cuotas_pagadas} cuota(s):")
        print(f"Cuotas pagadas: {cuotas_pagadas}")
        print(f"Saldo restante: {saldo_restante:.2f}")
        print(f"Cuotas pendientes por pagar: {numero_cuotas - cuotas_pagadas}")
        print(f"Cupo liberado: {cupo_liberado:.2f}")
        
        if cuotas_pagadas < numero_cuotas:
            respuesta = input("\n¿Desea pagar otra cuota? (s/n): ")
            if respuesta.lower() != "s":
                break

    print("\nGracias por utilizar nuestro servicio.")

calcular_estado_de_cuenta()


