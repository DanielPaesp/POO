class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro = Livro("ONE PIECE VOL. 1", 100.00, "Eiichiro Oda")

eletronico = Eletronico("Computador", 10500.00, "0V")

livro.aplicar_desconto(15)
eletronico.aplicar_desconto(10)

print("=== Livro ===")
print(f"Nome: {livro.nome}")
print(f"Autor: {livro.autor}")
print(f"Preço com desconto: R$ {livro.preco:.2f}")

print("\n=== Eletrônico ===")
print(f"Nome: {eletronico.nome}")
print(f"Voltagem: {eletronico.voltagem}")
print(f"Preço com desconto: R$ {eletronico.preco:.2f}")