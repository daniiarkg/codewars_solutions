# Kata URL https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s):
    return False if len('#' + ''.join([x for x in s.split()])) > 140 or len(s)==0 else '#' + ''.join([x.capitalize() for x in s.split()])