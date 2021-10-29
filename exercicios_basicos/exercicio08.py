"""
Escreva um programa que leia um valor, e o exiba convertido em centímetros e milímetros.
"""
# Resposta:
num = int(input("Digite um número em metros: "))
print(
    f"O valor digitado foi {num} metros\nO seu valor em centímetros é {num * 100:.2f}cm\nO seu valor em milímetros é "
    f"{num * 1000:.2f}mm"
    )
