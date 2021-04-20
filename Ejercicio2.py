# Definir una función maximo() que tome como argumento dos números y devuelva el mayor de ellos.

# Ejemplo de implementacion:

# Al llamar a la funcion maximo y definirle como argumentos, 5 y 15, deberia retornar 15

# numero_maximo = maximo(5, 15)
# print(numero_maximo) --> debe ser igual a 15

def maximo(a, b):

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 'Son iguales'


input_user1 = input('ingresa un numero: ')
input_user2 = input('Ingresa un numero para comparar: ')

a = int(input_user1)
b = int(input_user2)

if isinstance(maximo(a, b), int):
    print('El mayor numero es: ', maximo(a, b))
else:
    print(maximo(a, b))
