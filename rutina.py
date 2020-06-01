#!/usr/bin/env python3
import sys
from random import uniform
from random import randint
from math import pi

weekly_array = [100,	100,	100,	100,	100,	100,	100,	100,	300,	400,	400,	400,	500,	500,	300,	300,	300,	300,	300,	300,	500,	800,	700,	200,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	500,	500,	500,	7000,	7000,	500,	500,	500,	500,	500,	500,	7000,	7000,	7000,	500,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	500,	500,	500,	7000,	7000,	500,	500,	500,	500,	500,	500,	6000,	6000,	6000,	500,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	500,	500,	500,	6000,	6000,	500,	500,	500,	500,	500,	500,	6000,	6000,	6000,	500,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	500,	500,	500,	6000,	6000,	500,	500,	500,	500,	500,	500,	6000,	6000,	6000,	500,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	300,	500,	500,	6000,	6000,	500,	500,	500,	500,	500,	500,	5000,	5000,	6000,	500,	
500,	200,	200,	200,	200,	200,	200,	200,	300,	400,	400,	400,	1000,	1000,	500,	500,	500,	500,	500,	500,	1000,	1000,	1000,	500]


def usage():
    print('''
    Uso: 
        python3 rutina.py $cantidadRepartidores $radioEntrega $tiempoFinal [debug]

    Ejemplo: 
        python3 rutina.py 2 5 1000
        python3 rutina.py 4 20 10000 debug
    '''
    )

def generarIntervaloPedido(tiempoActual, radio):
    r = uniform(0, 1)
    superficie = pi * radio * radio
    superficie_cobertura_maxima_km2 = 1400
    # distribución lineal
    frecuencia_arribos_por_hora = (weekly_array[int(tiempoActual) % 168] * (superficie / superficie_cobertura_maxima_km2) ) * (0.9 + 0.2 * r)
    intervalo_arribo_segundos = 3600000 / frecuencia_arribos_por_hora
    return intervalo_arribo_segundos

def generarTiempoEntrega(radio):
    velocidad_promedio_kmh = 9
    minimo_tiempo_atencion_minutos = 18 #tiempo record
    peor_tiempo = (4 * radio) / velocidad_promedio_kmh
    r = uniform(0, 1)
    #distribución lineal
    tiempoEntrega = minimo_tiempo_atencion_minutos + r * peor_tiempo
    return tiempoEntrega

def buscarMenorTiempoComprometido(tiempoComprometidoRepartidores):
    # Busco el repartidor con menor tiempo comprometido
    menorTiempoComprometido = tiempoComprometidoRepartidores.index(min(tiempoComprometidoRepartidores))
    return menorTiempoComprometido

def calcularTiempoMaximoEntrega(listaTiemposEntrega):
    # Calcula el máximo tiempo de entrega en el que cae el 90% de los pedidos
    listaTiemposEntrega.sort()
    index = round(len(listaTiemposEntrega) * 0.9) - 1
    return listaTiemposEntrega[index]

def main():
    if len(sys.argv) < 4:
        usage()
        exit(1)

    # Leo argumentos
    cantidadRepartidores = int(sys.argv[1])
    radioEntrega = int(sys.argv[2])
    tiempoFinal = int(sys.argv[3])

    # Chequeo modo debug
    if len(sys.argv) == 5: 
        if sys.argv[4] == "debug": 
            debug = True
            print("\nModo debug habilitado")
    else: 
            debug = False

    print("\n#### Corriendo simulación con cantidad de repartidores = {0} y radio de entrega = {1} km ####".format(cantidadRepartidores, radioEntrega))
    
    # Seteo condiciones iniciales
    tiempoActual = tiempoProximoPedido = 0
    cantidadEntregas = tiempoMaximoEntrega = 0 
    tiempoComprometidoRepartidores = []
    listaTiemposEntrega = []

    for i in range(cantidadRepartidores):
        tiempoComprometidoRepartidores.append(0)

    ## Inicio simulación ##

    if not debug: print("\nEntregas: ", end = "")
    
    while (tiempoActual < tiempoFinal):

        if not debug: print(".", end = "")

        if debug: print("\nNúmero entrega = {0}".format(cantidadEntregas))

        # Avanzo el tiempo
        tiempoActual = tiempoProximoPedido
        if debug: print("Tiempo actual = {0}".format(tiempoActual))

        # Genero intervalo de próximo de pedido
        intervaloPedido = generarIntervaloPedido(tiempoActual, radioEntrega)
        if debug: print("Intervalo pedido = {0}".format(intervaloPedido))
        tiempoProximoPedido = tiempoActual + intervaloPedido
        if debug: print("Tiempo próximo pedido = {0}".format(tiempoProximoPedido))

        # Genero intervalo de tiempo de entrega
        tiempoEntrega = generarTiempoEntrega(radioEntrega)
        if debug: print("Intervalo entrega = {0}".format(tiempoEntrega))

        for i in range(cantidadRepartidores):
            if debug: print("Tiempo comprometido repartidor {0} = {1}".format(i, tiempoComprometidoRepartidores[i]))

        # Busco menor tiempo comprometido
        repartidor = buscarMenorTiempoComprometido(tiempoComprometidoRepartidores)
        
        if tiempoActual > tiempoComprometidoRepartidores[repartidor]:
            # Hay repartidores ociosos -> toman pedido inmediatamente
            tiempoComprometidoRepartidores[repartidor] = tiempoActual + tiempoEntrega
            listaTiemposEntrega.append(tiempoEntrega)
            cantidadEntregas += 1

        else:
            # No hay repartidores ociosos -> el pedido se demora
            tiempoComprometidoRepartidores[repartidor] = tiempoComprometidoRepartidores[repartidor] + tiempoEntrega
            listaTiemposEntrega.append((tiempoComprometidoRepartidores[repartidor] - tiempoActual))
            cantidadEntregas += 1

    ## Fin simulación ##

    # Calculo resultados
    tiempoMaximoEntrega = calcularTiempoMaximoEntrega(listaTiemposEntrega)
    resultadoExitoso = "SI" if (tiempoMaximoEntrega < 35) else "NO"
    
    # Imprimo resultados
    if debug: print("\nLista de tiempos de entregas: ", listaTiemposEntrega, end = "")
    print("\n\n#### Resultados con cantidad de repartidores = {0} y radio de entrega = {1} km #### \n".format(cantidadRepartidores, radioEntrega))####")
    print("Tiempo máximo de entrega en el 90% de pedidos = {0} min".format(tiempoMaximoEntrega))
    print("Cantidad de entregas = {0}".format(cantidadEntregas))
    print("Conclusión: {0} se logra tiempo máximo de entrega menor a 35 min\n".format(resultadoExitoso))

if __name__ == "__main__":
    try: 
        main()
    except ValueError:
        print ("ERROR!")
