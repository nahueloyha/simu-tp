# Optimización de tiempos de entrega en plataformas de delivery

Trabajo Práctico Nº 6 - 1º Cuat. 2020

Grupo 03 - Simulación - UTN - FRBA

## Integrantes

Nombre | Padrón
:---: | :---:
Federico Torres | 148.739-5
Jose Fuentes | 88.525-2
Nahuel Oyhanarte | 154.566-8

## Requisitos

* [python3](https://www.python.org/downloads)

## Instrucciones

1. Clonar este repositorio: `git clone https://github.com/nahueloyha/simu-tp`

2. Entrar al directorio: `cd simu-tp`

3. Ejecutar la simulación: `python3 rutina.py $cantidadRepartidores $radioEntrega $tiempoFinal [debug]`

## Variables

```bash
$cantidadRepartidores: número entero, representa personas
$radioEntrega: número entero, representa kilómetros
$tiempoFinal: número entero, representa duración de la simulación
debug: string literal "debug", opcional, para ejecutar en modo debug/verbose (deshabilitado x default)
```

## Ejemplo

* Simular 2 repartidores, con 5 kilómetros de radio de entrega y por 1000 minutos: `python3 rutina.py 2 5 1000`
* Simular 4 repartidores, con 20 kilómetros de radio de entrega, por 10000 minutos y en modo debug: `python3 rutina.py 4 20 10000 debug`
