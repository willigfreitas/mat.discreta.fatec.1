def cifra_de_cesar(texto, chave):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            maiusculo = caractere.isupper()
            caractere = chr(((ord(caractere) - ord('A' if maiusculo else 'a') + chave) % 26) + ord('A' if maiusculo else 'a'))
        resultado += caractere
    return resultado

# Criptografar
mensagem_original = "Matemática Discreta operações reversíveis!"
chave = 3
mensagem_cifrada = cifra_de_cesar(mensagem_original, chave)
print("Mensagem cifrada:", mensagem_cifrada)

# Descriptografar
mensagem_descriptografada = cifra_de_cesar(mensagem_cifrada, -chave)
print("Mensagem descriptografada:", mensagem_descriptografada)
