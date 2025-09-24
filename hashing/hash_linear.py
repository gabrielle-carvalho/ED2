class HashLinear:
    def __init__(self, tam=8):
        self.tam = tam
        self.lista = [None] * tam

    def hash(self, chave):
        return chave % self.tam  # endereço de base

    def insert(self, chave):
        base = self.hash(chave)
        if self.lista[base] is None:  # posição livre
            self.lista[base] = chave
            return

        if self.lista[base] == chave:  # duplicado
            print(f"chave {chave} duplicada")
            return

        deslocamento = chave // self.tam
        pos = base

        while True:
            pos = (pos + deslocamento) % self.tam
            if self.lista[pos] is None:  # achou posição livre
                self.lista[pos] = chave
                return
            if self.lista[pos] == chave:  # duplicado
                print(f"chave {chave} duplicada")
                return
            if pos == base:  # deu a volta e não achou espaço
                print(f"tabela cheia, não é possível adicionar {chave}")
                return

    def __str__(self):
        return str(self.lista)


def main():
    h = HashLinear(8)
    valores = [10, 18, 26, 5, 13, 21, 29]
    for v in valores:
        print(f"Inserindo {v}...")
        h.insert(v)
        print("Tabela atual:", h)

    print("\nTabela final:")
    print(h)


if __name__ == "__main__":
    main()
