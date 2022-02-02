# cpf = '451.641.528-35' # Problema 1 - input de CPF só aceita números
# cpf = '45164152835'
cpf = '34210639583'
cpf_calculo = cpf[0:9]
soma1 = soma2 = 0

# digitos_cpf = cpf.split('.')
# trim_cpf = cpf.split('-')
# trim_cpf.pop(1)
# digitos_cpf = trim_cpf[0].split('.')
# cpf_calculo = ''
# for conjunto_numeros in digitos_cpf:
#     cpf_calculo += conjunto_numeros
# print(cpf_calculo)

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

if cpf == cpf_calculo:
    print(f'\nCPF digitado:\t {cpf}\nCPF calculado:\t {cpf_calculo}\n\nVÁLIDO.')
else:
    print(f'\nCPF digitado:\t {cpf}\nCPF calculado:\t {cpf_calculo}\n\nINVÁLIDO.')