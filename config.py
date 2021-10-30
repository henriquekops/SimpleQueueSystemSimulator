#!/usr/bin/env python
# -*- coding: utf-8 -*-

from yamale import (
    validate,
    make_data,
    make_schema,
    YamaleError
)


class YamlParser:

    schema = make_schema('schema.yaml')

    def __init__(self) -> None:
        pass

    def validate(self, file_path: str):
        validate(self.schema, make_data(file_path))


# testing
if __name__ == '__main__':
    p = YamlParser()
    try:
        p.validate('example.yaml')
        print('valid')
    except YamaleError as e:
        print(e)