"""Testing functions to transform big query result in report models"""
import pytest
from google.cloud.bigquery._helpers import Row

from pointz.report import MonthlySummary, Report

columns_dct = {'sales': 0, 'pointz_sales': 1, 'pointz': 2, 'year': 3, 'month': 4, 'region_name': 5, 'partner_name': 6,
               'segment_name': 7, 'partner_id': 8}
annual_report_result = [
    Row((500, 400, 10, 2017, 1, 'Fortaleza', 'Posto Flex', 'GAS', 1), columns_dct),
    Row((1800, 1600, 40, 2017, 2, 'Fortaleza', 'Posto Flex', 'GAS', 1), columns_dct)
]
row = annual_report_result[0]


def test_row_to_monthly_summary_pointz_sales():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert '4.00' == summary.pointz_sales


def test_row_to_monthly_summary_sales():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert '5.00' == summary.sales


@pytest.mark.parametrize(
    'row,expected_percentage',
    [
        (annual_report_result[0], 80),
        (annual_report_result[1], 89)
    ]
)
def test_row_to_monthly_sales_percentage(row, expected_percentage):
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert expected_percentage == summary.sales_percentage


@pytest.mark.parametrize(
    'row,base_coin_value',
    [
        (annual_report_result[0], '0.010'),
        (annual_report_result[1], '0.020')
    ]
)
def test_row_to_monthly_base_coin_value(row, base_coin_value):
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert base_coin_value == summary.base_coin_value


@pytest.mark.parametrize(
    'row,base_coin_emission',
    [
        (annual_report_result[0], '0.10'),
        (annual_report_result[1], '0.80')
    ]
)
def test_row_to_monthly_base_coin_emission(row, base_coin_emission):
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert base_coin_emission == summary.base_coin_emission


def test_row_to_monthly_summary_year():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert 2017 == summary.year


def test_row_to_monthly_summary_month():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert 'jan' == summary.month


def test_bigquery_result_to_report_title():
    report = Report.from_bigquery_result(annual_report_result)
    assert 'GAS - Posto Flex - Fortaleza' == report.title


def test_bigquery_result_to_report_total_sales():
    report = Report.from_bigquery_result(annual_report_result)
    assert '23.00' == report.total_sales


def test_bigquery_result_to_report_total_pointz_sales():
    report = Report.from_bigquery_result(annual_report_result)
    assert '20.00' == report.total_pointz_sales


def test_bigquery_result_to_report_total_sales_percentage():
    report = Report.from_bigquery_result(annual_report_result)
    assert 87 == report.total_sales_percentage
