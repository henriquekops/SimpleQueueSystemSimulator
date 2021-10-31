#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint # TODO: drop

# built-in dependencies
from typing import Tuple

# external dependencies
from yaml import full_load
from yamale import (
    validate as y_validate,
    make_data,
    make_schema,
    YamaleError
)


class YamlParser:

    schema = make_schema('static/schema.yaml')

    def validate(self, file_path:str) -> Tuple[bool, YamaleError]:
        """
        Schema validation for yaml input
        """
        try:
            y_validate(self.schema, make_data(file_path))
            return True, None
        except YamaleError as e:
            return False, e

    def read(self, file_path:str) -> dict:
        """
        Load yaml data into dict
        """
        try:
            with open(file_path) as f: 
                return full_load(f)
        except:
            return dict()


# testing

# use below command at project root (SimpleQueueSimulator/):
#   $ python src/utils/config.py

if __name__ == '__main__':
    p = YamlParser()
    pprint(p.validate('example.yaml')) # validate schema
    pprint(p.read('example.yaml')) # show loaded data
