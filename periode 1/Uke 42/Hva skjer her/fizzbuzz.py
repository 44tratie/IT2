"""
This program will display all the numbers between 1 and 100, with some exceptions:

- For each number divisible by three the computer will display the word "fizz"
- For each number divisible by five the computer will display the word "buzz"
- For each number divisible by three and by five the computer will display the word "fizz-buzz"
,
This is what the output will look like:
1
2
Fizz
4
Buzz
Fizz
7
"""


def is_divisible_by(divisor: int, dividend: int) -> bool:
    return dividend % divisor == 0


for current_number in range(1, 16):
    if is_divisible_by(15, current_number):
        print("fizz-buzz")
        continue

    elif is_divisible_by(5, current_number):
        print("buzz")
        continue

    elif is_divisible_by(3, current_number):
        print("fizz")
        continue

    print(current_number)
