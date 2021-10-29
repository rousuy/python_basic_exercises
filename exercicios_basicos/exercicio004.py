"""
Faça um programa que leia algo pelo teclado, e mostre na tela o seus tipo primitivo e todas as informações possiveis
sobre ela.
"""
# Reposta:
user_info = input("Digite algo: ")
print(
    f"O tipo primitivo desse valor é: {type(user_info)}\nÉ alfabético: {user_info.isalnum()}"
    f"\nÉ alfanumerico: {user_info.isalpha()}\nÉ um digito: {user_info.isdigit()}\nÉ em minúsculo:"
    f"{user_info.islower()}\n"f"É em maiúsculo: {user_info.isupper()}\nÉ numérico: {user_info.isnumeric()} "
    )
