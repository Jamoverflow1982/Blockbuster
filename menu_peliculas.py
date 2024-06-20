# Muestra la lista de películas.
def lista(peliculas):
    for pelicula in peliculas:
            print(f"{pelicula['codigo_pelicula']} {pelicula['titulo_pelicula']} {pelicula['genero_pelicula']} {pelicula['año_pelicula']} {pelicula['descripcion_pelicula']}")

# Añade una nueva pelicula a la lista.
def alta(peliculas):
    pelicula = {}
    ultima_pelicula = 4 # Comienza en 4 porque ya hay 4 películas en la lista inicial
    ultima_pelicula += 1
    pelicula = {
        "codigo_pelicula": ultima_pelicula,
        "titulo_pelicula": input("Titulo: "),
        "genero_pelicula": input("Genero: "),
        "año_pelicula": int(input("Año: ")),
        "descripcion_pelicula": input("Descripcion: ")
    }
    peliculas.append(pelicula)
    reasignar_codigos(peliculas)
    print("El Alta se realizó correctamente")

# Elimina una pelicula de la lista por su codigo.
def baja(codigo, peliculas):
    for pelicula in peliculas:
        if pelicula["codigo_pelicula"] == codigo:
            peliculas.remove(pelicula)
            print("La Baja se realizó correctamente")
            reasignar_codigos(peliculas)
            return
    print("No se encontró el titulo")

# Modifica una pelicula de la lista por su codigo.
def modificar(codigo, peliculas):
    for pelicula in peliculas:
        if pelicula["codigo_pelicula"] == codigo:
            pelicula["genero_pelicula"] = input("Genero: ")
            pelicula["año_pelicula"] = int(input("Año: "))
            pelicula["descripcion_pelicula"] = input("Descripcion: ")
            print("La Modificación se realizó correctamente")
            reasignar_codigos(peliculas)
            return
    print("No se encontró el titulo")

# Reasigna el codigo de la lista de peliculas nuevamente.    
def reasignar_codigos(peliculas):
    ultima_pelicula = 0  # Reiniciar el contador
    for pelicula in peliculas:
        ultima_pelicula += 1
        pelicula["codigo_pelicula"] = ultima_pelicula
        
peliculas = [
        {
            'codigo_pelicula': 1,
            'titulo_pelicula': 'El Padrino',
            'genero_pelicula': 'Crimen, Drama',
            'año_pelicula': 1972,
            'descripcion_pelicula': 'La historia de una familia mafiosa italiana en los Estados Unidos.',
        },
        {
            'codigo_pelicula': 2,
            'titulo_pelicula': 'Toy Story',
            'genero_pelicula': 'Animación, Aventura, Comedia',
            'año_pelicula': 1995,
            'descripcion_pelicula': 'Las aventuras de un grupo de juguetes que cobran vida cuando los humanos no están cerca.',
        },
        {
            'codigo_pelicula': 3,
            'titulo_pelicula': 'Titanic',
            'genero_pelicula': 'Drama, Romance',
            'año_pelicula': 1997,
            'descripcion_pelicula': 'Una historia de amor a bordo del trágico RMS Titanic.',
        },
        {
            'codigo_pelicula': 4,
            'titulo_pelicula': 'El Rey León',
            'genero_pelicula': 'Animación, Aventura, Drama',
            'año_pelicula': 1994,
            'descripcion_pelicula': 'La historia de un joven león llamado Simba que debe reclamar su lugar como rey.',
        }
    ]

opcion = 0
while opcion != "5":
    print("\nListado de Peliculas\n")
    print("1- Alta")
    print("2- Baja")
    print("3- Lista")
    print("4- Modificación")
    print("5- Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("\nAlta de Pelicula")
        alta(peliculas)
    elif opcion == "2":
        print("\nBaja de Pelicula")
        lista(peliculas)
        codigo = int(input("Escribe el Codigo de la Pelicula a eliminar: "))
        baja(codigo, peliculas)
    elif opcion == "3":
        print("\nLista de Peliculas")
        lista(peliculas)
    elif opcion == "4":
        print("\nModificar Pelicula")
        lista(peliculas)
        codigo = int(input("Escribe el Codigo de la Pelicula a modificar: "))
        modificar(codigo, peliculas)
    elif opcion == "5":
        print("Salir")
        print("Cerrando el programa... Adiós")
    else:
        print("Opción incorrecta")