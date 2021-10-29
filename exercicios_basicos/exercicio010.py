"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere: U$1,00 = R$3,27.
"""
# Resposta:
reais = float(input('Quantos você tem em sua carteira? '))
print(f'Você tem {reais:.2f} Reais\nVocê pode comprar {reais / 3.27:.2f} Dólares.')
