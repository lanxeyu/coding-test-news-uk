# Question 1
# Write a function that prints the numbers from 1 to 100 (i.e. it should 
# print 1, 2,...,100 to the screen).

def print_1_to_100():
    for i in range(1, 101):
        print(i)

# Question 2
# Write a function that prints the numbers from 1 to 100. However, for
# multiples of 3 it should print “Fizz” instead of the number; for
# multiples of 5 it should print “Buzz”. For multiples of 3 and 5, print
# “FizzBuzz”.

def print_fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# Question 3
# Write a function to search for a character within a string. Given a
# character and string as inputs, your function should return the index
# of the first occurrence of the character within the string. If the string
# does not contain the character, your function should return -1.
# Do not use any built-in library functions to answer this question (e.g.
# if you’re using Python, do not use the find() or index() functions).

def search_char_in_string(target_char, my_string):
    i = 0
    for char in my_string:
        if char == target_char:
            return i
        i += 1
    
    return -1

# Question 4
# A palindrome is a string that reads the same way backwards as it
# does forwards, e.g. “radar” or “madam”. Write a function that takes a
# string as input and prints “Palindrome” if the input string is a
# palindrome but “Not palindrome” otherwise. For the empty string
# (i.e. “”), your function should print “Empty string”.
# Do not use any built-in library functions to answer this question (and
# if you’re using Python, do not use anything like my_string[::-1]).

def check_is_palindrome(my_string):
    if my_string == '':
        print('Empty string')
        return

    cleaned_string = ''.join(my_string.split()).lower()

    reversed_array = []
    for i in range(len(cleaned_string) - 1, -1, -1):
        reversed_array.append(cleaned_string[i])

    reversed_string = ''.join(reversed_array)

    if reversed_string == cleaned_string:
        print('Palindrome')
    else:
        print('Not palindrome')

# Question 5
# Write a function that takes a list/array of strings as input and
# determines whether it contains duplicate strings. Your function
# should print “Contains duplicates” if the list does contain duplicates;
# otherwise, it should print “Does not contain duplicates”.

def check_duplicates(my_array):
    my_array.sort()
    
    for i in range(len(my_array) - 1):
        if my_array[i] == my_array[i + 1]:
            print('Contains duplicates')
            return
    
    print('Does not contain duplicates')
        
# Question 6
# Write a function that takes a list/array of strings as input and
# “deduplicates” it. Your function should return a new list/array of
# strings with all duplicates removed. It’s fine if your new list/array is
# not in the same order as the original list.

def deduplicate(my_array):
    my_array.sort()

    i = len(my_array) - 1
    while i > 0:
        if my_array[i] == my_array[i - 1]:
            my_array.pop(i)
        i -= 1
    
    return my_array
    
# Question 7
# A word is an anagram of another word if the first word’s letters can
# be rearranged to form the second word. For example, “ward” and
# “draw” are anagrams of one another, as are “silent” and “listen”.
# Write a function that determines whether two strings are anagrams
# of another. Your function should take two strings as input and print
# “Anagram” if they are anagrams; otherwise, it should print “Not
# anagram”. For simplicity, treat blank spaces as if they are any other
# character.

def check_are_anagrams(string1, string2):
    cleaned_string1 = ''.join(string1.split()).lower()
    cleaned_string2 = ''.join(string2.split()).lower()

    if sorted(cleaned_string1) == sorted(cleaned_string2):
        print("Anagram")
    else:
        print("Not anagram")

# Question 8
# Write a function that finds the largest prime factor of any number
# greater than 1. Your function should take a single number as input
# and return its largest prime factor. For example, the prime factors of
# 78 are 2, 3 and 13, so its largest prime factor is 13.

def get_largest_prime_factor(my_number):
    divisor = 2

    while divisor ** 2 <= my_number:
        if my_number % divisor == 0:
            my_number //= divisor
        else:
            divisor += 1

    return my_number

# Question 9
# An n-digit number is pandigital if it makes use of all the digits 1 to n
# exactly once. For example, the 5-digit number 15234 is pandigital, as
# is the 6-digit number 463215.
# Write a function that takes a number as input and prints “Pandigital”
# if the input number is pandigital but “Not pandigital” otherwise.

def check_is_pandigital(my_number):
    num_to_string = str(my_number)

    n = len(num_to_string)
    ref_dict = {}
    for i in range(1, n + 1):
        ref_dict.update({str(i) : 0})

    for char in num_to_string:
        if char in ref_dict and ref_dict[char] == 0:
            ref_dict[char] += 1
        else:
            print('Not pandigital')
            return
    
    print('Pandigital')

# Question 10
# Write a function that sorts a list/array of numbers. Your function
# should take a list/array of numbers as input and return the list/array
# in ascending order.
# Do not use any built-in library functions to answer this question (e.g.
# if you’re using Python, do not use the sort() function).

def sort_numbers(num_array):
    num_of_passes = len(num_array) - 1

    while num_of_passes > 0:

        for i in range(len(num_array) - 1):
            if num_array[i + 1] < num_array[i]:
                temp = num_array[i]
                num_array[i] = num_array[i + 1]
                num_array[i + 1] = temp

        num_of_passes -= 1

    return num_array