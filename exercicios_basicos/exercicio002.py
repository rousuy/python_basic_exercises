"""
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
"""
# Resposta:
nome = input("Qual é o seu nome? ")
print(f"Seja Bem-Vindo(a) {nome}")  # Formatação em f'strings a partir da versão 3.6 do python (versão mais atual)
print("Seja Bem-Vindo(a) %s" % nome)  # Formatação em versões 2 do python
print("Seja Bem-Vindo(a) {}".format(nome))  # Formatação em versões 3 até 3.5 do python
