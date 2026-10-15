"""
# calculate the position of an object at free fall, given an initial height
# y = y0 + (v0+t) + (1/2*g*t^2)
# y0 = altura inicial (metros).    altura_inicial
# v0 = velocidad inicial (metros/segundo)       velocidad_inicial (por defecto 0)
# g = acceleracion de la gravedad (por defecto 9.811 m/s2)      GRAVEDAD

resultado: 
    la altura actual en metros      altura_actual
"""
#inicializar constantes

GRAVEDAD = -9.81
VELOCIDAD_INICIAL = 0

#pedir datos iniciales (altura inicial, tiempo)

altura_inicial = float(input("Introduce la altura desde la que lo dejamos caer (cm)"))
tiempo = float(input("En que momento quieres saber la posicion (s)?"))

#convertimos la funccion a python
altura_inicial /= 100
altura_actual = altura_inicial + (VELOCIDAD_INICIAL * tiempo) + (0.5 * GRAVEDAD * (tiempo ** 2))

if altura_actual > 0:
    print(f"la altura en el segundo {tiempo} del objecto es {altura_actual}")
else: 
    print("el objecto esta en el sueloooo")
