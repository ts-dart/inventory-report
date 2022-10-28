from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 437
    nome_da_empresa = 'Microsoft'
    nome_do_produto = 'Xbox Series X'
    data_de_fabricacao = '12/09/2021'
    data_de_validade = 'Sem vencimento'
    numero_de_serie = '00314042007-B'
    instrucoes_de_armazenamento = 'Sem instruções especiais de armazenamento'

    expect = (
        f"O produto {nome_do_produto}"
        f" fabricado em {data_de_fabricacao}"
        f" por {nome_da_empresa} com validade"
        f" até {data_de_validade}"
        f" precisa ser armazenado {instrucoes_de_armazenamento}."
    )

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert str(product.__repr__()) == expect
