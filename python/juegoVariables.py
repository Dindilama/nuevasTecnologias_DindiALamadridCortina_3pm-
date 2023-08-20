# hacer juego que arroje numeros al azar y que incremente o decremente segun estas dos variables 
import random

vidas = 5;

puntos = 0;

while vidas != 0:

    num = random.randint(0, 9)

#sintaxis de while en python:

    if num == 0:
        vidas -=1
        print(f"Te quedan{vidas} vidas")
    else:
        puntos +=1
        print(f"Has ganado {puntos} puntos")

