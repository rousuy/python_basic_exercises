"""
Construa um algorítimo que leia o preço de um produto, e mostre seu novo preço, com 5% de desconto.
"""
# Resposta:
preco = float(input('Digite o preço do produto: R$'))
desconto = (preco * 5) / 100
print(f'Seu produto custa R${preco:.2f}\nCom 5% de desconto, seu produto custará R${preco - desconto:.2f}.')
