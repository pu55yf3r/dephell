# built-in
from argparse import ArgumentParser, REMAINDER

# app
from ..config import builders
from ..repositories import WareHouseRepo
from .base import BaseCommand


class PackageSearchCommand(BaseCommand):
    @classmethod
    def get_parser(cls):
        parser = ArgumentParser(
            prog='dephell package search',
            description='Search package on PyPI.org',
        )
        builders.build_config(parser)
        builders.build_output(parser)
        builders.build_api(parser)
        builders.build_other(parser)
        parser.add_argument('name', nargs=REMAINDER, help='package name or other search keywords')
        return parser

    def __call__(self):
        repo = WareHouseRepo()
        results = repo.search(self.args.name)
        print(self.get_value(data=results, key=self.config.get('filter')))