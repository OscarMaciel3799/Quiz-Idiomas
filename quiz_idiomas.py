import random
import datos

print("--- QUIZ DE IDIOMAS ---")
while True:
    print("Que temática le gustaría estudiar hoy?")
    print("1) Colores")
    print("2) Días")
    print("3) Estaciones")
    print("4) Frases")
    print("5) Meses")
    print("6) Números")
    print("7) Salir")
    tematica=int(input(">"))
    match tematica:
        case 1:
            lista=datos.colores
        case 2:
            lista=datos.dias
        case 3:
            lista=datos.estaciones
        case 4:
            lista=datos.frases
        case 5:
            lista=datos.meses
        case 6:
            lista=datos.numeros
        case 7:
            print("Saliendo...")
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
            continue  
    
    print("Modo 1: Español → Alemán")
    print("Modo 2: Alemán → Español")
    modo=input("Elige modo (1 o 2):")

    print("\nEscribe 'salir' para terminar.\n")

    while True:
        esp, ale = random.choice(lista)
        intentos=3
        if modo == "1":
            print("Traduce --->  ",esp,"  <---al alemán:")
            while intentos>0:
                
                respuesta = input("Tu respuesta: ")

                if respuesta.lower() == "salir":
                    break
            
                if respuesta.strip().lower() == ale.strip().lower():
                    print("✅ Correcto!\n")
                    intentos=0
                else:
                    intentos-=1
                    if intentos==0:
                        print("❌ Incorrecto.")
                        print("Respuesta:", ale, "\n")
                    else:
                        print("Te quedan ",intentos, "intentos")

        else:
            print("Traduce al español:")
            print("👉", ale)
            
            while intentos>0:
                respuesta = input("Tu respuesta: ")

                if respuesta.lower() == "salir":
                    break

                if respuesta.strip().lower() == esp.strip().lower():
                    print("✅ Correcto!\n")
                    intentos=0
                else:
                    intentos-=1
                    if intentos==0:
                        print("❌ Incorrecto.")
                        print("Respuesta:", esp, "\n")
                    else:
                        print("Te quedan ",intentos, "intentos")

    print("👋 Fin del programa. ¡Buen estudio!")