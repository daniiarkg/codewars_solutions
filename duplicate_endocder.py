# Kata URL https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word):
    return ''.join(')' if word.lower().count(i)>1 else '(' for i in word.lower())