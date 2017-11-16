from decimal import Decimal
from os import path

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

_templates_path = path.dirname(__file__)
_templates_path = path.join(_templates_path, 'templates')

_env = Environment(loader=FileSystemLoader(_templates_path))


def _to_str_with_2_digits(dec):
    return f'{dec:.2f}'


class MonthlySummary:
    def __init__(self, month, year, sales, pointz_sales, base_coin_value, base_coin_emission):
        """Class representing a monthly summary dre data

        :param month: month of summary
        :param year: year of summary
        :param sales: total sales in cents
        :param pointz_sales: total sales with pointz in cents
        :param base_coin_value a tenth cent
        """
        self._base_coin_value = Decimal(base_coin_value) / 1000
        self._sales = Decimal(sales) / 100
        self._base_coin_emission = Decimal(base_coin_emission) / 100
        self._pointz_sales = Decimal(pointz_sales) / 100
        self.year = year
        self.month = month

    @property
    def sales(self):
        return _to_str_with_2_digits(self._sales)

    @property
    def pointz_sales(self):
        return _to_str_with_2_digits(self._pointz_sales)

    @property
    def base_coin_emission(self):
        return _to_str_with_2_digits(self._base_coin_emission)

    @property
    def title(self):
        return f'{self.month}-{self.year}'

    @property
    def sales_percentage(self):
        return self._pointz_sales * 100 / self._sales

    @property
    def base_coin_value(self):
        return f'{self._base_coin_value:.3f}'

    @classmethod
    def from_bigquery_row(cls, row):
        summary = cls(row.month, row.year, row.sales, row.pointz_sales, 10, 10)
        return summary


class Report:
    def __init__(self, title, monthly_summaries):
        self.monthly_summaries = monthly_summaries
        self.title = title

    @property
    def total_sales(self):
        result = sum(summary._sales for summary in self.monthly_summaries)
        return _to_str_with_2_digits(result)

    @property
    def total_pointz_sales(self):
        result = sum(summary._pointz_sales for summary in self.monthly_summaries)
        return _to_str_with_2_digits(result)

    @property
    def total_base_coin_emission(self):
        result = sum(summary._base_coin_emission for summary in self.monthly_summaries)
        return _to_str_with_2_digits(result)

    @property
    def total_sales_percentage(self):
        result = sum(summary._pointz_sales for summary in self.monthly_summaries) * 100 / sum(
            summary._sales for summary in self.monthly_summaries)
        return round(result)

    @classmethod
    def from_bigquery_result(cls, bigquery_result):
        monthly_summaries = [MonthlySummary.from_bigquery_row(row) for row in bigquery_result]
        row = bigquery_result[0]
        title = f'{row.segment_name} - {row.partner_name} - {row.region_name}'
        return cls(title, monthly_summaries)


def render(template, report):
    return _env.get_template(template).render(report=report)
