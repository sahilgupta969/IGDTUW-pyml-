# Write a python program that generates the first n numbers in the Fibonacci sequence.

n = int(input("enter the num "))
a= 0
b = 1
for i in range(0,n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c