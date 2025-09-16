# procura o menor ou maior elemento da lista
# o menor valor vai ser o primeiro elemento da lista, troca com quem esta como primeiro na posicao da lista
# vai seguindo com essa troca ate o final


def selection_sort(lista):
    n = len(lista)
    for j in range(n-1): # passear pelo array
        min_index = j

        for i in range(j+1, n):
            if lista[i] < lista[min_index]:
                min_index = i

        if lista[j] > lista[min_index]:
        # if min_index != j:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

    return lista


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Lista original:", arr)
    print("Lista ordenada (Selection Sort):", selection_sort(arr))