import csv

def archivo_preguntas():

    with open ("preguntas.csv", "r") as csvfile:
       preguntas = list(csv.DictReader(csvfile))

    return preguntas

def ingreso_jugadores():

    lista_jugadores = []

    #Cantidad de jugadores
    cantidad_jugadores = int(input("Ingrese la cantidad de jugadores (Se puede de 2 a 4 participantes):"))

    #Mensaje de error por si no está dentro de las opciones
    while cantidad_jugadores < 2 or cantidad_jugadores > 4:
        cantidad_jugadores = int(input("Error, intente nuevamente. Ingrese la cantidad de jugadores (Se puede de 2 a 4 participantes):"))

    #Ingreso del jugador a la lista
    for i in range(cantidad_jugadores):

        lista_jugadores.append(str(input("Ingrese el nombre del jugador:")))

    print("Los participantes son:")

    for i in range(len(lista_jugadores)):

        print(lista_jugadores[i])    


    return lista_jugadores

def contador_puntos(jugadores,archivo_csv):

    lista_jugadores = jugadores

    preguntas = archivo_csv

    lista_puntajes = []
    #Bucle por cada pregunta

    for n in range(len(lista_jugadores)):
        print(f"Turno de: {lista_jugadores[n]}")
        puntaje = 0
    
        for i in range(5):
            print(preguntas[i]["pregunta"])
                
            print("1:", preguntas[i]["respuesta_1"])
            print("2:", preguntas[i]["respuesta_2"])
            print("3:", preguntas[i]["respuesta_3"])
            print("4:", preguntas[i]["respuesta_4"])

            numero_respuesta = int(input("Elija una respuesta:"))
            respuesta = None

            #Bucle While por si la respuesta no está dentro de las opciones
            while numero_respuesta < 1 or numero_respuesta > 4:
                numero_respuesta = int(input("Error, intente nuevamente:"))

            #Condicionales con posibles respuestas
            if numero_respuesta == 1:
                respuesta = preguntas[i]["respuesta_1"]
                print("Usted ha elegido", preguntas[i]["respuesta_1"])
            elif numero_respuesta == 2:
                respuesta = preguntas[i]["respuesta_2"]
                print("Usted ha elegido", preguntas[i]["respuesta_2"])
            elif numero_respuesta == 3:
                respuesta = preguntas[i]["respuesta_3"]
                print("Usted ha elegido", preguntas[i]["respuesta_3"])
            else:
                respuesta = preguntas[i]["respuesta_4"]
                print("Usted ha elegido", preguntas[i]["respuesta_4"])

            #Punto por si acierta
            if respuesta == preguntas[i]["respuesta_correcta"]:
                    puntaje += 1

        lista_puntajes.append(puntaje)      

    return lista_puntajes      
            
def comparar_puntaje(jugadores,puntos):

    lista_jugadores = jugadores
    lista_puntaje = puntos
    lista_ganadores = []
    mayor_puntaje = max(lista_puntaje)

    #Bucle para saber quienes obtuvieron el mayor puntaje
    for i in range(len(lista_jugadores)):

        if lista_puntaje[i] == mayor_puntaje:
            lista_ganadores.append(lista_jugadores[i])

    #Condicional para saber quiénes fueron los ganadores
    if len(lista_ganadores) == 1:
        print(f"Ha ganado {lista_ganadores[0]} con {mayor_puntaje} puntos")

    else:
        if len(lista_ganadores) == 2:
            print(f"Los ganadores han sido {lista_ganadores[0]} y {lista_ganadores[1]} con {mayor_puntaje} puntos")    
                
        elif len(lista_ganadores) == 3:
            print(f"Los ganadores han sido {lista_ganadores[0]}, {lista_ganadores[1]} y {lista_ganadores[2]} con {mayor_puntaje} puntos")

        else:
            print(f"Todos han empatado con {mayor_puntaje} puntos")


if __name__ == '__main__':
    #Bienvenida a la trivia
    print("Bienvenidos a capitales del mundo")

    #Ingreso jugadores
    lista_jugadores = ingreso_jugadores()

    #Abrir archivo csv con las preguntas
    preguntas = archivo_preguntas()

    #Ronda de preguntas con contador puntajes
    lista_puntajes= contador_puntos(lista_jugadores,preguntas)

    #Comparación de puntos y resultado final
    comparar_puntaje(lista_jugadores,lista_puntajes)

    #print(lista_jugadores)