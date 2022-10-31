import csv
import json
# import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if Inventory.__file_type(path) == 'csv':
            return Inventory.__csv_file(path, report_type)
        '''elif Inventory.__file_type(path) == 'xml':
            return Inventory.__xml_file(path, report_type)'''
        return Inventory.__json_file(path, report_type)

    def __file_type(path):
        type = (path[len(path) - 3], path[len(path) - 2], path[len(path) - 1])
        return ''.join(type)

    def __csv_file(path, report_type):
        with open(path, mode='r') as file:
            data = csv.DictReader(file)
            products_list = [index for index in data]

            if report_type == 'simples':
                return SimpleReport().generate(products_list)
            elif report_type == 'completo':
                return CompleteReport().generate(products_list)

    '''def __xml_file(path, report_type):
        with open(path, mode='r') as file:
            data = xmltodict.parse(file.read())
            products_list = [index for index in data['dataset']['record']]

            if report_type == 'simples':
                return SimpleReport().generate(products_list)
            elif report_type == 'completo':
                return CompleteReport().generate(products_list)'''

    def __json_file(path, report_type):
        with open(path, mode='r') as file:
            data = json.load(file)
            products_list = [index for index in data]

            if report_type == 'simples':
                return SimpleReport().generate(products_list)
            elif report_type == 'completo':
                return CompleteReport().generate(products_list)
