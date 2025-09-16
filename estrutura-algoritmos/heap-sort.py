def heapify(lista, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] > lista[maior]: # verifica se o filho da esquerda é maior que a raiz
        maior = esquerda

    if direita < n and lista[direita] > lista[maior]: # verifica se o filho da direita é maior que o maior até agora
        maior = direita

    if maior != i: # se o maior não for a raiz, troca e continua o heapify
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)

def heap_sort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):    # construir um heap máximo
        heapify(lista, n, i)
        
    for i in range(n - 1, 0, -1):    # extrair os elementos do heap
        lista[0], lista[i] = lista[i], lista[0]  # troca
        heapify(lista, i, 0)

    return lista

if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print("Lista original:", arr)
    heap_sort(arr)
    print("Lista ordenada (Heap Sort):", arr)
