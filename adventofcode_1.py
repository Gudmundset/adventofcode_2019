#!/usr/bin/python
""" For example:
>>> print(fuel_req(12))
2
>>> print(fuel_req(14))
2
>>> print(fuel_req(1969))
654
>>> print(fuel_req(100756))
33583
"""

from collections import Counter

def fuel_req(mass):
    '''Function: fuel calculator'''
    return int(mass / 3) - 2

def fuel_req_recursive(mass):
    '''Function: fuel calculator recursive'''
    extra_fuel = 0
    while fuel_req(mass) > 0:
        extra_fuel += fuel_req(mass)
        mass = fuel_req(mass)
    return extra_fuel

def fuel_counter_upper():
    '''Function: main'''
    c = Counter()
    log_file = 'mass.log'
    with open(log_file) as f:
        for mass in f.readlines():
            if mass:
                c['fuel_required'] += fuel_req_recursive(int(mass))
    print(c)

if __name__ == "__main__":
    fuel_counter_upper()
