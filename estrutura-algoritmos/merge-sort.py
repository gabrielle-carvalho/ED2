def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)

    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista[k] = right[j]
            j += 1
        elif j >= len(right):
            lista[k] = left[i]
            i += 1
        elif left[i] < right[j]:
            lista[k] = left[i]
            i += 1
        else:
            lista[k] = right[j]
            j += 1

if __name__ == "__main__":
    arr = [7, 5, 1, 8, 3]
    print("Lista original:", arr)
    merge_sort(arr)
    print("Lista ordenada (Merge Sort):", arr)
