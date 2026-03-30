from ClasseTrufa import Trufa

trufaChocolate = Trufa('Chocolate' , 'Cacau em pó')
trufaChocolate.adicionarEstoque(15)

trufaLeiteNinho = Trufa('Leite Ninho', 'Leite em pó')
trufaLeiteNinho.adicionarEstoque(15)

trufaPacoca = Trufa('Paçoca' , 'Paçoca')
trufaPacoca.adicionarEstoque(15)

trufaMaracuja = Trufa('Maracuja' , 'Maracuja')
trufaMaracuja.adicionarEstoque(15)

trufaNinhoComMorango = Trufa('Ninho com morango', 'Leite em pó e morango')
trufaNinhoComMorango.adicionarEstoque(15)

estoqueTrufas = [trufaChocolate, trufaLeiteNinho, trufaPacoca, trufaMaracuja, trufaNinhoComMorango]

totalGeral = 0 

for Trufa in estoqueTrufas:
    print(Trufa)

    totalGeral += Trufa.valorTotalEstoque()

print("-" * 30)
print("Valor total do estoque: " , totalGeral)
