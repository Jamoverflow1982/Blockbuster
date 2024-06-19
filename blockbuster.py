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
        