# Implemente o Quicksort usando o primeiro elemento como pivô; 
# Reimplemente o Quicksort usando o elemento do meio como pivô; 
# Implemente o Shellsort ou Heapsort; 
# Compare os desempenhos (tempo de execução) das implementações.

import time
import pandas as pd

dados = pd.read_csv("ai_assistant_usage_student_life.csv")

print("Visualização inicial dos dados:")
print(dados.head())

def quick_sort_start(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:  # só ordena se a sublista tiver 2 ou mais elementos
        p = partition_start(lista, inicio, fim)  # particiona a sublista e obtém índice final do pivô
        quick_sort_start(lista, inicio, p - 1) 
        quick_sort_start(lista, p + 1, fim)

def partition_start(lista, inicio, fim):
    pivot = lista[inicio]  # pivô escolhido como primeiro elemento
    i = inicio + 1  # i aponta para o primeiro elemento após o pivô (procura elementos > pivô)
    j = fim  # j aponta para o final da sublista (procura elementos < pivô)

    while True:
        while i <= j and lista[i] <= pivot:
            i += 1
        while i <= j and lista[j] >= pivot:
            j -= 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
        else:
            break
    lista[inicio], lista[j] = lista[j], lista[inicio]
    return j

def quick_sort_middle(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition_middle(lista, inicio, fim)
        quick_sort_middle(lista, inicio, p - 1)
        quick_sort_middle(lista, p + 1, fim)

def partition_middle(lista, inicio, fim):
    meio = (inicio + fim) // 2    
    lista[meio], lista[inicio] = lista[inicio], lista[meio]  # coloca pivô no início
    return partition_start(lista, inicio, fim)

def shell_sort(lista):
    n = len(lista)
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            aux = lista[i]
            j = i
            while j >= intervalo and lista[j-intervalo] > aux:
                lista[j] = lista[j-intervalo]
                j-= intervalo
            lista[j] = aux
        intervalo //=2 #divide pela metade o intervalo

coluna = dados.select_dtypes(include=["number"]).iloc[:,0]  # pegar a 1ª coluna numérica
lista_original = coluna.dropna().astype(float).tolist()

for metodo, func in [
    ("QuickSort pivô no início", quick_sort_start),
    ("QuickSort pivô no meio", quick_sort_middle),
    ("ShellSort", shell_sort)
]:
    lista = lista_original.copy()
    inicio = time.time()
    func(lista)
    fim = time.time()
    print(f"{metodo}: {fim - inicio:.6f} segundos")