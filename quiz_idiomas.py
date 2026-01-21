import random

frases=[("Hola", "Hallo!"),
    ("Buenos días", "Guten Morgen!"),
    ("Buen día", "Guten Tag"),
    ("Buenas noches", "Gute Nacht"),
    ("¿Cómo estás?", "Wie geht es dir?"),
    ("Estoy bien", "Mir geht es gut"),
    ("Me llamo ...", "Ich heiße ..."),
    ("¿De dónde eres?", "Woher kommst du?"),
    ("Vengo de Argentina", "Ich komme aus Argentinien"),
    ("Tengo hambre", "Ich habe Hunger"),
    ("Tengo sed", "Ich habe Durst"),
    ("Estoy cansado.", "Ich bin müde"),
    ("¿Dónde está el baño?", "Wo ist das Badezimmer?"),
    ("Estudio alemán", "Ich lerne Deutsch"),
    ("¿Qué te gusta hacer?", "Was machst du gern?"),
    ("Está lloviendo", "Es regnet"),
    ("Necesito ayuda", "Ich brauche Hilfe"),
    ("Hasta mañana", "Bis morgen"),
    ("Eso es interesante", "Das ist interessant"),
    ("No entiendo", "Ich verstehe nicht")
]

print("--- QUIZ DE IDIOMAS ---")
print("Modo 1: Español → Alemán")
print("Modo 2: Alemán → Español")

modo = input("Elige modo (1 o 2): ")

print("\nEscribe 'salir' para terminar.\n")

while True:
    esp, ale = random.choice(frases)
    intentos=3
    if modo == "1":
        print("Traduce al alemán:")
        print("👉", esp)
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