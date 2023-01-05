#!/usr/bin/env python3
"""Takes list input of floats and ints
and returns sum """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function sums list, returns float """
    mySum: float = 0
    for x in mxd_lst:
        mySum += x
    return mySum
