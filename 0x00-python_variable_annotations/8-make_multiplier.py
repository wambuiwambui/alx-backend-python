#!/usr/bin/env python3
"""
Python annotations
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier