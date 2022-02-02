'''SOLUÇÃO 1 - CONTANDO UTILIZANDO UMA LISTA'''
# lista = ['Aoba','eu','sou','Goku','bão?', 1, 2, 3, 4, 6, 7]

# contador_regressivo = len(lista)
# for contador_progressivo, _ in enumerate(lista):
#     contador_regressivo -= 1
#     print(contador_progressivo, contador_regressivo)
#     if contador_progressivo == 8:
#         break

'''SOLUÇÃO 2 - Utilizando While'''
# contador_progressivo = 0
# contador_regressivo = 10
# while contador_progressivo < 9:
#     print(contador_progressivo, contador_regressivo)
#     contador_progressivo += 1
#     contador_regressivo -= 1

'''SOLUÇÃO 3 - Utilizando For'''

# for c_p, c_r in enumerate(range(10, 1, -1)):
#     print(c_p, c_r)

'''SOLUÇÃO 4 - Utilizando Funções'''
def contar(inicio, final, modo):
    if modo == 1:
        for _, c_r in enumerate(range(inicio, final, -1)):
            print(c_r)
    elif modo == 0:
        for c_p, _ in enumerate(range(inicio, final, -1)):
            print(c_p)
    else:
        print('MODO INVÁLIDO! DIGITE 0 PARA CONTAGEM PROGRESSIVA OU 1 PARA CONTAGEM REGRESSIVA.')

if __name__ == '__main__':
    contar(10,1,1)