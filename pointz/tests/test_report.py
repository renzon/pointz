import pytest

from pointz.report import render, Report, MonthlySummary


def read_report_content():
    monthly_summaries = [
        MonthlySummary('jan', 2017),
        MonthlySummary('fev', 2017),
    ]
    report = Report(
        'GAS - Posto Flex - Fortaleza',
        monthly_summaries
    )
    return render('dre.html', report=report)


def test_title():
    report_content = read_report_content()
    assert 'GAS - Posto Flex - Fortaleza' in report_content


@pytest.mark.parametrize('header', ['jan-2017', 'fev-2017'])
def test_month_header(header):
    report_content = read_report_content()
    assert header in report_content


@pytest.mark.parametrize('sale', ['5.00', '18.00', '23.00'])
def test_total_sales(sale):
    report_content = read_report_content()
    assert sale in report_content


@pytest.mark.parametrize('sale', ['4.00', '16.00', '20.00'])
def test_pointz_sales(sale):
    report_content = read_report_content()
    assert sale in report_content


@pytest.mark.parametrize('percentage', ['80%', '89%', '87%'])
def test_sales_percentage(percentage):
    report_content = read_report_content()
    assert percentage in report_content


@pytest.mark.parametrize('value', ['0.50', '0.25'])
def test_base_point_value(value):
    report_content = read_report_content()
    assert value in report_content


@pytest.mark.parametrize('value', ['2.00', '4.00', '6.00'])
def test_base_point_emission(value):
    report_content = read_report_content()
    assert value in report_content
