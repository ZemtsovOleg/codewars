'''
DESCRIPTION:
Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. Bonus points for a solution that is efficient and/or that uses only built-in language functions. Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

Example
madam -> True
adamm -> True
junk -> False

Hint
The brute force approach would be to generate all the permutations of the string and check each one of them whether it is a palindrome. However, an optimized approach will not require this at all.
'''

import collections


# my decision
def permute_a_palindrome(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(s).values()) < 2


# other solutions
def permute_a_palindrome1(s: str) -> bool:
    return sum(v % 2 for v in collections.Counter(x for x in s.lower() if x.isalpha()).values()) <= 1


def permute_a_palindrome2(s: str) -> bool:
    return sum(s.count(l) % 2 for l in set(s)) < 2


def permute_a_palindrome3(s: str) -> bool:
    if not s:
        return True
    for i in s:
        if s == s[::-1]:
            return True
        s = f'{s[1:]}{i}'
    return False


print(permute_a_palindrome("aa"), True)
print(permute_a_palindrome("aaa"), True)
print(permute_a_palindrome("baa"), True)
print(permute_a_palindrome("aab"), True)
print(permute_a_palindrome("aabb"), True)
print(permute_a_palindrome("aabbb"), True)
print(permute_a_palindrome("baabcd"), False)
print(permute_a_palindrome("racecars"), False)
print(permute_a_palindrome("abcdefghba"), False)
print(permute_a_palindrome(""), True)
