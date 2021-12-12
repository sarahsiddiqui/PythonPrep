# Write a program that asks the user to input any four numbers. 
# Output the four numbers in order from largest to smallest with the minimum amount of inequalities possible.

num1 = float(input("Please enter a number: ")) 
num2 = float(input("Please enter a number again: ")) 
num3 = float(input("Please enter another number: "))
num4 = float(input("Please enter one last number: "))  

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
if num2 > num3:
    temp = num2
    num2 = num3
    num3 = temp
if num3 > num4:
    temp = num4
    num4 = num3
    num3 = temp
if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp
    
print (num4, num3, num2, "and", num1)