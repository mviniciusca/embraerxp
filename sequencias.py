palavra = 'araraquara'
contador_a = 0
contador_r = 0

for letra in palavra:
    if letra == 'r':
        contador_r = contador_r + 1
    if letra == 'a':
        contador_a = contador_a + 1
print(
    f"A palavra {palavra} tem {contador_a} letras 'a' e {contador_r} letras 'r'")
