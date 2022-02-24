'''
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)

    ['Tarefa 01', 'Tarefa 02']
    ['Tarefa 01'] <- Desfazer
    ['Tarefa 01', 'Tarefa 02'] <- Refazer

    input <- Nova tarefa
'''

lista_de_tarefas = []  # Variável que armazena todas a tarefas
garbage = []  # Variável que armazena descartes

'''
1° Passo: Criar menu que apresenta as opções ao usuário:
"(1) - Adicionar tarefa
(2) - Listar tarefas
(3) - Desfazer última ação
(4) - Refazer última ação
BONUS (5) - Salvar afazeres
(0) - Sair"

1.1: Criar também o input da opção do usuário.
'''

print("\n~~~~~~~~~~ LISTA DE TAREFAS ~~~~~~~~~~\n\n")
print("Escolha uma opção:\n(1)\tAdicionar tarefa\n(2)\tListar tarefas\n(3)\tDesfazer última ação\n(4)\tRefazer última ação\n(0)\tSair")

'''
2° Passo: Programar funções (1) a (4).
'''

def adicionar_tarefa(lista):
    tarefa = input('Digite a tarefa: ')
    prazo_final = input('Agora digite o prazo final de conclusão: ')
    lista.append((tarefa, prazo_final))
    return lista

def listar_tarefas(lista):
    print()
    print()
    # Implementar índice
    # Implementar verificação de lista vazia
    for tarefa, prazo in lista:
        print(f'{tarefa}\nPrazo final: {prazo}.')

def desfazer(lista):
    try:
        garbage.append(lista[-1])
        lista.pop()
    except IndexError:
        pass
    return lista

def refazer(lista):
    try:
        lista.append(garbage[-1])
        garbage.pop()
    except IndexError:
        pass
    return lista

def salvar(lista):  # Implementar registro em .txt da lista
    pass

'''
3° Passo: Programar esqueleto do código com condicionais e repetições.
'''

if __name__ == '__main__':

    while True:
        opção_usuário = input('Opção: ')
        if opção_usuário == '1':
            adicionar_tarefa(lista_de_tarefas)
        elif opção_usuário == '2':
            listar_tarefas(lista_de_tarefas)
        elif opção_usuário == '3':
            desfazer(lista_de_tarefas)
        elif opção_usuário == '4':
            refazer(lista_de_tarefas)
        # elif opção_usuário == 5:
        elif opção_usuário == '0':
            break
        else:
            print('\nOpção Inválida.\n')