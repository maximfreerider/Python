#https://www.codewars.com/kata/the-sum-and-the-rest-of-certain-pairs-of-numbers-have-to-be-perfect-squares/train/python
def closest_pair_tonum(upper_lim):
    for m in range(upper_lim-1,1,-1):
        for n in range(m-1,0,-1):
            if sq(m+n) and sq(m-n):
                return (m, n)
def sq(n):
    root = n ** .5
    return int(root) == root





from math import sqrt
def closest_pair_tonum(upper_lim):
    for m in range(upper_lim-1,1,-1):
        for n in range(m-1,0,-1):
            if math.sqrt(m+n) and math.sqrt(m-n):
                return (m, n)
