# Write a program that asks the user to input positive numbers (>= 0) until a negative number is entered. 
# After, output how many positive numbers were entered.

count = 0

while True:
    num = int(input("Please enter a number <negetive number or zero to exit>: "))
    if num <= 0:
        break
    count += 1

print ("There were", count, "positive numbers")



