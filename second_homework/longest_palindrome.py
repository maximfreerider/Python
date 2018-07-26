#https://www.codewars.com/kata/longest-palindrome/train/python

from itertools import combinations_with_replacement as cwr  '''itertools.combinations_with_replacement(iterable, r) - комбинации длиной r из iterable с повторяющимися элементами.'''

def longest_palindrome (s):
    return max(len(s[i:j]) for i,j in cwr(range(len(s)+1), 2) if s[i:j] and s[i:j]==s[i:j][::-1]) if s else 0