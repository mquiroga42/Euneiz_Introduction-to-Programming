import random

def generar_numero_con_letras():
    numero_aleatorio = [str(random.randint(0, 9)) for _ in range(8)]
    
    num_letras = random.randint(1, 2)
    indices = random.sample(range(6), num_letras)

    for index in indices:
        numero_aleatorio[index] = random.choice('ABCDEF')

    return ''.join(numero_aleatorio) + str(random.randint(0, 9))

with open('hex.txt', 'w') as archivo:
    for _ in range(1):
        b8270 = 'B8270'
        e0_f0 = random.choice(['E0', 'F0'])
        numletter = generar_numero_con_letras()
        lista_elemento = f'{b8270}{e0_f0}{numletter}'
        archivo.write(lista_elemento + '\n')
