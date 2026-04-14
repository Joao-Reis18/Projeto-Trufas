def cadastrar_ingrediente():
        ingredientes = []

        while True:
            nome = input("Nome do ingrediente: ")
            preco = float(input("Preço do ingrediente: "))

            ingredientes.append({"nome": nome, "preco": preco})

            continuar = input("Deseja inserir novos ingredientes? [S/N] ")

            if continuar.lower() != "s":
                break

        return ingredientes

def calcular_custo_total (ingredientes):
    total = 0
    for item in ingredientes:
        total += item["preco"]

    return total

def calcular_custo_por_trufa(custo_total , quantidade):
        return custo_total / quantidade

def calcular_lucro(preco_venda , custo_unitario, quantidade_vendida):
        lucro_unitario = preco_venda - custo_unitario
        lucro_total = lucro_unitario * quantidade_vendida
        return lucro_unitario, lucro_total
