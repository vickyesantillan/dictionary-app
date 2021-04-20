# Producto Vectorial entre vectores

def prod_vect(A, B):
    '''
    This function will calculate the vectorial product between two vectors A and B from R3
    Esta funcion va a calcular el producto vectorial entre dos vectores A y B de R3
    '''
    axb = []  # Vector producto AxB

    # Calculo las componentes
    axb_1 = A[1] * B[2] - A[2] * B[1]  # Primer elemento del producto
    axb_2 = A[2] * B[0] - A[0] * B[2]  # Segundo elemento del producto
    axb_3 = A[0] * B[1] - A[1] * B[0]  # Tercer elemento del producto

    # Agrego los elementos al vector
    axb.append(axb_1)
    axb.append(axb_2)
    axb.append(axb_3)

    return axb


A = []
B = []

input_user1 = input('Ingrese vector A en el siguiente formato a,b,c: ')
A1 = input_user1.split(',')

while len(A1) != 3:
    print('El formato de vector no es el requerido, intentalo de nuevo')
    input_user1 = input('Ingrese vector A en el siguiente formato a,b,c: ')
    A1 = input_user1.split(',')

input_user2 = input('Ingrese vector B en el siguiente formato d,e,f: ')
B1 = input_user2.split(',')

while len(B1) != 3:
    print('El formato de vector no es el requerido, intentalo de nuevo')
    input_user2 = input('Ingrese vector A en el siguiente formato d,e,f: ')
    B1 = input_user2.split(',')

for i in A1:
    A.append(float(i))

for i in B1:
    B.append(float(i))

#print(A, B)

print(prod_vect(A, B))
