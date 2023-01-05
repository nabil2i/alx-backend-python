#!/usr/bin/env python3
""" Takes list input of floats and returns sum"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function sums list of floats """
    mySum: float = 0
    for x in input_list:
        mySum += x
    return mySum
