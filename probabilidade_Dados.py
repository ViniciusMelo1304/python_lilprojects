'''
Desafio - Criar um verificador da Teoria das Probabilidades, assim como provar que as probabilidades empíricas se aproximam das teóricas conforme o espaço amostral tende ao infinito.
'''

def Dado():
    import random
    dado = random.randint(1, 6)
    return dado


contagem = 0
resultado = []
d1 = d2 = d3 = d4 = d5 = d6 = 0

while contagem < 10000000:  # Define quantas vezes o dado será 'lançado'
    resultado.append(Dado())  # Adiciona o resultado do dado à uma lista
    contagem += 1

for dado in range(len(resultado)):  # Calcula a soma dos resultados de cada face
    if resultado[dado] == 1:
        d1 += 1
    elif resultado[dado] == 2:
        d2 += 1
    elif resultado[dado] == 3:
        d3 += 1
    elif resultado[dado] == 4:
        d4 += 1
    elif resultado[dado] == 5:
        d5 += 1
    else:
        d6 += 1

prob1 = d1/len(resultado)  # Calcula as probabilidades
prob2 = d2/len(resultado)
prob3 = d3/len(resultado)
prob4 = d4/len(resultado)
prob5 = d5/len(resultado)
prob6 = d6/len(resultado)

print("1: {} vezes.\n2: {} vezes.\n3: {} vezes.\n4: {} vezes.\n5: {} vezes.\n6: {} vezes.\n".format(
    d1, d2, d3, d4, d5, d6))  # Mostra quantas vezes cada dado foi lançado
print("Prob1: {}.\nProb2: {}.\nProb3: {}.\nProb4: {}.\nProb5: {}.\nProb6: {}.\n".format(
    prob1, prob2, prob3, prob4, prob5, prob6))  # Mostra a probabilidade de cada face do dado