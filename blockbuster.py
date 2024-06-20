"""
TP fin curso inicial
Martina - Cristian - Patricio - Javier Monzon
Preentrega 24-6-22
"""
import os

#CAMBIAR SEGUN SISTEMA OPERATIVO
sistema='clear' #Limpieza pantalla Linux o Mac
#sistema='cls' #Limpieza pantalla Windows

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
            "psw":"123456"
        },
        {
            
            "id_usuario":2,
            'dni': "22555888",
            "nombre_apellido": "Rodrigo Ramirez",
            "contacto": "1178988891",
            "psw":"123456"
        },
        {
            "id_usuario":3,
            'dni': "42555888",
            "nombre_apellido": "Julian Alvarez",
            "contacto": "1158989687",
            "psw":"123456"
        },
        {
            
            "id_usuario":4,
            "dni": "25555988",
            "nombre_apellido": "Lautaro Martinez",
            "contacto": "1169878444",
            "psw":"123456"
        },
        {
            
            "id_usuario":5,
            "dni": "32955788",
            "nombre_apellido": "Facundo Aguirre",
            "contacto": "1178911844",
            "psw":"123456"
        }
    ]
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
            print()
            print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
            print(Back.RED+Fore.WHITE+Style.BRIGHT+'EL DNI NO COINCIDE CON NINGUN USUARIO'.center(90,' '))
            print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LE QUEDAN {intento} INTENTOS'.center(90,' '))
            print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
            print()
    if usu==True:
        usu=False
        intento=3
        while intento!=0: #Comprueba si la contraseña es correcta
            clave=input('Ingrese su contraseña: ')
            if usuarios[i]["psw"]==clave:
                print()
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+'¡ ¡ ¡ CONTRASEÑA CORRECTA ! ! !'.center(90,' '))
                print(Back.GREEN+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
                intento=0
                usu=True
            else:
                intento-=1
                print()
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print(Back.RED+Fore.WHITE+Style.BRIGHT+'CONTRASEÑA INCORRECTA!'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+f'LE QUEDAN {intento} INTENTOS'.center(90,' '))
                print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
                print()
    
    if usu==False: 
        print()
        print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
        print(Back.RED+Fore.WHITE+Style.BRIGHT+'NO SE PUDO AUTENTICAR USUARIO'.center(90,' '))
        print(Back.RED+Fore.WHITE+Style.BRIGHT+'VOLVIENDO AL MENU PRINCIPAL'.center(90,' '))
        print(Back.RED+Fore.WHITE+Style.BRIGHT+' '*90)
        print()
    
    return usu,i #Retorna si se pudo aprobar el acceso y en que posicion del diccionario esta el usuario

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

while True:
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
    try:
        op=int(input(Fore.WHITE+Style.BRIGHT+'Selecciona una opcion: '))
        print()
        match op:
            case 1:
                usuEncontrado, pos = autorizacion(lista_usuarios, peliculas)
                if usuEncontrado==True:
                    menuAlquiler(pos, lista_usuarios, peliculas, alquilado)
                print()
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
        