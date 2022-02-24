'''Desafio: fazer um quiz utilizando de dicionários.'''

print('\n***** QUIZ DE CONHECIMENTOS GERAIS *****\n')

Perguntas ={
    'Pergunta 1':
    {
        'pergunta':'Quem descobriu o Brasil?',
        'respostas':{'a':'Pedro Álvares Cabral',
                     'b':'Cristóvão Colombo',
                     'c':'Pero Vaz de Caminha',
                     'd':'Dom João VI',
                     'e':'Carlota Joaquina',},
        'resposta_certa':'a',
    },
    'Pergunta 2':
    {
        'pergunta':'Quanto é 12x21?',
        'respostas':{'a':'218',
                     'b':'252',
                     'c':'240',
                     'd':'282',
                     'e':'262',},
        'resposta_certa':'b',
    },
    'Pergunta 3':
    {
        'pergunta':'Quantas UF (Unidade Federativa) existem no Brasil?',
        'respostas':{'a':'24',
                     'b':'26',
                     'c':'28',
                     'd':'27',
                     'e':'21',},
        'resposta_certa':'d',
    },
    'Pergunta 4':
    {
        'pergunta':'O prefixo "pneumo" dá à palavra significado de:',
        'respostas':{'a':'Ar',
                     'b':'Fogo',
                     'c':'Asa',
                     'd':'Voo',
                     'e':'Pulmão',},
        'resposta_certa':'e',
    },
}

acertos = 0

for perguntas_keys, perguntas_values in Perguntas.items():
    print(f'{perguntas_keys.upper()}\n{perguntas_values["pergunta"]}\n')
    for respostas_keys, respostas_values in perguntas_values['respostas'].items():
        print(f'({respostas_keys})  {respostas_values}')

    while True:
        resposta_usuário = input('Sua resposta: ')
        if resposta_usuário.lower() in perguntas_values['respostas'].keys():
            break
        else:
            print('\nVocê tem que digitar uma das opções apresentadas.\n')

    if resposta_usuário.lower() == perguntas_values['resposta_certa']:
        print('Você ACERTOU!')
        acertos += 1
    else:
        print('Você errou...')
    print()

qnt_perguntas = len(Perguntas)
porcentagem_acertos = acertos / qnt_perguntas

print(f'\nVocê acertou {acertos} de {qnt_perguntas}.\n')
print(f'\nSua nota foi {porcentagem_acertos:0.2%}.\n')

if porcentagem_acertos == 1:
    print('\n\nTemos um gêniozinho aqui...\nVocê GABARITOU!!! PARABÉNS\n')
elif porcentagem_acertos >= 0.8:
    print('\n\nVocê foi muito bem. Parabéns!\n')
elif porcentagem_acertos >= 0.5:
    print('\n\nVocê está acima da média, mas precisa estudar mais...\n')
elif porcentagem_acertos >= 0.3:
    print('\n\nVocê teve um desempenho abaixo da média...\n')
else:
    print(
        '\n\nCuidado, você tem errado conhecimentos básicos demais...\nAconselho pegar mais firme nos estudos...\n')