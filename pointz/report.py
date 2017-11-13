from os import path

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

_templates_path = path.dirname(__file__)
_templates_path = path.join(_templates_path, 'templates')

_env = Environment(loader=FileSystemLoader(_templates_path))


class MonthlySummary:
    def __init__(self, month, year):
        self.year = year
        self.month = month

    @property
    def title(self):
        return f'{self.month}-{self.year}'


class Report:
    def __init__(self, title, monthly_summaries):
        self.monthly_summaries = monthly_summaries
        self.title = title


def render(template, report):
    return _env.get_template(template).render(report=report)
