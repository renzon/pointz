import os
from os import path

from pointz.bigquery.client import client
from pointz.bigquery.reader import get_annual_dre_by_partner_region, get_max_transaction_id
from pointz.bigquery.schema import transactions_table
from pointz.bigquery.uploader import get_transaction_batches, sql_transaction_to_bigquery_row
from pointz.report import render_multiple_annual_dres


def create_annual_dre_per_partner_region(year=None):
    print('Gerando DRES')
    result = list(get_annual_dre_by_partner_region(year))
    build_dir_path = path.abspath('build')
    if not path.exists(build_dir_path):
        os.mkdir(build_dir_path)
    for title, report in render_multiple_annual_dres(result):
        dre_file_path = path.join(build_dir_path, f'dre-{title}.html')
        with open(dre_file_path, 'w', encoding='utf8') as dre_file:
            dre_file.write(report)
    print('Relatórios gerados')


def load_data_and_generate_report():
    global max_id
    print('Pegando id máximo de transação no Bigquery')
    max_id = get_max_transaction_id()
    print(f'Id máximo encontrado: {max_id}')
    for batch in get_transaction_batches(max_id, limit=2):
        rows = [sql_transaction_to_bigquery_row(transaction) for transaction in batch]
        print('Carregando transações no Bigquery')
        client.create_rows(transactions_table, rows)
    print('Carregando no Bigquery Finalizado')
    create_annual_dre_per_partner_region()



main = load_data_and_generate_report
