'''
Desafio - Criar um verificador da Teoria das Probabilidades, assim como provar que as probabilidades empíricas se aproximam das teóricas conforme o espaço amostral tende ao infinito.
'''

def Dado():
    import random
    dado = random.randint(1, 6)
    return dado


print()

# Define quantas vezes o dado será 'lançado'
limite = int(input('Quantas vezes você quer lançar o dado?\n'))
frequencias = [0 for i in range(6)]
probabilidades = [0 for i in range(6)]


# Lança o dados 'limite' vezes e armazena as frequências
for lançamento in range(limite):
    dado = Dado()  # 'Lança' o dado
    for index, _ in enumerate(frequencias):
        if dado-1 == index:
            frequencias[index] += 1
            continue

print()

# Calcula as probabilidades e imprime as frequências
for indice, frequencia in enumerate(frequencias):
    probabilidades[indice] = frequencia/limite
    print(f'Face {indice + 1}:\t{frequencia:02}x')

print()

# Imprime as probabilidades
for indice, probabilidade in enumerate(probabilidades):
    print(f'Prob {indice + 1}:\t{probabilidade:2.2%}')
