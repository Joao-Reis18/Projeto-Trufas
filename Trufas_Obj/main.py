import Trufas

def main():
    print("=== SISTEMA DE CONTROLE DE TRUFAS ===")

    ingredientes = Trufas.cadastrar_ingrediente()

    custo_total = Trufas.calcular_custo_total(ingredientes)

    quantidade = int(input("Quantidade de trufas produzidas: "))
    preco_venda = float(input("Preço de venda por trufa (R$): "))
    quantidade_vendida = int(input("Quantidade vendida: "))

    custo_unitario = Trufas.calcular_custo_por_trufa(custo_total, quantidade)

    lucro_unitario, lucro_total = Trufas.calcular_lucro(
        preco_venda, custo_unitario, quantidade_vendida
    )

    print("\n=== RESULTADO ===")
    print(f"Custo total: R$ {custo_total:.2f}")
    print(f"Custo por trufa: R$ {custo_unitario:.2f}")
    print(f"Lucro por trufa: R$ {lucro_unitario:.2f}")
    print(f"Lucro total: R$ {lucro_total:.2f}")


main()