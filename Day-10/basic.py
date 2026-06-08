#positive or negative
'''n = int(input())
if n<0:
    print("Negative")
elif n>0:
    print("Positive")
else:
    print("Zero")'''   

#Even or odd
'''n = int(input())
if n%2 == 0:
    print("Even")
else:
    print("Odd")'''

#Divisible by 5 
''''n = int(input())
if n%5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")'''
#Divisible by 3 and 7
''''n = int(input())
if n%3 == 0 and n%7 == 0:
    print("Divisible by 3 and 7")
else:
    print("Not divisible by 3 and 7")'''
#Leap year
''''year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")'''
#marks
''''marks = int(input())
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")'''
#3digit
''''num = int(input())
if num >= 100 and num <= 999:
    print("3 digit number")
else:
    print("Not a 3 digit number")'''
#character is vowel
'''''char = input()
if char in 'aeiouAEIOU':
    print("Vowel")  
else:
    print("Not a vowel")'''
#gratest of 2 numbers
'''num1 = int(input())
num2 = int(input())
if num1 > num2:
    print("Greatest is", num1)
else:
    print("Greatest is", num2)'''
#smallest of 2 numbers
'''num1 = int(input())
num2 = int(input())
if num1 < num2:
    print("Smallest is", num1)
else:
    print("Smallest is", num2)'''
#number is zero
'''num = int(input())
if num == 0:
    print("Number is zero")
else:
    print("Number is not zero")'''
#is number is muliple of 10
'''num = int(input())
if num % 10 == 0:
    print("Number is multiple of 10")
else:
    print("Number is not multiple of 10")'''
#age is eligible for vote (18+)
'''age = int(input())
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")'''
#if number is between 1 to 100
num = int(input())
if num >= 1 and num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is not between 1 and 100")