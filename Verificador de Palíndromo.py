def eh_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_formatado = texto.replace(" ", "").lower()
    # Verifica se é igual ao reverso
    return texto_formatado == texto_formatado[::-1]

# Programa principal
entrada = input("Digite uma frase: ")

if eh_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
