#!/usr/bin/env python3
import sys
from random import randint

def usage():
    print('''
    Usage: 
        python3 rutina.py $cantidadRepartidores $radioEntrega
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

def main():
    if len(sys.argv) < 2:
        usage()
        exit(1)

    # Leo argumentos
    cantidadRepartidores = int(sys.argv[1])
    radioEntrega = int(sys.argv[2])
    print("")
    print("#### Simulando con cantidad de repartidores = {0} y radio de entrega = {1} km #### ".format(cantidadRepartidores, radioEntrega))
    
    # Seteo condiciones iniciales
    tiempoActual = tiempoProximoPedido = 0
    tiempoFinal = 1000
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
    tiempoMedioEspera = round(tiempoTotalEspera / cantidadEntregas)
    print("")
    print("#### Resultados con cantidad de repartidores = {0} y radio de entrega = {1} km #### ".format(cantidadRepartidores, radioEntrega))####")
    print("")
    print("Tiempo medio de espera = {0} min".format(tiempoMedioEspera))
    print("Cantidad de entregas = {0}".format(cantidadEntregas))

    if tiempoMedioEspera < 35:
        resultadoExitoso = "SI"
    else:
        resultadoExitoso = "NO"
    print("Conclusión: {0} se logra tiempo medio de espera menor a 35 min".format(resultadoExitoso))
    print("")

if __name__ == "__main__":
    main()
