def ingresar_persona():
    # Ingresar los datos de una nueva persona
    nombre = input("Ingrese el nombre de la persona: ")
    apellido = input("Ingrese el apellido de la persona: ")
    dni = input("Ingrese el DNI de la persona: ")
    telefonos = input("Ingrese los números de teléfono separados por comas: ").split(',')
    hijos = input("Ingrese los nombres de los hijos separados por comas: ").split(',')

    # Limpiar posibles espacios extra en los datos
    telefonos = [telefono.strip() for telefono in telefonos]
    hijos = [hijo.strip() for hijo in hijos]

    # Retornar la persona como una lista
    return [nombre, apellido, dni, telefonos, hijos]


def mostrar_datos(personas):
    # Mostrar todos los datos de las personas ingresadas
    for persona in personas:
        nombre, apellido, dni, telefonos, hijos = persona
        print(f"Nombre: {nombre} {apellido}")
        print(f"DNI: {dni}")
        print(f"Teléfonos: {', '.join(telefonos)} (Cantidad: {len(telefonos)})")
        print(f"Hijos: {', '.join(hijos)} (Cantidad: {len(hijos)})")
        print("-" * 40)


def filtrar_por_dni(personas):
    # Filtrar y mostrar datos por DNI
    dni_buscar = input("Ingrese el DNI de la persona a buscar: ")
    persona_encontrada = None

    for persona in personas:
        if persona[2] == dni_buscar:
            persona_encontrada = persona
            break
    
    if persona_encontrada:
        nombre, apellido, dni, telefonos, hijos = persona_encontrada
        print(f"Datos de la persona con DNI {dni}:")
        print(f"Nombre: {nombre} {apellido}")
        print(f"DNI: {dni}")
        print(f"Teléfonos: {', '.join(telefonos)} (Cantidad: {len(telefonos)})")
        print(f"Hijos: {', '.join(hijos)} (Cantidad: {len(hijos)})")
    else:
        print("Persona no encontrada con ese DNI.")

# * Incluyo 2 métodos para el menú, un bloque if y un match case (un método que me recomendó un compañero, similar a switch en js)
# ! Comentar el bloque que no se utilice para el funcionamiento del código seleccionandolo y luego Shift + """

def menu():
    personas = []  # Lista para almacenar las personas ingresadas
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar nueva persona")
        print("2. Mostrar todos los datos")
        print("3. Filtrar por DNI")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            # Ingresar una nueva persona
            persona = ingresar_persona()
            personas.append(persona)
        elif opcion == "2":
            # Mostrar todos los datos
            mostrar_datos(personas)
        elif opcion == "3":
            # Filtrar por DNI
            filtrar_por_dni(personas)
        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 4.")


# Ejecutar el menú
menu()

# * Bloque opcional

def menu():
    personas = []  # Lista para almacenar las personas ingresadas
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar nueva persona")
        print("2. Mostrar todos los datos")
        print("3. Filtrar por DNI")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        match opcion:
            case "1":
                # Ingresar una nueva persona
                persona = ingresar_persona()
                personas.append(persona)
            case "2":
                # Mostrar todos los datos
                mostrar_datos(personas)
            case "3":
                # Filtrar por DNI
                filtrar_por_dni(personas)
            case "4":
                # Salir del programa
                print("Saliendo del programa.")
                break
            case _:
                # Opción no válida
                print("Opción no válida, por favor seleccione una opción del 1 al 4.")

# Ejecutar el menú
menu()    
