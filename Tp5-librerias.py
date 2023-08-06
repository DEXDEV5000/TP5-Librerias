"""Ejercicio 1"""
#Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3)
"""def redondear(numero):
    entero = int(numero)
    decimal = numero - entero
    if decimal >= 0.5:
        return entero + 1
    else:
        return entero"""
""""Ejercicio 2"""
#Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado
# main_module.py
# main_module.py
#from mi_paquete.redondeo_module import redondear
#def suma_redondeada(a, b):
#    suma = a + b
#    return redondear(suma)
"""Ejercicio 3"""
#Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema.
#import datetime
#fecha_hora_actual = datetime.datetime.now()
#formato_fecha_hora = fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S")
#print("La fecha y hora actual del sistema es:", formato_fecha_hora)
"""Ejercicio 4"""
#Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito)
"""import random
def generar_numero_par():
    return random.randrange(2, 11, 2)
numeros_generados = set()
while True:
    numero_par = generar_numero_par()
    print("Número par generado:", numero_par)
    numeros_generados.add(numero_par)
    if len(numeros_generados) == 5:
        break"""
"""Ejercicio 5"""
#Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola m
#import random
#def bola_magica():
#    respuestas = [
#        "Es seguro que sí",
#        "Las chances son buenas",
#        "Puedes contar con ello",
#        "Pregúntame de nuevo más tarde",
#        "Concéntrate y pregunta de nuevo",
#        "No veo con claridad, intenta de nuevo",
#        "Mi respuesta es no",
#        "Mis fuentes me dicen que no"
#    ]
#    return random.choice(respuestas)
#pregunta = input("Hazme una pregunta: ")
#respuesta = bola_magica()
#print("La bola mágica dice:", respuesta)
"""Ejercicio 6"""
#Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)
#import time
#def medir_tiempo(func):
#    inicio = time.time()
#    func()
#    fin = time.time()
#    tiempo_total = fin - inicio
#    return tiempo_total
#def funcion_demo():
#    for _ in range(1000000):
#        pass
#tiempo = medir_tiempo(funcion_demo)
#print("Tiempo de ejecución:", tiempo, "segundos")
"""Ejercicio 7"""
#(Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.
#import random
#def simular_sorteo(participantes, cantidad_ganadores):
#    ganadores = random.sample(participantes, cantidad_ganadores)
#    return ganadores
#participantes = ["Juan", "Eric", "Leonel", "Guido", "Naruto", "Sans?"]
#cantidad_ganadores = 2
#ganadores = simular_sorteo(participantes, cantidad_ganadores)
#print("¡Los ganadores son:", ganadores)
"""Ejercicio 8"""
#(Opcional) Escriba una función que pida al usuario ingresar su fecha de
#nacimiento y sea capaz de devolver la cantidad de días desde su
#nacimiento hasta hoy
#import datetime
#def calcular_dias_desde_nacimiento(fecha_nacimiento):
#    hoy = datetime.date.today()
#    diferencia = hoy - fecha_nacimiento
#    return diferencia.days
#def obtener_fecha_nacimiento():
#    año = int(input("Ingresa el año de nacimiento: "))
#    mes = int(input("Ingresa el mes de nacimiento: "))
#    dia = int(input("Ingresa el día de nacimiento: "))
#    return datetime.date(año, mes, dia)
#fecha_nacimiento = obtener_fecha_nacimiento()
#dias_transcurridos = calcular_dias_desde_nacimiento(fecha_nacimiento)
#print(f"Han transcurrido {dias_transcurridos} días desde tu nacimiento.")
"""Ejercicio 9"""
#(Opcional) Implemente el programa del ejercicio 6 usando un diccionario
import random
def bola_magica_diccionario():
    respuestas = {
        1: "Es seguro que sí",
        2: "Las chances son buenas",
        3: "Puedes contar con ello",
        4: "Pregúntame de nuevo más tarde",
        5: "Concéntrate y pregunta de nuevo",
        6: "No veo con claridad, intenta de nuevo",
        7: "Mi respuesta es no",
        8: "Mis fuentes me dicen que no"
    }
    numero_respuesta = random.randint(1, 8)
    return respuestas[numero_respuesta]
pregunta = input("Hazme una pregunta: ")
respuesta = bola_magica_diccionario()
print("La bola mágica dice:", respuesta)
