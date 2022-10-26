'''

Solução dos Exercícios do Módulo 1 - Python


Os alunos deverão desempenhar as seguintes atividades:
1. Execute e analise a saída do seguinte código no Google Colab1

'''

# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero % 5 == 0:
        print(numero)


'''
2. Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 e que estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500).
'''

inicio = 100
fim = 500

for numero in range(inicio, fim + 1):
    if (numero % 2 == 0 or numero % 5 == 0 or numero % 7 == 0):
        print(numero)

'''
3. Altere o código da atividade 1, criando uma variável divisor e, em seguida, verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e excluindo o 1000) são múltiplos da variável divisor.
• Por exemplo, se o valor de divisor for igual a 3, todos os números múltiplos de 3, dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).
'''

divisor = 3
inicio = 0
fim = 1000

for numero in range(inicio, fim + 1):
    if (numero % divisor == 0):
        print(numero)

'''
4. Crie um código declarando as seguintes variáveis do tipo string:
'''

nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

'''
Em seguida, realize as seguintes transformações nas variáveis:

• Transforme todos os caracteres das variáveis em maiúsculo;
• Transforme todos os caracteres das variáveis em minúsculo;
• Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
• Exiba o número de caracteres de cada variável;
• Remova os pontos (.) e o hífen (–) da variável cpf.

'''

# • Transforme todos os caracteres das variáveis em maiúsculo;
print(nome.upper(), cidade.upper())

# • Transforme todos os caracteres das variáveis em minúsculo
print(nome.lower(), cidade.lower())

# • Exiba o número de caracteres de cada variável;
print(len(cpf), len(nome), len(cidade))

# • Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
letra = 'ã'
findCidade = cidade.find(letra)
findNome = nome.find(letra)
findCPF = cpf.find(letra)

if findCidade >= 0:
    posicao = findCidade
    print(f"A letra '{letra}' está na posição {posicao} da palavra {cidade}")
else:
    print(f"A letra '{letra}' não existe em {cidade}")
if findNome >= 0:
    posicao = findNome
    print(f"A letra '{letra}' está na posição {posicao} da palavra {nome}")
else:
    print(f"A letra '{letra}' não existe em {nome}")
if findCPF >= 0:
    posicao = findCPF
    print(f"A letra '{letra}' está na posição {posicao} da palavra {cpf}")
else:
    print(f"A letra '{letra}' não existe em {cpf}")

# • Remova os pontos (.) e o hífen (–) da variável cpf.
cpf = (cpf.replace('-', ''))
cpf = (cpf.replace('.', ''))
print(cpf)


# Teste
value = (2 + 3) * 5 - 1
print(value)

# Teste 2
print(int(cpf))

# Teste 3
print(True and False)
print(False or True)

#
numero = '127957'
numero = int(numero) + 1.0
print(type(numero))
print(numero)
