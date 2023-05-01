'''
DESCRIPTION:
Instructions
The goal of this kata is two-fold:

1.) You must produce a fibonacci sequence in the form of an array, containing a number of items equal to the input provided.

2.) You must replace all numbers in the sequence divisible by 3 with Fizz, those divisible by 5 with Buzz, and those divisible by both 3 and 5 with FizzBuzz.

For the sake of this kata, you can assume all input will be a positive integer.

Use Cases
Return output must be in the form of an array, with the numbers as integers and the replaced numbers (fizzbuzz) as strings.


Input:

fibs_fizz_buzz(20)
Output:

[1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz"]
'''


def fibs_fizz_buzz(n: int) -> int:
    x, y = 0, 1
    fib = []
    for i in range(n):
        x, y = y, y + x
        if (not x % 3) and (not x % 5):
            fib.append('FizzBuzz')
        elif not x % 3:
            fib.append('Fizz')
        elif not x % 5:
            fib.append('Buzz')
        else:
            fib.append(x)
    return fib


print(fibs_fizz_buzz(20))
