# Kata URL https://www.codewars.com/kata/51c8e37cee245da6b40000bd
def solution(string,markers):
    if len(markers) == 0:
        return string
    for i in markers:
        string = string.replace(i,markers[0])
    rs = [x.rstrip(' ') for x in string.split(markers[0])]
    result = rs[0]
    rs = rs[1:]
    for j in rs:
        result = result + j[j.find('\n'):] if j.find('\n') != -1 else result
    return result