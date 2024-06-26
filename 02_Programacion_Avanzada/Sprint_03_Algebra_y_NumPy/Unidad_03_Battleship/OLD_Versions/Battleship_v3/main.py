import numpy as np
import time

from class_Tablero import Tablero
from funciones import solicitar_coordenadas


def juego():
    '''
    Función principal del juego
    '''
    
    print('\n ~~~~ Bienvenidx a Hundir la Flota ~~~~ \n')
    print('Escriba "exit" en cualquier momento para terminar el juego\n')
    
    tablero_jugador = Tablero(jugador_id = 'Jugador') 
    tablero_maquina = Tablero(jugador_id = 'Máquina')

    juego_terminado = False
    
    # print(tablero_jugador)
    # print(type(tablero_jugador.tablero))
    tablero_jugador.mostrar_tableros(tablero_maquina, ocultar_barcos = False) # ocultar_barcos = False de momento para ver si funciona

    while not juego_terminado:      
        turno_jugador = True
        turno_maquina = True
        while turno_jugador:
            print()
            coordenadas = solicitar_coordenadas()
            # if coordenadas == "exit":
            #     juego_terminado = True
            turno_jugador = tablero_jugador.disparar(tablero_maquina, coordenadas)  # Mostramos los tableros desde main para que salgan en el mismo orden siempre           
            if turno_jugador:
                tablero_maquina.vidas_jugador -= 1
                print("Acertaste, continua...")
                print("\n\n") 
            if tablero_maquina.vidas_jugador == 0:
                print('FIN DE PARTIDA. Ganaste')
                turno_jugador = False
                turno_maquina = False
                juego_terminado = True
            tablero_jugador.mostrar_tableros(tablero_maquina, ocultar_barcos = True)  
        while turno_maquina:
            print()
            print("Turno de la máquina, pensando...")
            time.sleep(3)                                                                                       # Dejamos 3 segundos para no ser inmediato
            coordenadas = np.random.randint(0,10,2)                                                     # Generamos el disparo de la máquina
            print("La máquina dispara a: ["+str(coordenada[0])+","+str(coordenadas[1])+"]")    # Indica el disparo
            turno_maquina = tablero_maquina.disparar(tablero_jugador, coordenadas)                      # Realizamos el disparo de la máquina
            if turno_maquina:
                tablero_jugador.vidas_jugador -= 1
                print("La maquina acertó, sigue ella...")                
                print("\n\n")     
            if tablero_jugador.vidas_jugador == 0:
                print('FIN DE PARTIDA. Ganó la máquina.')
                turno_maquina = False
                juego_terminado = True                                           
            tablero_jugador.mostrar_tableros(tablero_maquina)                                                   # Mostramos los tableros desde main para que salgan en el mismo orden siempre           


if __name__ == "__main__":
    juego()  



# PSEUDO-CÓDIGO DE FUNCIONAMIENTO
'''
### El siguiente pseudo-código es la intención principal del programa
def juego():
    
    print('Bienvenido a Hundir la Flota')
    print('Instrucciones del juego:') # Instrucciones simples del juego
    tablero_jugador = Tablero(jugador_id = 'Jugador')
    tablero_maquina = Tablero(jugador_id = 'Maquina')

    juego_terminado = False
    turno_jugador = True

    while not juego_terminado:
        if turno_jugador:
            
            1 - Mostrar tableros
            2 - Pedir coordenadas
                2.1 Con comandos especiales salir de la partida o mostrar menú del juego
            3 - while ¿Tocado o hundido?
                3.1 Volver a pedir coordenadas
            
        else: # turno de la máquina
            
            Código similar al del 'Jugador' pero son métodos random
                - Nota: No puede disparar a casillas que ya ha disparado
'''

