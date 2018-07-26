#https://www.codewars.com/kata/pair-of-gloves/train/python
def number_of_pairs(gloves):
    my_set = set(gloves)
    total = 0
    for i in my_set:
        total += gloves.count(i)//2
    return total