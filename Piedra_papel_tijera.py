def jugar():
    # Inicializar puntos
    Puntos_jugadorNo1= 0 #Inicianda el puntaja del JugadorNo1 en 0
    Puntos_jugadorNo2= 0 #Iniciando el puntaje del JugadorNo2 en 0
    Juego_Activo = True #controla si el juego esta activo

    while Juego_Activo:
        # Solicitar la eleccion de ambos jugadores
        Eleccion_jugadorNo1=input("jugador No 1, elige: Piedra, Papel o Tijera: ").lower()
        Eleccion_jugadorNo2=input("jugador No 2, elige: Piedra, Papel o Tijera: ").lower()

        # Validar que las elecciones sean correctas
        if Eleccion_jugadorNo1 not in ["piedra","papel","tijera"] or Eleccion_jugadorNo2 not in ["piedra","papel","tijera"]:
            print("!Error! elige entre: Piedra, Papel o Tijera") 
            continue # Volver a perdir eleccion si la entrada es incorrecta

        # Comparar las elecciones
        if Eleccion_jugadorNo1 == Eleccion_jugadorNo2:
            print("!Empate sigue jugando !")
        else:
            # Combinaciones que determinan al ganador
            if  Eleccion_jugadorNo1=="piedra"and Eleccion_jugadorNo2 =="tijera":
                print("JugadorNo1 !gana!")
                Puntos_jugadorNo1+=1
                
            elif Eleccion_jugadorNo1 == "papel"and Eleccion_jugadorNo2 == "piedra":
                print("jugadorNo1 !gana!")
                Puntos_jugadorNo1+=1

            elif Eleccion_jugadorNo1 == "tijera"and Eleccion_jugadorNo2 == "papel":
                print("jugadorNo1 !gana!")
                Puntos_jugadorNo1+=1

            elif Eleccion_jugadorNo2 == "piedra"and Eleccion_jugadorNo1 == "tijera":
                print("jugadorNo2 !gana!")
                Puntos_jugadorNo2+=1

            elif Eleccion_jugadorNo2 == "papel"and Eleccion_jugadorNo1 == "piedra":
                print("JugadorNo2 !gana!")
                Puntos_jugadorNo2+=1
                
            elif Eleccion_jugadorNo2 == "tijera"and Eleccion_jugadorNo1 == "papel":
                print("!jugadorNo2 !gana!")
                Puntos_jugadorNo2+=1

        #Mostrar puntaje actuales
        print(f"puntajes - JugadorNo1: {Puntos_jugadorNo1},JugadorNo2:{Puntos_jugadorNo2}")
        #preguntar si desean jugar otra vez
        respuesta=input("Jugar otra vez? (si/no):").lower()
        if respuesta != "si":
            Juego_Activo= False
    #Mostrar puntaje final
    print ("!juego terminado!")
    print(f"Puntaje final-Jugador No 1:{Puntos_jugadorNo1}, Jugador No 2: {Puntos_jugadorNo2}")
#Llamar a la funcion para iniciar el juego
jugar()