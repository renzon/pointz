import os
from os import path

from pointz.bigquery.reader import get_annual_dre_by_partner_region
from pointz.report import render_annual_dre_per_partner_region


def create_annual_dre_per_partner_region(year=None):
    result = list(get_annual_dre_by_partner_region(year))
    print(result)
    report = render_annual_dre_per_partner_region(result)
    build_dir_path = path.dirname(__file__)
    build_dir_path = path.abspath(path.join(build_dir_path, '..', 'build'))
    if not path.exists(build_dir_path):
        os.mkdir(build_dir_path)
    dre_file_path=path.join(build_dir_path, 'dre.html')
    with open(dre_file_path, 'w', encoding='utf8') as dre_file:
        dre_file.write(report)




if __name__ == '__main__':
    create_annual_dre_per_partner_region(2016)
