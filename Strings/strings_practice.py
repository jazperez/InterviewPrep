#Some Daily Warm-Ups
# 1. How do you print duplicate characters from a string?
def showDuplicateChars1(string):
    count = {}
    # count = {p:1, r:2, o:1, g:1,..... } {key:value}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            print(key, count[key])

def showDuplicateChars2(string):
    list_of_chars = set()
    duplicates = set()
    for char in string:
        ## checking whether the char is already present in set or not
        if char in list_of_chars:
            ## increasing count if present
            duplicates.add(char)
        else:
            list_of_chars.add(char)

    for x in duplicates:
        print(x)

# 2. How do you reverse a given string in place?
# 3. How do you check if two strings are anagrams of each other?
# 4. How do you find all the permutations of a string?
# 5. How can a given string be reversed using recursion?
# 6. How do you check if a string contains only digits?
# 7. How do you count a number of vowels and consonants in a given string?
# 8. How do you convert a given String into int like the atoi()?
# 9. How do you check if a given string is a palindrome?
# 10. How do you find the length of the longest substring without repeating characters?
# 11. How do you remove a given character from String?
# 12. How to convert a byte array to String?
# 13. Given string str, How do you find the longest palindromic substring in str?
# 14. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# 15. Write a Python function that takes a list of words and returns the longest word and the length of the longest one. 
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
# 15. Write a Python program to remove the nth index character from a nonempty string.
# 16. Write a Python program to remove the characters which have odd index values of a given string.
# 17. Write a Python program to count the occurrences of each word in a given sentence.
# 18. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# 19. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# 20. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
# 21. Write a Python function to insert a string in the middle of a string. 
# 22. Write a Python program to create a Caesar encryption.
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
# 23. Write a Python program to remove a newline in Python.
# 24. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
# Example: -12.3899 -> -13
# # Example: 11.3433 -> 11
# 25. Write a Python program to strip a set of characters from a string.
# 26. Write a program that will find the squared root of an int without using a library.
# 27. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# 28. Write a Python program to find the second most repeated word in a given string.
# 29. Write a Python program to remove spaces from a given string.
# 30. Write a Python program to compute sum of digits of a given string.
# 31. Write a Python program to find maximum length of consecutive 0's in a given binary string.
# 32. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string
# 33. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
# 34. Write a Python program to find smallest window that contains all characters of a given string.
# 35. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters.
# 36. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
# 37. Write a Python program to find smallest and largest word in a given string.
# 38. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001
# 39. Write a Python program to swap cases of a given string. 
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY
# 40.Write a Python program to convert a given Bytearray to Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d
# 41. Write a Python program find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python
# 42. Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# 43. Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
# 44. Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'
# 45. How would you check if each word in a string begins with a capital letter?
# 46. Count the number of a specific character in a string.
# 47. Split a string on a specific character.
# 48. Give an example of string slicing.
# 49. Remove whitespace from the left, right or both sides of a string.
# 50. Construct K Palindrome Strings
# Given a string s and an integer k. You should construct k non-empty palindrome strings using all the characters in s.
# Return True if you can use all the characters in s to construct k palindrome strings or False otherwise.

# Example 1:
# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

# Example 2:
# Input: s = "leetcode", k = 3
# Output: false
# Explanation: It is impossible to construct 3 palindromes using all the characters of s.

#interview question
def findMaxDiffInTimes(times):
    # times = ["01:30", "24:00", "06:29", "14:09"]
    hours = []
    MAX_DIFF = 0

    for i in times:
        i = i.replace(":", "")
        hours.append(int(i))

    hours.sort()
    MAX_DIFF = hours[-1] - hours[0]
    print(MAX_DIFF)


showDuplicateChars1("programming")
showDuplicateChars2("banana")
# times = ["01:30", "24:00", "06:29", "14:09"]
# findMaxDiffInTimes(times)