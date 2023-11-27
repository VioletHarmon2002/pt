#Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

from itertools import combinations

number = list[1, 2, 3, 4, 5, 6, 7, 8, 9]
digit = 3
digit_code = list(combinations(number, digit))
print(digit_code)

















