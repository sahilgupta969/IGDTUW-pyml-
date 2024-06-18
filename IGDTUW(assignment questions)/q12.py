# Write a python program that calculates the sum of the digits of a given number
num = int(input("enter any num "))
sum = 0
while num >0:
    r = num%10
    sum = sum + r
    num = num//10
print("\n sum of digit given num = %d" % sum)