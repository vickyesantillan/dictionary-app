# Suponga que 's' es una cadena de caracteres en minúscula.

# Escribe un programa que cuente el número de vocales contenidas en la cadena s.
# Las vocales válidas son: 'a', 'e', ​​'i', 'o' y 'u'.
#
# Por ejemplo, si s = 'azcbobobegghakl', su programa debería imprimir:

# Numero de vocales: 5


def vocal_counter(s):
    '''
    This function will return how many vocals are in a string 's'
    '''
    cont = 0

    for i in range(len(list(s))):

        if s[i] == 'a':
            cont += 1
        elif s[i] == 'e':
            cont += 1
        elif s[i] == 'i':
            cont += 1
        elif s[i] == 'o':
            cont += 1
        elif s[i] == 'u':
            cont += 1
    return cont


inputuser = input('Input a character chain of letters to analyze: ')

if inputuser == '':
    print('You did not introduce anything, please try again')
else:
    print('The number of vocals is:', vocal_counter(inputuser))
