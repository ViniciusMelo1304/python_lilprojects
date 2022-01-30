'''Desafio: Criar um Jogo da Forca.'''

# Passo EXTRA: Importar saudação
# Passo 1: Criar lista que contém palavras a serem descobertas
# Passo 2: Randomicamente escolher da lista e comunicar ao usuário quantas letras a palavra tem
# Passo 3: Criar input do usuário
# Passo 3.1: Armazenar o input do usuário, verificando se bate com alguma letra da palavra secreta
# Passo 4: Mostrar ao usuário, caso acerte, onde a letra se encaixa
# Passo 5: Determinar número de tentativas do usuário.
# Passo 6: Fazer o Game Over e a Vitória

import random
from basico_101 import saudacao

def categorizar(dicionario):
    categorias = []
    for chave in dicionario:
        categorias.append(chave)
    return categorias

def acessar(chave, dicionario):
    return chave, dicionario[chave]

saudacao()

lista_Secretas = {
'Alimento':         ['abobora', 'tomate', 'abacaxi', 'melancia', 'banana', 'uva', 'caqui', 'laranja', 'jaca',
                     'mexerica', 'pizza', 'poke'],
'Objeto':           ['teclado','tapete', 'mesa', 'computador', 'bancada', 'cadeira', 'travesseiro', 'camiseta',
                     'camisa', 'casaco', 'jaqueta', 'blusa', 'telhado', 'parede', 'ventilador', 'medalha', 'celular', 'pasta', 'pente', 'telefone', 'modem', 'fio', 'monitor', 'microfone', 'gabinete', 'copo', 'tigela', 'mouse', 'mousepad', 'notebook', 'caneta', 'baralho', 'garrafa', 'diploma'],
'Partes do Corpo':  ['olho', 'nariz', 'ouvido', 'cabelo', 'unha', 'dente', 'lingua', 'joelho', 'ombro',
                     'aracnoide', 'duramater', 'perna', 'bulbo'],
'Profissão':        ['otorrinolaringologista', 'cardiologista', 'ortopedista', 'dentista', 'mecanico', 'presa',
                     'lojista', 'reporter', 'chef', 'jornalista', 'engenheiro', 'cabeleireiro', 'programador'],
'Carro':            ['Corsa', 'Meriva', 'Lamborghini', 'Monza', 'Opala', 'Impala', 'Chevette', 'Corvette', 'Ferrari',
                     'Jaguar', 'Porsche', 'Onix'],
'Animal':           ['veado', 'corsa', 'cachorro', 'gato', 'lince', 'pombo', 'guepardo', 'javali', 'suricato', 'girafa', 'rinoceronte',
                     'tucano', 'arara', 'barata', 'formiga', 'rato', 'hamster', 'pato', 'sapo', 'pernilongo', 'abelha', 'emu', 'ema', 'avestruz', 'dodo'],
'País':             ['Brasil', 'Suriname', 'Mexico', 'Alemanha', 'Italia', 'Turquia', 'Inglaterra', 'India', 'China',
                     'Tailandia', 'Indonesia', 'Laos', 'Togo', 'Chipre', 'Gana', 'Congo', 'Egito', 'Nigeria', 'Argelia', 'Angola'],
'Nome':             ['Giovanni', 'Fernando', 'Vinicius']
}

chaves = categorizar(lista_Secretas)
chave_aleatoria, lista_aleatoria = acessar(chaves[random.randrange(len(chaves))], lista_Secretas)
segredo = lista_aleatoria[random.randrange(len(lista_aleatoria))].upper()

tentativas = 6

# print(f'{chaves}\n')  # Mostra as categorias
print(f'\nCategoria: {chave_aleatoria.upper()}.\n\nA palavra secreta tem {len(segredo)} letras.\n\nVocê tem {tentativas} tentativas.\n')


digitadas = []


while True:

    letra = input(
        "\nDigite uma letra ou tente a palavra inteira (custa duas tentativas): ").upper()

    if not letra.isdecimal() and len(letra) == 1:
        if letra in segredo:
            digitadas.append(letra)
        else:
            tentativas -= 1
            if tentativas == 0:
                print(
                    f'\nInfelizmente, suas tentativas acabaram.\nA palavra era {segredo}.\n\n***************GAME OVER***************\n')
                break
            print(f"Você errou... Ainda restam {tentativas} tentativas.")
            continue
    else:
        if not letra.isdecimal() and letra == segredo:
            print(
                f'\nCARACA, QUE PALPITE CERTEIRO!\nA palavra secreta era {segredo}.\n\n')
            break
        elif letra.isdecimal():
            print(f"\n***Digite apenas UMA LETRA***\n")
        else:
            tentativas -= 2
            print(
                f"\nA palavra secreta não é essa... Restam {tentativas} tentativas.\n")
            if tentativas == 0:
                break
        continue

    palavra_secreta = ''

    for letra_secreta in segredo:
        if letra_secreta in digitadas:
            palavra_secreta += letra_secreta
        else:
            palavra_secreta += '*'
    print(palavra_secreta)

    if palavra_secreta == segredo:
        print(
            f'\nPARABÉNS, VOCÊ GANHOU!\nA palavra secreta era {segredo}.\n\n')
        break
