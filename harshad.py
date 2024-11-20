#program to find a Harshad number
#defination: A number that is divisible by the sum of its digits. 
# For example, 18 is a Harshad number because 18 is divisible by (1 + 8) = 9.

num = int(input("Enter a number: "))

x = num
a = 0

while num != 0:
    a += (num % 10)
    num //= 10

if x % a == 0:
    print(f"{x} is a Harshad number")
else:
    print(f"{x} is not a Harshad number.")