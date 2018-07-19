# https://www.codewars.com/kata/check-for-prime-numbers/train/python

def is_prime(n):
  if n == 0 or n == 1:
    return False
  for i in range(n):
    if i != 1 and i != 0:
      a = n % i
      if a == 0:
        return False
  return True