def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j-1
        if j + 1 != i:
            lista[j+1] = chave
    return lista

if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print("Lista original:", arr)
    insertion_sort(arr)
    print("Lista ordenada (Insertion Sort):", arr)
    