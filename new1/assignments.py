# # assignment_no.1

age = int (input ("enter your age :"))
if age < 18:
    print ("you are not eligible to vote !")
else :
    print ("you are eligible to vote !")

# # assignment_no.2

num1 = int (input ("enter first number  :"))
num2 = int (input ("enter second number  :"))
num3 = int (input ("enter third number  :"))
if num1 > num2 & num1 > num3 :
    greatest_num=num1
elif num2 > num1 & num2 > num3 :
    greatest_num=num2
else :
        greatest_num=num3

# assignment_no.3

num1 = int (input ("enter first number  :"))
num2 = int (input ("enter second number  :"))
if num1 > num2 :
    print ("the largest number is :" , num1)
else:
    print ("the largest number is :" , num2 )

# # assignment_no.4

num = int (input ("enter a number :"))
if (num%2 == 0):
    print ("the given number is even !")
else :
    print ("the given number is odd !")
# assignment_no.5

char1 = str (input ("enter a character  :"))
if (char1.isupper()):
    print (char1.lower())
else :
    print (char1.upper())

# assignment_no.6

year = int (input ("enter a year :"))
if (year%4 == 0):
    print ("the given year is a leap year !")
else :
    print ("the given year is not a leap year !")/

# assignment_no.7

num = int (input ("enter a number :"))
if num < 0 :
    print ("the given number is negative !")
elif num == 0:
    print ("the given number is equal to zero !")
else :
    print ("the given  number is positive !")

# assignment_no.8.

char1 = str (input ("enter a character  :"))
vowels = ("a","e","i","o","u")
if char1 in vowels :
    print ("the given character is a vowel !")
else:
    print ("the given character is not a vowel !")