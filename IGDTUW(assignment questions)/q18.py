# Write a python program that checks if two strings are anagrams of each other.

str1 = "abcd"
str2 = "cdab"

str1 = sorted(str1)
str2 = sorted(str2)

if str1==str2:
    print("yes")
else:
    print("no")
