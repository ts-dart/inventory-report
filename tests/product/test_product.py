from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 437
    nome_da_empresa = 'Microsoft'
    nome_do_produto = 'Xbox Series X'
    data_de_fabricacao = '12/09/2021'
    data_de_validade = 'Sem vencimento'
    numero_de_serie = '00314042007-B'
    instrucoes_de_armazenamento = 'Sem instruções especiais de armazenamento'

    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
