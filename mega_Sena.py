'''
Desafio - Verificar a baixa probabilidade de acertar um jogo na Mega Sena.
'''

import time
import pandas as pd

def MegaSena():
    sorteio = []
    import random
    while len(sorteio) < 6:
        número = random.randint(1, 60)
        if número not in sorteio:
            sorteio.append(número)
        sorteio.sort()
    return sorteio


tempo_inicial = time.time()  # em segundos

Jogo = []
numJogos = 0
Jogo_Usuário = MegaSena()
print(Jogo_Usuário)

'''
Caso o usuário queira digitar um jogo específico, descomentar esta parte e comentar a variável Jogo_Usuário acima.

Jogo_Usuário = []
for num_aposta in range(1,7):
    x = int(input(f"Insira o {num_aposta}° número: "))
    Jogo_Usuário.append(x)
'''

while Jogo_Usuário != Jogo:
    Jogo = MegaSena()
    numJogos += 1

tempo_final = time.time()  # em segundos
tupla = (Jogo_Usuário, numJogos, tempo_final-tempo_inicial)

print(tupla)



print(f"O programa demorou {tempo_final - tempo_inicial:0f} segundos para encontrar um jogo, de forma randômica, que fosse equivalente ao do usuário.")
print(numJogos)

# tabela.to_excel(r"C:\Users\Vinicius\Desktop\Aula 3 - Intensivão de Python\Produtos Novo.xlsx",
                # sheet_name="Nova DB", index=False)