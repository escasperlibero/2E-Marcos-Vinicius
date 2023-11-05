import random

# Função para gerar um vetor de tamanho 30 com números ímpares aleatórios
def gerar_vetor(tamanho):
    vetor = []
    for _ in range(tamanho):
        numero = random.randint(1, 100)  # Números ímpares entre 1 e 100
        if numero % 2 == 0:
            numero += 1  # Garante que seja ímpar
        vetor.append(numero)
    return vetor

# Função para ordenar o vetor usando o Insertion Sort
def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and chave < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave

# Função para imprimir o vetor
def imprimir_vetor(vetor):
    for numero in vetor:
        print(numero, end=' ')

# Main
tamanho_vetor = 30
vetor_aleatorio = gerar_vetor(tamanho_vetor)

print("Vetor gerado:")
imprimir_vetor(vetor_aleatorio)

insertion_sort(vetor_aleatorio)

print("\nVetor ordenado:")
imprimir_vetor(vetor_aleatorio)
