"""Testing functions to transform big query result in report models"""
from google.cloud.bigquery._helpers import Row

from pointz.report import MonthlySummary

columns_dct = {'sales': 0, 'pointz_sales': 1, 'pointz': 2, 'year': 3, 'month': 4, 'region_name': 5, 'partner_name': 6,
               'segment_name': 7}

# @pytest.mark.parametrize(
#     'row',
#     [
#         Row((100, 400, 10, 2017, 1, 'Fortaleza', 'Posto Flex', 'GAS'), columns_dct),
#         Row((1800, 1600, 40, 2017, 2, 'Fortaleza', 'Posto Flex', 'GAS'), columns_dct)
#     ]
# )
row = Row((500, 400, 10, 2017, 1, 'Fortaleza', 'Posto Flex', 'GAS'), columns_dct)


def test_row_to_monthly_summary_pointz_sales():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert '4.00' == summary.pointz_sales


def test_row_to_monthly_summary_sales():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert '5.00' == summary.sales


def test_row_to_monthly_summary_year():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert 2017 == summary.year

def test_row_to_monthly_summary_month():
    """Test that a row can be transformed into a MonthlySummary"""
    summary = MonthlySummary.from_bigquery_row(row)
    assert 1 == summary.month
