class Trufa:

    def __init__(self, sabor, ingredientePrincipal):
        self.sabor = sabor
        self.ingredientePrincipal = ingredientePrincipal
        self.qnt = 0
        self.preco = 7

    def adicionarEstoque(self, quantidade):
        self.qnt += quantidade

    def valorTotalEstoque(self):
        return self.qnt * self.preco

    def __str__(self):
        return f"Trufa de {self.sabor} | Quantidade: {self.qnt}"

