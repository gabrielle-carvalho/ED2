class HashLinear:
    def __init__(self, tam =8):
        self.tam=tam
        self.lista=[None] * tam

    def hash(self, num):
        return num % self.tam

    def insert(self, num):
        pos = self.hash(num)
        for step in range(self.tam):
            i = (pos+1) % self.tam # procura prox pos livre, usando % ele volta ao indice 0 se a lista acabar
            if self.lista[i] is None: # se a posicao que quer esta livre, basta add
                self.lista[i] = num
                return
        print("Tabela cheia, nao e possivel add", num)

    def __str__(self): #retorna na visualizacao q a gnt ta acostumado
        return str(self.lista)
    
def main():
    h = HashLinear(8)

    valores = [10, 18, 26, 5, 13, 21, 29]
    for v in valores:
        print(f"Inserindo {v}...")
        h.insert(v)
        print("Tabela atual:", h)

    print("\ntabela final:")
    print(h)


if __name__ == "__main__":
    main()
