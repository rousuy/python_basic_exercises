"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma áre de 2m quadrados.
"""
# Resposta:
entrada = input("Digite o valor da altura e largura: ").split()
alt = float(entrada[0])
large = float(entrada[1])
area = alt * large
print(f'A área da sua parede é de {area}m\nPara pintar sua parede serão necessários {(alt * large) / 2}l de tinta')
