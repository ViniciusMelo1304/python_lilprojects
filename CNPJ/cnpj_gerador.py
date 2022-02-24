from random import randint
from cnpj_validador import calcula_digitos, trata_saida

def gera_cnpj():
    cnpj = ''
    for digito in range(8):
        digito = randint(0, 9)
        cnpj += str(digito)
    else:
        cnpj += '0001'
    cnpj = calcula_digitos(cnpj)
    cnpj = trata_saida(cnpj)

    return cnpj

