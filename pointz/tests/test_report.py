from os import path


def test_title():
    report_path = path.dirname(__file__)
    report_path = path.join(report_path, '..', '..', 'contrib', 'dre-sample.html')
    report_path = path.abspath(report_path)
    report_file = open(report_path, 'r', encoding='utf8')
    report_content = '\n'.join(report_file.readlines())

    assert 'GAS - Posto Flex - Fortaleza' in report_content
