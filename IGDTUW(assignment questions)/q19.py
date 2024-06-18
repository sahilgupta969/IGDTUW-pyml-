# Write a python program that removes all punctuation from a given string


punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
my_str = input("Enter a string: ")  

no_punct = ""  
for char in my_str:  
   if char not in punctuation:  
       no_punct = no_punct + char  
  
print(no_punct)  