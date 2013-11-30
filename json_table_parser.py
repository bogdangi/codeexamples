# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
File: json_table_parser.py
Author: Bogdan Girman
Description: This program should check correct sums
'''
import json


def jsonTableParser(json_table):
    """
    Дана таблица размера n x m, в ячейках
    которой содержатся целочисленные
    значения.
    Последняя строка таблицы содержит
    итоговые суммы значений соответствующих
    столбцов.
    а. Напишите функцию на Python, которая
    принимает на вход строку, содержащую
    одномерный Json-массив ячеек таблицы вида
        >>> table = '''[
        ... {
        ... "value": 0,
        ... "x":1,
        ... "y":2
        ... },
        ... {
        ... "value": 4,
        ... "x":3,
        ... "y":2
        ... },
        ... {
        ... "value": 2,
        ... "x":3,
        ... "y":4
        ... },
        ... {
        ... "value": 1,
        ... "x":1,
        ... "y":5
        ... },
        ... {
        ... "value": 6,
        ... "x":3,
        ... "y":5
        ... },
        ... {
        ... "value": 1,
        ... "x":1,
        ... "y":4
        ... }
        ... ]'''

    где структура

    {
    "value": 6,
    "x":3,
    "y":5
    }

    описывает ячейку таблицы, содержащую
    значение (value) 6, положение которой
    на экране определятся координатами (x,y),
    и возвращает строку, содержащую
    одномерный Json-массив, который состоит из
    структур вида

        >>> print jsonTableParser(table) #doctest: +ELLIPSIS
        [...
        {
        "x": 1,
        "correct": 1
        }...
        ...
        ]

    где «x» определяет столбец, а ячейка
    «correct» содержит 1, если итоговая сумма в
    столбце «x» верна, и 0 — в противном
    случае.
    Результат должен содержать только те
    столбцы «x», которые переданы в исходном
    наборе данных.
    """
    table = json.loads(json_table)
    result_table = {}
    # calculate sum for first run
    for i in table:
        # create new column in table if it is not exist
        result_table[i['x']] = result_table.get(i['x'], {
            'last': 0,
            'sum': 0,
            'last_row': 0
            })
        result_table[i['x']]['sum'] = result_table[i['x']]['sum'] + i['value']
        if result_table[i['x']]['last_row'] < i['y']:
            result_table[i['x']]['last_row'] = i['y']
            result_table[i['x']]['last'] = i['value']

    result = []
    # find right sum for table
    for i in result_table.keys():
        result.append({
            'x': i,
            # div it to 2 more faster than subtract *last* from *sum*
            'correct': result_table[i]['sum']/2 == result_table[i]['last']
            and 1 or 0
            })

    return json.dumps(result, indent=0, separators=(',', ': '))
