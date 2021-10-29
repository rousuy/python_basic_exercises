"""
Construa um algorítimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
# Resposta:
salario = float(input('Digite o valor do salário do funcionário: R$'))
aumento = (salario * 15) / 100
print(
    f'O funcionário recebe atualmente R${salario:.2f}\nCom um novo aumento de 15%, passará a receber R$'
    f'{salario + aumento:.2f}.'
    )
