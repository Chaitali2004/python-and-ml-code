
# ques 1 - Write a program that takes two numbers as input and prints their sum.
input1 = int(input("please enter the first number:"))
input2 = int(input("please enter the second number:"))
totalsum = input1 + input2
print("the sum of two number is: ", totalsum)

# ques 2 - Write a python program that checks whether a given number is even or odd.
input1 = (int(input("please enter the number: ")))
if input1 %2==0:
    print(input1,"is an even number.")

else:
    print(input1,"is an odd number.")


# ques 3- Write a python program that calculates the factorial of a given number
from math import factorial
input1 = (int(input("Please enter the number: ")))
fact1 = input1*factorial(input1-1)
print("The factorial of the number is: ",fact1)


# ques 4 - Write a program that asks the user for their name and then prints a greeting message
input1 = input("Hi, Please enter your name:")
print("Nice to meet you",input1,"I hope you’re having a pleasant day.")


# ques 5 -  Write a program that takes a string input from the user and writes it to a text file
with open("output.txt", "w") as file:
  input1 = input("Enter the string you want to write to the file: ")
  file.write(input1)
print("Successfully wrote to the file!")


# ques 6 - Write a program that reads the content of a text file and prints it to the console.
with open("output.txt", "r") as file:
  data = file.read()
  print("the content of the file is: ",data)
print("Successfully read to the file!")



# ques 7 - Write a python program that takes a string as input and returns its length.
input1 = input("Please enter a string: ")
print("The length of the string is: ",len(input1))



# ques 8 -Write a python program that concatenates two strings and returns the result.
input1 = input("Please enter the first string: ")
input2 = input("Please enter the second string: ")
combine = input1 + input2
print("the sum of two number is: ", combine)


# ques 9 - Write a python program that checks if a substring is present in a given string.
given_string = "hello, here we are learning python ml workshop."
input1 = input("Please enter a substring: ").lower()

if input1 in given_string.lower():
  print("The substring -",input1,"- is present in the string.")
else:
  print("The substring -",input1,"- is not present in the string.")


# ques 10 : Write a python program that converts a given string to uppercase.
input1 = input("Please enter a substring: ").upper()
print(input1)



# ques 11 : Write a python program that generates the first n numbers in the Fibonacci sequence
def fibonacci(n):
  if n < 0:
    print("Invalid input. Fibonacci series starts from 0.")
    return None
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number of terms in the Fibonacci series: "))
for i in range(number):
  print(fibonacci(i), end=" ")


# ques 12 - Write a python program that calculates the sum of the digits of a given number
n = int(input("Please enter the number digits you want to add: "))
sum = 0
for i in range(n):
    data = int(input("enter the digits: "))
    sum = sum+data
print ("The sum of all the digits are",sum)




# ques 13 - Write a program that asks the user for their birth year and calculates their age
from datetime import date
birthyear = int(input("Please enter you birth year: "))
currentyear = date.today().year
age = currentyear- birthyear
print("your age is ",age)




# ques 14 - Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = []
while True:
  line = input("Enter a line (or press Enter to finish): ")
  if not line:  # Check if the line is empty (equivalent to line == "")
    break
  lines.append(line)
print("Here are the lines you entered:")
# here an range is run to print al line lines by lines
for line in lines:
  print(line)

# 15. Write a program that reads data from a CSV file and prints it to the console.
import csv
with open('Fruits.csv','r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

# 16. Write a program in python that counts the frequency of each character in a string.
def char_frequency(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
            return char_counts

text = "Hello, world! This is a test string."
char_counts = char_frequency(text)
for char, count in char_counts.items():
  print(f"Character '{char}': {count} occurrences")


# 17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
text = "this is a string"
title_text = text.title()
print(title_text)

# 18. Write a python program that checks if two strings are anagrams of each other.
string1 = "cinema".lower().replace(" ", "")
string2 = "iceman".lower().replace(" ", "")

if len(string1) != len(string2):
  print("Not anagrams: Strings have different lengths")
  exit()

char_counts1 = {}
for char in string1:
  char_counts1[char] = char_counts1.get(char, 0) + 1

char_counts2 = {}
for char in string2:
  char_counts2[char] = char_counts2.get(char, 0) + 1

if char_counts1 != char_counts2:
  print("Not anagrams: Character frequencies differ")
else:
  print("Anagrams: Strings have the same character frequencies")


# 19. Write a python program that removes all punctuation from a given string.
text = "This is a string! With some punctuation or without some?"
punctuation = "!@#$%^&*()-_=+[{]}|;:'\",<.>/? "
new_text = ""
for char in text:
  if char not in punctuation:
    new_text += char

print(new_text)

# 20. Write a python program that takes a list of numbers and returns their sum
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
  total += number
print(f"The sum of the numbers is: {total}")  # Output: The sum of the numbers is: 15
