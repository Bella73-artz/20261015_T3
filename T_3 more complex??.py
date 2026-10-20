"""
# calculate the position of an object in projectile motion
# tiempo - given 
# v0 = velocidad inicial (metros/segundo) - given    velocidad_inicial)
# g = acceleracion de la gravedad (por defecto 9.811 m/s2)      GRAVEDAD
# angulo >90, - given

resultado: 
    la posicion actual en metros      posicion_actual
"""
#inicializar constantes

GRAVEDADES = {
    "Tierra": -9.81,
    "Marte": -3.7, 
    "Luna": -1.62, 
    "Jupiter": -24.79, 
    "Sol": -274
    }
UBICACION_POR_DEFECTO = "Tierra"
VELOCIDAD_INICIAL = 0

#pedir datos iniciales (altura inicial, tiempo)

tiempo = float(input("En que momento quieres saber la posicion (s)?"))
angulo = float(input("A que angulo tiras el objeto? (menor de 90)"))
velocidad_inicial = float(input("Que es la velocidad inicial? (metros por segundo)"))
ubicacion = (input("En que planeta estas? (Tierra, Marte, Luna, Jupiter, Sol)"))

#vaidamos que la ubicacion sea valida
if ubicacion in GRAVEDADES:
    #tenemos esta ubicacion
    GRAVEDAD = GRAVEDADES[ubicacion]
else: 
    print("donde vas? estas en la tierra stupid")
    GRAVEDAD = GRAVEDADES[UBICACION_POR_DEFECTO]

#convertimos la funccion a python

import math
angle_radians = math.radians(angulo)

velocidad_horizontal = float((velocidad_inicial * math.cos(angle_radians)))
velocidad_vertical = float((velocidad_inicial * math.sin(angle_radians)))

posicion_horizontal = float((velocidad_horizontal * tiempo))
posicion_vertical = float((velocidad_vertical + (0.5 * GRAVEDAD * tiempo ** 2)))


if posicion_vertical > 0:
    print(f"El vector de posicion del objecto es ({posicion_horizontal}x {posicion_vertical}y), en el segundo {tiempo}")
else: 
    print("el objecto esta en el sueloooo")
