'''
Os alunos deverão desempenhar as seguintes atividades:
1. Execute e analise a saída do seguinte código no Google Colab1
.
2. Altere o código da atividade 1 para que ele exiba os números múltiplos de 2, 5 e 7 e que 
estejam dentro do intervalo entre 100 e 500 (incluindo o 100 e o 500).
3. Altere o código da atividade 1, criando uma variável divisor e, em seguida, verifique quais os 
números no intervalo entre 0 e 1000 (incluindo o 0 e excluindo o 1000) são múltiplos da 
variável divisor. 
• Por exemplo, se o valor de divisor for igual a 3, todos os números múltiplos de 3, 
dentro do intervalo, deverão ser exibidos (0, 3, 6, 9, ..., 996, 999).
'''

# declaração das variáveis
inicio = 0
fim = 100
# verifica quais números são divisíveis por cinco, e exibe aqueles que são
for numero in range(inicio, fim):
    if numero <= 100 and numero % 5 == 0:
        print(numero)
