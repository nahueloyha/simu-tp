#!/usr/bin/env python3
import sys
from random import randint

listaDeTAs = []

def usage():
    print('''
    Uso: 
        python3 rutina.py $cantidadRepartidores $radioEntrega $tiempoFinal

    Ejemplo: 
        python3 rutina.py 2 5 1000
    '''
    )


def generarIntervaloPedido(tiempoActual):
    # Acá iría la FDP de intervaloPedido
    intervaloPedidoRandom = randint(5,20)
    return intervaloPedidoRandom


def generarTiempoEntrega(radioEntrega):
    # Acá iría la FDP de tiempoEntrega
    tiempoEntregaRandom = randint(10,20) * radioEntrega
    return tiempoEntregaRandom


def buscarMenorTiempoComprometido(tiempoComprometidoRepartidores):
    # Busco el repartidor con menor tiempo comprometido
    menorTiempoComprometido = tiempoComprometidoRepartidores.index(min(tiempoComprometidoRepartidores))
    return menorTiempoComprometido

def calcularMaximoTA():
    #Calcula el maximo tiempo de atencion en el que cae el 90% de los pedidos
    print("Array de TAs:")
    print(listaDeTAs)
    listaDeTAs.sort()
    index = round(len(listaDeTAs) * 0.9) - 1
    return listaDeTAs[index]

def main():
    if len(sys.argv) < 4:
        usage()
        exit(1)

    # Leo argumentos
    cantidadRepartidores = int(sys.argv[1])
    radioEntrega = int(sys.argv[2])
    tiempoFinal = int(sys.argv[3])
    print("")
    print("#### Simulando con cantidad de repartidores = {0} y radio de entrega = {1} km #### ".format(cantidadRepartidores, radioEntrega))
    print("")
    print ("        ...        ")
    print("")
    # Seteo condiciones iniciales
    tiempoActual = tiempoProximoPedido = 0
    cantidadEntregas = tiempoTotalEspera = 0 
    tiempoComprometidoRepartidores = []

    for i in range(cantidadRepartidores):
        tiempoComprometidoRepartidores.append(randint(10,30))
        # tiempoComprometidoRepartidores.append(0)

    ## Inicio simulación ##

    while (tiempoActual < tiempoFinal):

        print("")

        # Avanzo el tiempo
        tiempoActual = tiempoProximoPedido
        print("Tiempo actual = {0}".format(tiempoActual))

        # Genero intervalo de próximo de pedido
        intervaloPedido = generarIntervaloPedido(tiempoActual)
        print("Intervalo pedido = {0}".format(intervaloPedido))
        tiempoProximoPedido = tiempoActual + intervaloPedido
        print("Tiempo próximo pedido = {0}".format(tiempoProximoPedido))

        # Genero intervalo de tiempo de entrega
        tiempoEntrega = generarTiempoEntrega(radioEntrega)
        listaDeTAs.append(tiempoEntrega)
        print("Intervalo entrega = {0}".format(tiempoEntrega))

        for i in range(cantidadRepartidores):
            print("Tiempo comprometido repartidor {0} = {1}".format(i, tiempoComprometidoRepartidores[i]))

        # Busco menor tiempo comprometido
        repartidor = buscarMenorTiempoComprometido(tiempoComprometidoRepartidores)

        if tiempoActual > tiempoComprometidoRepartidores[repartidor]:
            # Hay repartidores ociosos -> toman pedido inmediatamente
            tiempoComprometidoRepartidores[repartidor] = tiempoActual + tiempoEntrega
            tiempoTotalEspera = tiempoTotalEspera + tiempoEntrega
            cantidadEntregas = cantidadEntregas + 1

        else:
            # No hay repartidores ociosos -> el pedido se demora
            tiempoComprometidoRepartidores[repartidor] = tiempoComprometidoRepartidores[repartidor] + tiempoEntrega
            tiempoTotalEspera = tiempoTotalEspera + tiempoComprometidoRepartidores[repartidor] - tiempoActual
            cantidadEntregas = cantidadEntregas + 1

    ## Fin simulación ##

    # Imprimo resultados
    tiempoMedioEspera = calcularMaximoTA()
    print("")
    print("#### Resultados con cantidad de repartidores = {0} y radio de entrega = {1} km #### ".format(cantidadRepartidores, radioEntrega))####")
    print("")
    print("Tiempo maximo de atencion en el 90% de pedidos = {0} min".format(tiempoMedioEspera))
    print("Cantidad de entregas = {0}".format(cantidadEntregas))

    if tiempoMedioEspera < 35:
        resultadoExitoso = "SI"
    else:
        resultadoExitoso = "NO"
    print("Conclusión: {0} se logra tiempo medio de espera menor a 35 min".format(resultadoExitoso))
    print("")

if __name__ == "__main__":
    main()


