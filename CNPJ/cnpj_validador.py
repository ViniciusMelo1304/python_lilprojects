def trata_entrada(cnpj):
    caracteres = ['/', '-', '.']
    for símbolo in caracteres:
        # Remove os caracteres especiais do input de CNPJ
        cnpj = cnpj.replace(símbolo, '')
    return cnpj


def trata_saida(cnpj_calculado):
    simbolos = ((2, '.'),
                (6, '.'),
                (10, '/'),
                (15, '-'))
    lista_intermediaria = []
    if len(cnpj_calculado) != 14:
        raise ValueError("A entrada deve conter 14 dígitos para ser tratada.")
    else:
        for numero in cnpj_calculado:
            lista_intermediaria.append(numero)
        for tupla in simbolos:
            indice, simbolo = tupla
            lista_intermediaria.insert(indice, simbolo)
        cnpj_calculado = ''.join(lista_intermediaria)
        return cnpj_calculado


def fatiar(cnpj):
    cnpj = trata_entrada(cnpj)
    return cnpj[0:12]  # Retorna só os 12 primeiros dígitos


def calcula_digito1(cnpj):
    cnpj = fatiar(cnpj)
    multiplicador = 5
    soma = 0
    for número in cnpj:
        soma += int(número) * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            multiplicador = 9
    dígito1 = 11 - (soma % 11)
    if dígito1 > 9:
        return 0
    return dígito1


def calcula_digito2(cnpj):
    cnpj = fatiar(cnpj)
    cnpj += str(calcula_digito1(cnpj))
    multiplicador = 6
    soma = 0
    for número in cnpj:
        soma += int(número) * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            multiplicador = 9
    dígito2 = 11 - (soma % 11)
    if dígito2 > 9:
        return 0
    return dígito2


def calcula_digitos(cnpj):
    cnpj = fatiar(cnpj)
    cnpj += str(calcula_digito1(cnpj))
    cnpj += str(calcula_digito2(cnpj))
    return cnpj


def verifica_cpnj(cnpj_digitado):
    cnpj_calculado = calcula_digitos(cnpj_digitado)
    print(f'\nCNPJ digitado:\t{cnpj_digitado}')
    print(f'\nCNPJ calculado:\t{trata_saida(cnpj_calculado)}')
    if trata_entrada(cnpj_digitado) == cnpj_calculado:
        print('\nVálido.\n')
    else:
        print('\nInválido.\n')
