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
# import pandas as pd

saudacao()

# lista_palavras = pd.read_csv(r'C:\Users\Vinicius\Desktop\br-sem-acentos.csv')

lista_Secretas = ['abobora', 'tomate', 'abacaxi', 'melancia', 'banana', 'uva', 'caqui', 'laranja', 'jaca', 'mexerica', 'pizza', 'poke',
                  'teclado', 'tapete', 'mesa', 'computador', 'bancada', 'cadeira', 'travesseiro', 'camiseta', 'camisa', 'casaco', 'jaqueta', 'blusa', 'telhado', 'parede', 'ventilador', 'medalha', 'bulbo', 'celular', 'pasta', 'pente', 'telefone', 'modem', 'fio', 'monitor', 'microfone', 'gabinete', 'copo', 'tigela', 'mouse', 'mousepad', 'notebook', 'caneta', 'baralho', 'garrafa', 'diploma', 'olho', 'nariz', 'ouvido', 'cabelo', 'unha', 'dente', 'lingua', 'joelho', 'ombro', 'aracnoide', 'duramater', 'perna', 'otorrinolaringologista', 'cardiologista', 'ortopedista', 'dentista', 'mecanico', 'presa', 'lojista', 'reporter', 'chef', 'jornalista', 'engenheiro', 'cabeleireiro', 'programador',
                  'meriva', 'lamborghini', 'monza', 'opala', 'impala', 'chevette', 'corvette', 'ferrari', 'jaguar', 'porsche', 'onix', 'veado', 'corsa', 'cachorro', 'gato', 'lince', 'pombo', 'guepardo', 'javali', 'suricato', 'girafa', 'rinoceronte', 'tucano', 'arara', 'barata', 'formiga', 'rato', 'hamster', 'pato', 'sapo', 'pernilongo', 'abelha', 'emu', 'ema', 'avestruz', 'dodo', 'brasil', 'suriname', 'mexico', 'alemanha', 'italia', 'turquia', 'inglaterra', 'india', 'china', 'tailandia', 'indonesia', 'laos', 'togo', 'chipre', 'gana', 'congo', 'egito', 'nigeria', 'argelia', 'angola', 'giovanni', 'fernando', 'vinicius']
# lista_Secretas = {
# 'Alimento': ['abobora', 'tomate', 'abacaxi', 'melancia', 'banana', 'uva', 'caqui', 'laranja', 'jaca', 'mexerica', 'pizza', 'poke'],
# 'Objeto': ['teclado','tapete', 'mesa', 'computador', 'bancada', 'cadeira', 'travesseiro', 'camiseta', 'camisa', 'casaco', 'jaqueta', 'blusa', 'telhado', 'parede', 'ventilador', 'medalha', 'bulbo', 'celular', 'pasta', 'pente', 'telefone', 'modem', 'fio', 'monitor', 'microfone', 'gabinete', 'copo', 'tigela', 'mouse', 'mousepad', 'notebook', 'caneta', 'baralho', 'garrafa', 'diploma'],
# 'Partes do Corpo': ['olho', 'nariz', 'ouvido', 'cabelo', 'unha', 'dente', 'lingua', 'joelho', 'ombro', 'aracnoide', 'duramater', 'perna'],
# 'Profissão': ['otorrinolaringologista', 'cardiologista', 'ortopedista', 'dentista', 'mecanico', 'presa', 'lojista', 'reporter', 'chef', 'jornalista', 'engenheiro', 'cabeleireiro', 'programador'],
# 'Carro': ['Corsa', 'Meriva', 'Lamborghini', 'Monza', 'Opala', 'Impala', 'Chevette', 'Corvette', 'Ferrari', 'Jaguar', 'Porsche', 'Onix'], 'Animal': ['veado', 'corsa', 'cachorro', 'gato', 'lince', 'pombo', 'guepardo', 'javali', 'suricato', 'girafa', 'rinoceronte', 'tucano', 'arara', 'barata', 'formiga', 'rato', 'hamster', 'pato', 'sapo', 'pernilongo', 'abelha', 'emu', 'ema', 'avestruz', 'dodo'],
# 'País': ['Brasil', 'Suriname', 'Mexico', 'Alemanha', 'Italia', 'Turquia', 'Inglaterra', 'India', 'China', 'Tailandia', 'Indonesia', 'Laos', 'Togo', 'Chipre', 'Gana', 'Congo', 'Egito', 'Nigeria', 'Argelia', 'Angola'],
# 'Nome': ['Giovanni', 'Fernando', 'Vinicius']
# }

tentativas = 6
# print(lista_palavras)
# print(len(lista_Secretas))
# segredo = lista_palavras[random.randrange(100)]
segredo = lista_Secretas[random.randint(-len(lista_Secretas), -1)]
print(
    f'\nA palavra secreta tem {len(segredo)} letras.\nVocê tem {tentativas} tentativas.\n\n')


digitadas = []


while True:

    letra = input(
        "\nDigite uma letra ou tente a palavra inteira (custa duas tentativas): ")

    if not letra.isdecimal() and len(letra) == 1:
        if letra in segredo:
            digitadas.append(letra)
        else:
            tentativas -= 1
            if tentativas == 0:
                print(
                    f'\nInfelizmente, suas tentativas acabaram.\nA palavra era {segredo.upper()}.\n\n***************GAME OVER***************\n')
                break
            print(f"Você errou... Ainda restam {tentativas} tentativas.")
            continue
    else:
        if not letra.isdecimal() and letra == segredo:
            print(
                f'\nCARACA, QUE PALPITE CERTEIRO!\nA palavra secreta era {segredo.upper()}.\n\n')
            break
        elif letra.isdecimal():
            print(f"\n***Digite apenas UMA LETRA***\n")
        else:
            tentativas -= 2
            print(
                f"\nNão é essa a palavra... Restam {tentativas} tentativas.\n")
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
            f'\nPARABÉNS, VOCÊ GANHOU!\nA palavra secreta era {segredo.upper()}.\n\n')
        break
