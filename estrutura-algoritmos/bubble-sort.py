def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # aux = lista[i]
                # lista[i] = lista[i+1]
                # lista[i+1] = aux
                lista[i], lista[i+1] = lista[i+1], lista[i] #troca de elementos de maneira simplificada
    return lista

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", arr)
    print("Lista ordenada (Bubble Sort):", bubble_sort(arr))
