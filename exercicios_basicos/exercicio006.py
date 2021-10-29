"""
Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
# Resposta:
num = int(int(input("Digite um número: ")))
print(
    f"O número digitado foi: {num}\nO seu dobro é {num * 2}\nO seu triplo é {num * 3}\nA sua raiz quadra é "
    f"{num ** (1/2):.2f}"
    )
