# Kata URL https://www.codewars.com/kata/5254ca2719453dcc0b00027d
from itertools import permutations as pms
def permutations(string):
    return sorted(list(set([''.join(i) for i in pms(string)])))