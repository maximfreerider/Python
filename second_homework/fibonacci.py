# https://www.codewars.com/kata/n-th-fibonacci/train/python
def nth_fib(n):
    a = 0
    b = 1
    c = 2
    if n == 1:
         return 0
    elif n == 2:
        return 1
    else:
        while c < n:
            a = b
            b = b + a
            c = c + 1
        return b