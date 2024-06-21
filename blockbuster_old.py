import os
import platform
from colorama import Fore, Style, Back, init

init(autoreset=True)

# Detectar el sistema operativo para limpiar la pantalla
sistema = 'clear' if platform.system() != 'Windows' else 'cls'

# Películas alquiladas
alquilado = [{'usuario': '22555888', 'peliculas': ['El Padrino', 'Toy Story', 'Titanic']}, {'usuario': '42555888', 'peliculas': ['El Rey León', 'Toy Story', 'El Padrino']}]

# Lista de usuarios
lista_usuarios = [
    {"id_usuario": 1,
        "dni": "22555888",
        "nombre_apellido": "Juan Carlos Peralta",
        "contacto": "1178998844",
        "Domicilio": "Av. Brasil 235",
        "psw": 123456},
    
    {"id_usuario": 2, "dni": "22555888",
        "nombre_apellido": "Rodrigo Ramirez",
        "Domicilio": "Av. Mitre 4000",
        "contacto": "1178988891",
        "psw": 123456},
    {"id_usuario": 3, "dni": "25555988",
        "nombre_apellido": "Lautaro Martinez",
        "contacto": "1169878444",
        "Domicilio": "Cno. Doctor Federico 2020",
        "psw": 123456},
    {"id_usuario": 4, "dni": "32955788",
        "nombre_apellido": "Facundo Aguirre",
        "Domicilio": "Av. Miranda 7898",
        "contacto": "1178911844",
        "psw": 123456},
    {"id_usuario": 5, "dni": "43955788",
        "nombre_apellido": "Leandro Paredes",
        "Domicilio": "ESporas 5467",
        "contacto": "1175915847",
        "psw": 123456},
    {"id_usuario": 6, "dni": "19955588",
        "nombre_apellido": "Gonzalo Montiel",
        "Domicilio": "Av. Dardo Rocha 4589",
        "contacto": "1187987425", "psw": 123456}
]

# Películas disponibles
peliculas = [
    {'codigo_pelicula': 1,
        'titulo_pelicula': 'El Padrino',
        'genero_pelicula': 'Crimen, Drama',
        'año_pelicula': 1972,
        'descripcion_pelicula': 'La historia de una familia mafiosa italiana en los Estados Unidos.'},
    
    {'codigo_pelicula': 2,
        'titulo_pelicula': 'Toy Story',
        'genero_pelicula': 'Animación, Aventura, Comedia',
        'año_pelicula': 1995, 'descripcion_pelicula': 'Las aventuras de un grupo de juguetes que cobran vida cuando los humanos no están cerca.'},
    
    {'codigo_pelicula': 3,
        'titulo_pelicula': 'Titanic',
        'genero_pelicula': 'Drama, Romance',
        'año_pelicula': 1997,
        'descripcion_pelicula': 'Una historia de amor a bordo del trágico RMS Titanic.'},
    
    {'codigo_pelicula': 4,
        'titulo_pelicula': 'El Rey León',
        'genero_pelicula': 'Animación, Aventura, Drama',
        'año_pelicula': 1994, 'descripcion_pelicula': 'La historia de un joven león llamado Simba que debe reclamar su lugar como rey.'}
]

# Función para mostrar la lista de películas
def lista(peliculas):
    for pelicula in peliculas:
        print(f"{pelicula['codigo_pelicula']} {pelicula['titulo_pelicula']} {pelicula['genero_pelicula']} {pelicula['año_pelicula']} {pelicula['descripcion_pelicula']}")

# Función de autorización del usuario
def autorizacion(usuarios, peliculas):
    global dni
    intento = 3
    usu = False
    print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + ' ' * 90)
    print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + 'INGRESA TU DNI Y CONTRASEÑA PARA ALQUILAR PELICULAS!!!'.center(90, ' '))
    print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + ' ' * 90)
    print()
    while intento != 0:
        dni = input('Ingrese su DNI: ')
        for i, usuario in enumerate(usuarios):
            if usuario["dni"] == dni:
                print()
                print(Back.WHITE + Fore.BLUE + Style.BRIGHT + ' ' * 90)
                print(Back.WHITE + Fore.BLUE + Style.BRIGHT + f'BIENVENIDO {usuario["nombre_apellido"]}!!!'.center(90, ' '))
                print(Back.WHITE + Fore.BLUE + Style.BRIGHT + ' ' * 90)
                print()
                usu = True
                intento = 0
                return i
        if not usu:
            intento -= 1
            if intento == 0:
                print(Back.RED + Fore.WHITE + Style.BRIGHT + ' '*90)
                print(Back.RED + Fore.WHITE + Style.BRIGHT + 'ACCESO DENEGADO. HA SUPERADO EL NÚMERO DE INTENTOS PERMITIDOS.'.center(90, ' '))
                print(Back.RED + Fore.WHITE + Style.BRIGHT + ' '*90)

# Función para ver la lista de usuarios
def ver_lista_usuario(lista_usuarios):
    print(Back.YELLOW + Fore.CYAN + Style.BRIGHT + "****" * 25)
    print(Fore.CYAN + f"ID usuario\tNombre y apellido\tDNI\t\tTelefono\tDomicilio")
    for lista in lista_usuarios:
        print(Back.YELLOW + Fore.CYAN + Style.BRIGHT + "----" * 25)
        print(Fore.CYAN + f"{lista['id_usuario']}\t{lista['nombre_apellido']}\t{lista['dni']}\t{lista['contacto']}\t{lista['Domicilio']}")
    print(Back.YELLOW + Fore.CYAN + Style.BRIGHT + "****" * 25)

# Función para agregar un usuario
def agregar_usuario(lista_usuarios):
    lista_usuario = {}
    ultimo_usuario = lista_usuarios[-1]["id_usuario"]
    lista_usuario["id_usuario"] = ultimo_usuario + 1
    lista_usuario["dni"] = input("Ingrese DNI: ")
    lista_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
    lista_usuario["contacto"] = input("Ingrese numero de telefono: ")
    lista_usuario["Domicilio"] = input("Ingrese domicilio: ")
    lista_usuarios.append(lista_usuario)

# Función para eliminar un usuario
def eliminar_usuario(usuario, lista_usuarios):
    for usuario_eliminar in lista_usuarios:
        if usuario_eliminar["id_usuario"] == usuario:
            lista_usuarios.remove(usuario_eliminar)
            print("La baja se realizo correctamente")
            return
    print("No se encontro el usuario")

# Función para modificar los datos de un usuario
def modificar_lista_usuario(usuario, lista_usuarios):
    for modificar_usuario in lista_usuarios:
        if modificar_usuario["id_usuario"] == usuario:
            modificar_usuario["dni"] = input("Ingrese DNI: ")
            modificar_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
            modificar_usuario["contacto"] = input("Ingrese numero de telefono: ")
            modificar_usuario["Domicilio"] = input("Ingrese domicilio: ")
            print("Los datos se modificaron correctamente!!")
            return
    print("No se encontro usuario")

# Función para el menú de alquiler de películas
def menuAlquiler(posUsuario, usuario, peliculas, alquilado):
    global dni
    peli = False
    listaPelis = []
    print()
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + ' ' * 90)
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + f'¿{usuario[posUsuario]["nombre_apellido"]} QUE QUIERES VER HOY?'.center(90, ' '))
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + ' ' * 90)
    print()
    lista(peliculas)
    print()
    while True:
        alquila = input('Quieres Alquilar una Pelicula? ')
        if alquila.lower() == 'no':
            print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + ' ' * 90)
            print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + 'Vuelva pronto!!'.center(90, ' '))
            print(Back.BLUE + Fore.YELLOW + Style.BRIGHT + ' ' * 90)
            break
        elif alquila.lower() == 'si':
            while True:
                pelicula = input('¿Qué película quieres alquilar? ')
                for pelicula_a in peliculas:
                    if pelicula_a["titulo_pelicula"].lower() == pelicula.lower():
                        print()
                        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + ' ' * 90)
                        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + f'El alquiler de la pelicula {pelicula_a["titulo_pelicula"]} fue exitoso!'.center(90, ' '))
                        print(Back.WHITE + Fore.BLUE + Style.BRIGHT + ' ' * 90)
                        print()
                        peli = True
                        listaPelis.append(pelicula_a["titulo_pelicula"])
                        break
                if not peli:
                    print()
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + 'Esa película no está disponible.'.center(90, ' '))
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
                    print()
                otra = input('Quieres alquilar otra pelicula? ')
                if otra.lower() == 'no':
                    alquilado.append({'usuario': dni, 'peliculas': listaPelis})
                    break
        else:
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print(Back.RED + Fore.WHITE + Style.BRIGHT + 'Por favor, ingrese una opción válida'.center(90, ' '))
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print()

# Menú principal

def menuPrincipal():
    while True:
        os.system(sistema)    
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+'GRUPO 14'.center(90,' '))
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #######  #####  #    # ######  #     #  #####  ####### ####### ######   ')
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #     #  ') 
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     # #          #    #       #     #  ') 
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #     # #       ###    ######  #     #  #####     #    #####   ######   ')
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     #       #    #    #       #   #    ')
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #    #   ')
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  ####### #######  #####  #    # ######   #####   #####     #    ####### #     #  ')
        print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+' '*90)
        print(Back.YELLOW+Fore.BLUE+Style.BRIGHT+f'by Martina Luppi, Cristian Alderete, Patricio Noce, Javier Monzon '.rjust(90,' '))
        print()
        print(Back.BLUE+Fore.BLACK+' '*90)
        print(Back.BLUE+Fore.WHITE+Style.BRIGHT+'BIENVENIDOS A NUESTRO CLUB EN LINEA'.center(90,' '))
        print(Back.BLUE+Fore.BLACK+' '*90)
        print(Fore.YELLOW + Style.BRIGHT + "***" * 30)
        print(Fore.CYAN + Style.BRIGHT + "MENU PRINCIPAL".center(100, ' '))
        print(Fore.YELLOW + Style.BRIGHT + "---" * 30)
        print(Fore.YELLOW + Style.BRIGHT + "1. ALQUILER DE PELICULAS")
        print(Fore.YELLOW + Style.BRIGHT + "2. USUARIOS")
        print(Fore.YELLOW + Style.BRIGHT + "3. VER ALQUILERES")
        print(Fore.YELLOW + Style.BRIGHT + "4. SALIR")
        print(Fore.YELLOW + Style.BRIGHT + "***" * 30)
        print()
        opcion = int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
        os.system(sistema)

        if opcion == 1:
            posUsuario = autorizacion(lista_usuarios, peliculas)
            if posUsuario is not None:
                menuAlquiler(posUsuario, lista_usuarios, peliculas, alquilado)
        elif opcion == 2:
            while True:
                print(Fore.YELLOW + Style.BRIGHT + "****" * 25)
                print(Fore.CYAN + Style.BRIGHT + "GESTIÓN DE USUARIOS".center(100, ' '))
                print(Fore.YELLOW + Style.BRIGHT + "----" * 25)
                print(Fore.YELLOW + Style.BRIGHT + "1. Ver Usuarios")
                print(Fore.YELLOW + Style.BRIGHT + "2. Agregar Usuario")
                print(Fore.YELLOW + Style.BRIGHT + "3. Eliminar Usuario")
                print(Fore.YELLOW + Style.BRIGHT + "4. Modificar Usuario")
                print(Fore.YELLOW + Style.BRIGHT + "5. Volver al menú principal")
                print(Fore.YELLOW + Style.BRIGHT + "****" * 25)
                print()
                opcion_usuario = int(input(Fore.CYAN + Style.BRIGHT + "Seleccione una opción: "))
                os.system(sistema)

                if opcion_usuario == 1:
                    ver_lista_usuario(lista_usuarios)
                elif opcion_usuario == 2:
                    agregar_usuario(lista_usuarios)
                elif opcion_usuario == 3:
                    usuario = int(input("Ingrese el ID del usuario a eliminar: "))
                    eliminar_usuario(usuario, lista_usuarios)
                elif opcion_usuario == 4:
                    usuario = int(input("Ingrese el ID del usuario a modificar: "))
                    modificar_lista_usuario(usuario, lista_usuarios)
                elif opcion_usuario == 5:
                    break
                else:
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + 'Por favor, ingrese una opción válida'.center(90, ' '))
                    print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
                    print()
        elif opcion == 3:
            print(Fore.YELLOW + Style.BRIGHT + "****" * 25)
            print(Fore.RED + Style.BRIGHT + "LISTA DE ALQUILERES".center(100, ' '))
            print(Fore.YELLOW + Style.BRIGHT + "----" * 25)
            for alquilados in alquilado:
                print(f"Usuario: {alquilados['usuario']}, Películas: {', '.join(alquilados['peliculas'])}")
            input(Fore.CYAN + Style.BRIGHT + "\nPresione Enter para continuar...")
        elif opcion == 4:
            print(Fore.RED + Style.BRIGHT + "****" * 25)
            print(Fore.RED + Style.BRIGHT + "GRACIAS POR UTILIZAR EL SISTEMA DE ALQUILERES".center(100, ' '))
            print(Fore.RED + Style.BRIGHT + "----" * 25)
            break
        else:
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print(Back.RED + Fore.WHITE + Style.BRIGHT + 'Por favor, ingrese una opción válida'.center(90, ' '))
            print(Back.RED + Fore.WHITE + Style.BRIGHT + ' ' * 90)
            print()

# Iniciar el programa
if __name__ == "__main__":
    menuPrincipal()