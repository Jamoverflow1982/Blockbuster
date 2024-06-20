"""
TP fin curso inicial
Martina - Cristian - Patricio - Javier Monzon
Preentrega 24-6-22
"""
import os

#CAMBIAR SEGUN SISTEMA OPERATIVO
sistema='clear' #Limpieza pantalla Linux o Mac
sistema='cls' #Limpieza pantalla Windows

from colorama import Fore, Style, Back, init
init(autoreset=True)

#Peliculas alquiladas (Javier)

alquilado=[{'usuario': '22555888', 'peliculas': ['El Padrino', 'Toy Story', 'Titanic']}, {'usuario': '42555888', 'peliculas': ['El Rey León', 'Toy Story', 'El Padrino']}]

#lista de usuarios 
lista_usuarios = [
        {
            
            "id_usuario":1,
            "dni": "22555888",
            "nombre_apellido": "Juan Carlos Peralta",
            "contacto": "1178998844",
            "Domicilio": "Av. Brasil 235",
            "psw": 123456
        },
        
        {
            
            "id_usuario":2,
            "dni": "22555888",
            "nombre_apellido": "Rodrigo Ramirez",
            "Domicilio": "Av. Mitre 4000",
            "contacto": "1178988891",
            "psw": 123456
        },
        
        {
            
            "id_usuario":3,
            "dni": "25555988",
            "nombre_apellido": "Lautaro Martinez",
            "contacto": "1169878444",
            "Domicilio": "Cno. Doctor Federico 2020",
            "psw": 123456
        },
        {
            
            "id_usuario":4,
            "dni": "32955788",
            "nombre_apellido": "Facundo Aguirre",
            "Domicilio": "Av. Miranda 7898",
            "contacto": "1178911844",
            "psw": 123456
        },
        {
            
            "id_usuario":5,
            "dni": "43955788",
            "nombre_apellido": "Leandro Paredes",
            "Domicilio": "ESporas 5467",
            "contacto": "1175915847",
            "psw": 123456
        },
        {
            
            "id_usuario":6,
            "dni": "19955588",
            "nombre_apellido": "Gonzalo Montiel",
            "Domicilio": "Av. Dardo rocha 4589",
            "contacto": "1187987425",
            "psw": 123456
        }
        
    ]
#funciones del usuario
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
#esta funcion permite ver la lista de usuarios
def lista(peliculas):
    for pelicula in peliculas:
            print(f"{pelicula['codigo_pelicula']} {pelicula['titulo_pelicula']} {pelicula['genero_pelicula']} {pelicula['año_pelicula']} {pelicula['descripcion_pelicula']}")

def autorizacion(usuarios, peliculas): #Autenticacion de usuario
    #Javier
    intento=3
    usu=False #Variable para validacion de usuario
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+'INGRESA TU DNI Y CONTRASEÑA PARA ALQUILAR PELICULAS!!!'.center(90,' '))
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print()
    while intento!=0: #Busca en el diccionario de usuarios si se encuentra el DNI
        dni=input('Ingrese su DNI: ')
        i=0
        for usuario in usuarios:
            if usuario["dni"]==dni:
                print()
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+f'BIENVENIDO {usuario["nombre_apellido"]}!!!'.center(90,' '))
                print(Back.WHITE+Fore.BLUE+Style.BRIGHT+' '*90)
                print()
                usu=True
                intento=0
                break
            i+=1
        if usu==False: #Si al buscar no coincide el DNI da 3 intentos para la busqueda
            intento-=1
def ver_lista_usuario(lista_usuarios):
    print(Back.YELLOW+Fore.CYAN+Style.BRIGHT+f"****"*25)
    print(Fore.CYAN+f"ID usuario\tNombre y apellido\tDNI\t\tTelefono\tDomicilio" )
    for lista in lista_usuarios:
        print(Back.YELLOW+Fore.CYAN+Style.BRIGHT+f"----"*25)
        print(Fore.CYAN+f"{lista["id_usuario"]} {"\t\t"}{lista["nombre_apellido"]} {"\t"}{lista["dni"]}{"\t"}{lista["contacto"]}{"\t"}{lista["Domicilio"]}")
    print(Back.YELLOW+Fore.CYAN+Style.BRIGHT+f"****"*25)
        
#esta funcion permite agregar usuarios         
def agregar_usuario(lista_usuarios):
    lista_usuario = {}
    ultimo_usuario = lista_usuarios[len(lista_usuarios)-1]["id_usuario"]
    lista_usuario["id_usuario"] = ultimo_usuario + 1
    lista_usuario["dni"] = input("Ingrese DNI: ")
    lista_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
    lista_usuario["contacto"] = input("Ingrese numero de telefono: ")
    lista_usuario["Domicilio"] = input("Ingrese domicilio: ")
    lista_usuarios.append(lista_usuario)
    
#esta funcion elimina usuarios con su id de socio
def eliminar_usuario(usuario, lista_usuarios):
    for usuario_eliminar in lista_usuarios:
        if usuario_eliminar["id_usuario"] == usuario:
            lista_usuarios.remove(usuario_eliminar)
            print("La baja se realizo correctamente")
            return
    print("No se encontro el usuario")    

#funcion para dodificar datos de usuario
def modificar_lista_usuario(usuario, lista_usuario):
    for modificar_usuario in lista_usuario:
        if modificar_usuario["id_usuario"] == usuario:
            modificar_usuario["dni"] = input("Ingrese DNI: ")
            modificar_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
            modificar_usuario["contacto"] = input("Ingrese numero de telefono: ")
            modificar_usuario["Domicilio"] = input("Ingrese domicilio: ")
            print("Los datos se modificaron correctamente!!")
            return
    print("No se encontro usuario") 
    
def menuAlquiler(posUsuario, usuario, peliculas, alquilado):
    #Javier
    peli=False
    listaPelis=[]
    print()
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+f'¿{usuario[posUsuario]["nombre_apellido"]} QUE QUIERES VER HOY?'.center(90,' '))
    print(Back.BLUE+Fore.WHITE+Style.BRIGHT+' '*90)
    print()
    lista(peliculas)
    while peli==False:
        try:
            i=0
            print()
            op=int(input(Fore.WHITE+Style.BRIGHT+'Elije por numero de pelicula: '))
            for pelicula in peliculas:
                if pelicula["codigo_pelicula"]==op:
                    print()
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+f'Usted esta por alquilar la pelicula {pelicula["titulo_pelicula"]}'.center(90,' '))
                    print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                    peli=True
                    listaPelis.append(pelicula["titulo_pelicula"])
                    break
                i+=1
            if peli==False: 
                print()
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' *90')
                print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LA OPCION {op} NO PERTENECE A UNA PELICULA'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+'INTENTE NUEVAMENTE'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
            else:
                while True:
                    try:
                        print()
                        agregar=input(Fore.WHITE+Style.BRIGHT+'¿Desea agregar otra pelicula mas? (S/N): ')
                        agregar=agregar.upper()
                        match agregar:
                            case "S":
                                peli=False
                                break
                            case "N":
                                break
                            case _:
                                print()
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'OPCION INVALIDA PRESIONE S o N'.CENTER(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+'INTENTE NUEVAMENTE'.CENTER(90,' '))
                                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                                print()
                    except AttributeError:
                        print()
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE S o N'.center(90,' '))
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO NUMEROS!'.center(90,' '))
                        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        except AttributeError:
            print()
            print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
            print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO PARA SELECCIONAR LA PELICULA'.center(90,' '))
            print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO CARACTERES!'.center(90,' '))
            print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
    print()
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+'Usted se llevara la(s) pelicula(s):'.center(90,' '))
    for cod in listaPelis:
        print(Back.WHITE+Fore.BLUE+Style.BRIGHT+f"{cod}".center(90,' '))
    print()
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+'¡ ¡ ¡ QUE DISFRUTE DEL ESPECTACULO ! ! !'.center(90,' '))
    print(Back.BLUE+Fore.YELLOW+Style.BRIGHT+' '*90)
    alquilado.append({"usuario":usuario[posUsuario]["dni"], "peliculas":listaPelis})
    
def menu_administradores():
    pass

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
print(Back.YELLOW+Fore.BLACK+' '*90)
print(Back.YELLOW+Fore.BLACK+'1 - ¿Sos usuario?'.center(90,' '))
print(Back.YELLOW+Fore.BLACK+' '*90)
print(Back.YELLOW+Fore.BLACK+'2 - ¿Como no sos usuario? Vamos a registrarte!!!'.center(90,' '))
print(Back.YELLOW+Fore.BLACK+' '*90)
print(Back.YELLOW+Fore.BLACK+'3 - Acceso para administradores'.center(90,' '))
print(Back.YELLOW+Fore.BLACK+' '*90)
print(Back.YELLOW+Fore.RED+'4 - SALIR'.center(90,' '))
print(Back.YELLOW+Fore.BLACK+' '*90)
print()
while True:
    try:
        op=int(input(Back.BLUE+Fore.WHITE+Style.BRIGHT+'Selecciona una opcion: '))
        print()
        match op:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                print()
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+'GRUPO 14'.center(90,' '))
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #######  #####  #    # ######  #     #  #####  ####### ####### ######   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #     #  ') 
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     # #          #    #       #     #  ') 
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  #       #     # #       ###    ######  #     #  #####     #    #####   ######   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #       #  #   #     # #     #       #    #    #       #   #    ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  #     # #       #     # #     # #   #  #     # #     # #     #    #    #       #    #   ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+f'  ######  ####### #######  #####  #    # ######   #####   #####     #    ####### #     #  ')
                print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+' '*90)
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'LOS PARTICIPANTES DEL GRUPO 14 AGRADECEN LA UTILIZACION DE NUESTRA PLATAFORMA'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'ESPERAMOS QUE VUELVA PRONTO!!!'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'ALUMNOS: Martina Luppi, Cristian Alderete, Patricio Noce, Javier Monzon'.center(90,' '))
                print(Back.YELLOW+Fore.WHITE+Style.BRIGHT+'CAC INICIAL 2024 Comision 24093'.center(90,' '))
                print()
                break
            case _:
                print()
                print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO ENTRE EL 1 Y EL 4'.center(90,' '))
                print(Back.RED+Style.BRIGHT+Fore.WHITE+f'EL NUMERO {op} NO ES UNA OPCION!'.center(90,' '))
                print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
                print()
    except ValueError:
        print()
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'POR FAVOR INGRESE UN NUMERO ENTRE EL 1 Y EL 4'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'¡NO ESTA PERMITIDO CARACTERES!'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print()
    except KeyboardInterrupt:
        print()
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'NA NA NA NA NAAAAAAAAA'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+'PARA SALIR UTILICE EL 4!'.center(90,' '))
        print(Back.RED+Style.BRIGHT+Fore.WHITE+' '*90)
        print()

#menu de opciones para manipular los datos del usuario
opcion = 1
while opcion != 5:
    print(Fore.YELLOW+"""
*************************************          
│   Lista de usuarios registrados   │ 
*************************************
│    1-AGREGAR USUARIO              │           
│    2-VER LISTA DE USUARIOS        │
│    3-ELIMINAR USUARIO             │
│    4-MODIFICAR USUARIO            │
│    5-SALIR                        │
*************************************                   
            """)
    try:
        opcion = int(input(Fore.YELLOW+"Elige una opción: "))
    except TypeError:
            print("Ingresa una opcion correcta")
    except Exception as e:
        print("Error no previsto", type(e).__name__)   
        continue
    match opcion:    
        case 1:
            agregar_usuario(lista_usuarios)
        case 2:
            ver_lista_usuario(lista_usuarios)
        case 3:
            usuario = int(input("Qué usuario quieres eliminar?- Ingrese id de usuario: "))
            eliminar_usuario(usuario, lista_usuarios)
        case 4:   
            print("Que usuario desea modificar? - Ingrese id de usuario")     
            usuario = int(input("Qué usuario quiere modificar? : "))
            modificar_lista_usuario(usuario, lista_usuarios)
        case 5:
            print("Programa finalizado - Hasta pronto!!")
        case _:
            print("Opción incorrecta")