from calculadora import * 

option = input("""
Seleccione una operación
1. Suma 
2. Resta
3. Division
""")

try:
    option = int(option)
except:
    print ("valor no valido")

if option not in [1,2,3]:
    print ("Valor no valido")
    exit()
    
if(1 == option):
    try:
        a=int(input(f'\n\n_Ingrese los valores a Sumar \n----> a = '))
        b=int(input('\n----> b = '))

        print(f'\nLa suma de {a}+{b} es igual a: {suma(a,b)}')
    except ValueError:
            input('Error, valor ingresado o valido \nPresione ENTER para continuar ...')
if(2 == option):
    try:
        a=int(input(f'\n\n_Ingrese los valores a Restar \n----> a = '))
        b=int(input('\n----> b = '))

        print(f'\nLa resta de {a}-{b} es igual a: {resta(a,b)}')
    except ValueError:
            input('Error, valor ingresado o valido \nPresione ENTER para continuar ...')     
if(3 == option):
    try:
        a=int(input(f'\n\n_Ingrese los valores a Dividir \n----> a = '))
        b=int(input('\n----> b = '))
        print(f'\nLa división de {a}/{b} es igual a: {division(a,b)}')
    except ValueError:
            input('Error, valor ingresado o valido \nPresione ENTER para continuar ...')
    except ZeroDivisionError:
            input('Error, no existe la división por 0 \nPresione ENTER para continuar ...')
