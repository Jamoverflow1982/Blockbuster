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
"""
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
        print()"""

#funciones del usuario
        
#esta funcion permite ver la lista de usuarios
def ver_lista_usuario(lista_usuarios):
    print(f"ID usuario \t Nombre y apellido \t DNI \t\t Telefono" )
    for lista in lista_usuarios:
        print(f"----"*20)
        print(f"{lista["id_usuario"]} {"\t\t"}{lista["nombre_apellido"]} {"\t"}{lista["dni"]}{"\t"}{lista["contacto"]} ")
            
#esta funcion permite agregar usuarios         
def agregar_usuario(lista_usuarios):
    lista_usuario = {}
    ultimo_usuario = lista_usuarios[len(lista_usuarios)-1]["id_usuario"]
    lista_usuario["id_usuario"] = ultimo_usuario + 1
    lista_usuario["dni"] = input("Ingrese DNI: ")
    lista_usuario["nombre_apellido"] = input("Ingrese nombre y apellido: ")
    lista_usuario["contacto"] = input("Ingrese numero de telefono: ")
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
            print("Los datos se modificaron correctamente!!")
            return
    print("No se encontro usuario")    

#lista de usuarios 
lista_usuarios = [
        {
            
            "id_usuario":1,
            "dni": "22555888",
            "nombre_apellido": "Juan Carlos Peralta",
            "contacto": "1178998844"
        },
        {
            
            "id_usuario":2,
            'dni': "22555888",
            "nombre_apellido": "Rodrigo Ramirez",
            "contacto": "1178988891"
        },
        {
            "id_usuario":3,
            'dni': "42555888",
            "nombre_apellido": "Julian Alvarez",
            "contacto": "1158989687"
        },
        {
            
            "id_usuario":4,
            "dni": "25555988",
            "nombre_apellido": "Lautaro Martinez",
            "contacto": "1169878444"
        },
        {
            
            "id_usuario":5,
            "dni": "32955788",
            "nombre_apellido": "Facundo Aguirre",
            "contacto": "1178911844"
        }
    ]
#menu de opciones para manipular los datos del usuario
opcion = 1
while opcion != 5:
    print(Back.BLUE+Style.BRIGHT+Fore.YELLOW+"""
Lista de usuarios registrados   

    1-AGREGAR USUARIO                         
    2-VER LISTA DE USUARIOS     
    3-ELIMINAR USUARIO      
    4-MODIFICAR USUARIO     
    5-SALIR                 
            """)
    
    opcion = int(input("Elige una opción: "))
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