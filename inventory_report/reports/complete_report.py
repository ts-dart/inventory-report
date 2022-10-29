from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list):
        oldest_manufacturing = SimpleReport._oldest_manufacturing_date(list)
        closest_expiration = SimpleReport._closest_expiration_date(list)
        company = SimpleReport._company_with_more_products(list)

        return(
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {company}\n"
            "Produtos estocados por empresa:\n"
            f"{CompleteReport.stock_by_company(list)}"
        )

    def stock_by_company(products_list):
        companyes, text = {}, ''

        for product in products_list:
            if product['nome_da_empresa'] not in companyes:
                companyes[product['nome_da_empresa']] = 1
            else:
                companyes[product['nome_da_empresa']] += 1

        for company in companyes:
            text += f'- {company}: {companyes[company]}\n'

        return text
