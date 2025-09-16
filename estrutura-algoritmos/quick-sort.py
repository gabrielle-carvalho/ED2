def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quick_sort(lista, inicio, p - 1)
        quick_sort(lista, p + 1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]  # pivô escolhido como último elemento
    i = inicio           # limite dos elementos menores que o pivô
    
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print("Lista original:", arr)
    quick_sort(arr)
    print("Lista ordenada (Quick Sort):", arr)
