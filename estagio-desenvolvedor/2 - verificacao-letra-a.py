def contar_a(string):
    contagem_maiuscula = 0
    contagem_minuscula = 0
    
    for char in string:
        if char == 'A':
            contagem_maiuscula += 1
        elif char == 'a':
            contagem_minuscula += 1
    
    if contagem_maiuscula > 0 or contagem_minuscula > 0:
        print(f"A letra 'a' aparece {contagem_minuscula} vez(es) em minúscula e {contagem_maiuscula} vez(es) em maiúscula.")
    else:
        print("A letra 'a' não está presente na string.")

texto = input("Digite uma string: ")
contar_a(texto)