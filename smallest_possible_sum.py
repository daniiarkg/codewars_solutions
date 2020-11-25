#Kata URL https://www.codewars.com/kata/52f677797c461daaf7000740
from math import gcd
from functools import reduce
def solution(a):
    return reduce(gcd,a)*len(a)