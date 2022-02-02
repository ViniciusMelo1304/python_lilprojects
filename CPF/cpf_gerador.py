def nove_digitos():
    lista = []
    cpf = ''
    import random
    while len(lista) < 9:
        número = random.randint(0, 9)
        lista.append(número)
    for digito in lista:
        cpf += str(digito)
    return cpf

def gerar_cpf(cpf_calculo):

    soma1 = soma2 = 0

    for índice, r in enumerate(range(10, 1, -1)):
        # print(f'{int(cpf_calculo[índice])} * {r} \t= {int(cpf_calculo[índice]) * r}')
        soma1 += int(cpf_calculo[índice]) * r

    if (11 - (soma1 % 11) > 9):
        digito_10 = 0
    else:
        digito_10 = 11 - (soma1 % 11)

    cpf_calculo += str(digito_10)


    for índice, r in enumerate(range(11, 1, -1)):
        # print(f'{int(cpf_calculo[índice])} * {r} \t= {int(cpf_calculo[índice]) * r}')
        soma2 += int(cpf_calculo[índice]) * r

    if (11 - (soma2 % 11) > 9):
        digito_11 = 0
    else:
        digito_11 = 11 - (soma2 % 11)

    cpf_calculo += str(digito_11)

    print(f'\nCPF CALCULADO:\t {cpf_calculo}\n')

    return cpf_calculo

# digitos = nove_digitos()

cpf_final = gerar_cpf(nove_digitos())
