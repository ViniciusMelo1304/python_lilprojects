'''
Desafio - Verificar a baixa probabilidade de acertar um jogo na Mega Sena.
'''

def MegaSena():
    sorteio = []
    import random
    while len(sorteio) < 6:
        número = random.randint(1, 60)
        if número not in sorteio:
            sorteio.append(número)
        else:
            pass
        sorteio.sort()
    return sorteio


Jogo = []
numJogos = 0
Jogo_Usuário = [1, 2, 3, 4, 5, 6]

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

print(numJogos)