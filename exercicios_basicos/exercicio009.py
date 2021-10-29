"""
Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
# Resposta:
num = int(input("Digite um número: "))
print(
    f"{' Tabuada ':=^20}\n"
    f"{num:>4}  x  1  =  {num * 1}\n{num:>4}  x  2  =  {num * 2}\n{num:>4}  x  3  =  {num * 3}\n{num:>4}  x  4  =  "
    f"{num * 4}\n{num:>4}  x  5  =  {num * 5}\n{num:>4}  x  6  =  {num * 6}\n{num:>4}  x  7  =  {num * 7}\n{num:>4}  "
    f"x  8  =  {num * 8}\n{num:>4}  x  9  =  {num * 9}\n{num:>4}  x  10 =  {num * 10}\n"
    f'{" Fim ":=^20}'
    )
