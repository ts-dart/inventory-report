from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list):
        oldest_manufacturing = SimpleReport.__oldest_manufacturing_date(list)
        closest_expiration = SimpleReport.__closest_expiration_date(list)
        company = SimpleReport.__company_with_more_products(list)

        return(
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {company}"
        )

    def __oldest_manufacturing_date(products_list):
        oldest_date = products_list[0]['data_de_fabricacao'].split('-')

        for product in products_list:
            curr__date = product['data_de_fabricacao'].split('-')

            if curr__date[0] < oldest_date[0]:
                oldest_date = curr__date
            elif curr__date[0] == oldest_date[0]\
                    and curr__date[1] < oldest_date[1]:
                oldest_date = curr__date
            elif curr__date[0] == oldest_date[0]\
                    and curr__date[1] == oldest_date[1]\
                    and curr__date[2] < oldest_date[2]:
                oldest_date = curr__date

        return '-'.join(oldest_date)

    def __closest_expiration_date(products_list):
        today_date = str(date.today()).split('-')
        closest_date = products_list[0]['data_de_validade'].split('-')
        year = int(closest_date[0]) - int(today_date[0])
        month = int(closest_date[1]) - int(today_date[1])
        day = int(closest_date[2]) - int(today_date[2])

        for product in products_list:
            curr_date = product['data_de_validade'].split('-')
            curr_year = int(curr_date[0]) - int(today_date[0])
            curr_month = int(curr_date[1]) - int(today_date[1])
            curr_day = int(curr_date[2]) - int(today_date[2])

            if curr_year < year:
                year, month, day = curr_year, curr_month, curr_day
                closest_date = curr_date
            elif curr_year == year\
                    and curr_month < month:
                year, month, day = curr_year, curr_month, curr_day
                closest_date = curr_date
            elif curr_year == year\
                    and curr_month == month\
                    and curr_day < day:
                year, month, day = curr_year, curr_month, curr_day
                closest_date = curr_date

        return '-'.join(closest_date)

    def __company_with_more_products(products_list):
        companyes, large, company_name = {}, 0, ''

        for product in products_list:
            if product['nome_da_empresa'] not in companyes:
                companyes[product['nome_da_empresa']] = 1
            else:
                companyes[product['nome_da_empresa']] += 1

        for company in companyes:
            if companyes[company] > large:
                large, company_name = companyes[company], company

        return company_name
