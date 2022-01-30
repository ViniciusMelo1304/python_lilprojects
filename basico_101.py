'''
Desafio Básico - Pedir ao usuário que digite o horário e printar 'Bom dia'/'Boa tarde'/'Boa noite' dependendo da hora que ele digitou.

> Importei uma biblioteca que extrai de forma automática o horário, à partir dela criei os if/else.
'''

def saudacao():
    from datetime import datetime

    dia_hora = datetime.today() #.strftime('%H:%M:%S')
    # print(f'{dia_hora.hour:02d}:{dia_hora.minute:02d}:{dia_hora.second:02d}')

    if (dia_hora.hour >= 5 and dia_hora.hour < 12):
        print('Bom dia!')
    elif (dia_hora.hour >= 12 and dia_hora.hour < 18):
        print('Boa tarde!')
    elif ((dia_hora.hour >= 18) or (dia_hora.hour >= 0 and dia_hora.hour < 5)):
        print('Boa noite!')
    else:
        print("\n\nHá algo de errado com o horário...")

'''
Desafio Básico 2 - Pedir ao usuário que digite o seu nome e printar 'Nome curto'/'Nome normal'/'Nome grande' dependendo do tamanho do nome digitado.

> Brinquei um pouco com listas para treinar, conferindo rusticamente se o nome foi digitado da forma correta, à partir disso criei os if/else.
'''

def nomear():
    verificador = True
    nome = input("Digite o seu nome inteiro: ")

    while verificador == True:
        if nome.istitle():
            nome_separado = nome.split()
            if (len(nome) <= 15):
                print(f'{nome_separado[0]}, seu nome é curtinho.')
            elif (len(nome) <= 18):
                print(f'{nome_separado[0]}, seu nome é mediano.')
            elif (len(nome) > 18):
                print(f'Uau {nome_separado[0]}, você tem um nome bem grande.')
            else:
                print("\n\nHá algo de errado com o nome...")
            verificador = False
        else:
            nome = nome.title()
            continue

'''
Desafio Básico 3 - Pedir ao usuário que digite um número, verificar e printar conforme o número digitado se é par ou ímpar.

> Primeiramente verifiquei se o input era um caractere numérico, enquanto não seja, ele repete o programa. Depois verifica a condição pedida.
'''

def parImpar():

    resultado = True

    while resultado == True:
        numero = input("Digite um número inteiro: ")
        if numero.isnumeric():
            if int(numero) % 2 == 0:
                print("\n***O número que você digitou é par!***\n")
                resultado = False
            else:
                print("\n***O número que você digitou é ímpar!***\n")
                resultado = False
        else:
            print("Você não digitou um número decimal...\n")

if __name__ == '__main__':
    saudacao()
    nomear()
    parImpar()

