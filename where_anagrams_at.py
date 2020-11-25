#Kata URL https://www.codewars.com/kata/523a86aa4230ebb5420001e1
anagrams = lambda word, words: list(filter(lambda x: sorted(x) == sorted(word), words ))