def shell_sort(lista):
    n = len(lista)
    intervalo = n // 2  # intervalo inicial

    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = temp
        intervalo //= 2  # intervalo reduzido

    return lista

if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print("Lista original:", arr)
    shell_sort(arr)
    print("Lista ordenada:", arr)
