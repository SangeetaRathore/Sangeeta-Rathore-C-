# 1. Write a python program to find maximum between two numbers.

c = int(input())
b = int(input())
if > b:
  print("max =", a)
else:
  print("max =", b)



# 2. Write a python program to find maximum between three numbers.

a = int(input())
b = int(input())
c = int(input())
if a > b:
  max = a
else:
  max = b
if max > c:
  print("Max = ", max)
else:
  print("Max = ", c)




# 3. Write a python program to check whether a number is negative, positive or zero.

a = int(input())
if a < 0:
  print("It is a negative number")
elif a == 0:
  print("It is zero")
else:
  print("It is a positive")



# 4. Write a python program to check whether a number is divisible by 5 and 11 or not.

a = int(input("Enter the number = "))
if (a % 5 == 0) & (a % 11 == 0):
  print("It is divisible")
else:
  print("It is not divisible")



# 5. Write a python program to check whether a number is even or odd.

a = int(input("Enter the number = "))
if a % 2 == 0:
  print("The nummber is EVEN")
else:
  print("The nummber is ODD")



# 6. Write a python program to check whether a year is leap year or not.

y = int(input("Enter the number = "))
if y > 0:
  if (y % 4 == 0) & (y % 100 != 0):
    print("leaf year")
  elif y % 400 == 0:
    print("leaf year")
  else:
    print("not leaf year")
else:
  print("invalid")



# 7. Write a python program to check whether a character is an alphabet or not.

letter = input()
b = len(letter)
if b == 1:
  if (letter >= "a") and (letter <= "z"):
    print("alphabet")
  elif (letter >= "A") and (letter <= "Z"):
    print("alphabet")
  else:
    print("not an alphabet")
else:
  print("invalid")




# 8.Write a python program to input any alphabet and check whether it is vowel or consonant.

sap = input()
l = len(sap)
if l == 1:
  if (sap >= "a") and (sap <= "z") or (sap >= "A") and (sap <= "Z"):
    if sap in ("A", "I", "O", "U", "E") or sap in ("a", "o", "i", "u", "e"):
      print("vowel")
    else:
      print("consonant")
  else:
    print("not an alphabet")
else:
  print("invalid")



# 9. Write a python program to input any character and check whether it is alphabet, digit or special character.

a = input("enter element = ")
if a >= "a" and a <= "z" or a >= "A" and a <= "Z":
  print("alphabet")
elif a >= "0" and a <= "9":
  print("digit")
else:
  print("special character")



# 10. Write a python program to check whether a character is uppercase or lowercase alphabet.

letter = input()
l = len(letter)
if l != 1:
  if (letter >= "a") and (letter <= "z"):
    print("LOWERCASE")
  elif (letter >= "A") and (letter <= "Z"):
    print("UPPERCASE")
  else:
    print("Not a Character")
else:
  print("invalid")



# 11. Write a python program to input week number and print week day.

a = int(input("Enter the number = "))
if a > 0 and a <= 7:
  if a == 1:
    print("sunday")
  elif a == 2:
    print("Monday")
  elif a == 3:
    print("Tuesday")
  elif a == 4:
    print("Wednesday")
  elif a == 5:
    print("Thursday")
  elif a == 6:
    print("Friday")
  else:
    print("Saturday")
else:
  print("invalid")



# 12. Write a python program to input the month number and print the number of days in that month.

a = int(input())
if a >= 0 and a <= 12:
  if a in (1, 3, 5, 7, 8, 10, 11):
    print("Days = 31")
  elif a == 2:
    print("28 or 29")
  else:
    print("Days = 30")
else:
  print("invalid")



# 13. Write a python program to count the total number of notes in a given amount.

amount = int(input())
sm = 0
if (amount > 0):
  if amount >= 2000:
    sm += amount // 2000
    amount = amount % 2000
  if amount >= 500:
    sm += amount // 500
    amount = amount % 500
  if amount >= 200:
    sm += amount // 200
    amount = amount % 200
  if amount >= 100:
    sm += amount // 100
    amount = amount % 100
  if amount >= 50:
    sm += amount // 50
    amount = amount % 50
  if amount >= 10:
    sm += amount // 10
    amount = amount % 10
  if amount >= 5:
    sm += amount // 5
    amount = amount % 5
  if amount >= 2:
    sm += amount // 2
    amount = amount % 2
  if amount >= 1:
    sm += amount // 1
    amount = amount % 1
  else:
    print("Total notes = ", sm)
else:
  print("invalid")



# 14. Write a python program to input angles of a triangle and check whether triangle is valid or not.

a = int(input("1st angle = "))
b = int(input("2nd angle = "))
c = int(input("3rd angle = "))
sm = a + b + c
if a > 0:
  if b > 0:
    if c > 0:
      if sm == 180:
        print("Valid Triangle")
      else:
        print("invalid")
    else:
      print("invalid")
  else:
    print("invalid")
else:
  print("invalid")



# 16. Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("1st side = "))
b = int(input("2nd side = "))
c = int(input("3rd side = "))
if a > 0:
  if b > 0:
    if c > 0:
      if (a + b > c) and (b + c > a) and (c + a > b):
        if a == b and b == c:
          print(" Eqiuateral Triangle")
        elif a == b or b == c:
          print(" Isoscale Triangle")
        else:
          print("Scalene Traiangle")
      else:
        print("invalid Triangle")
    else:
      print("invalid")
  else:
    print("invalid")
else:
  print("invalid")



# 17. Write a python program to calculate profit or loss.

a = int(input("Sp = "))
b = int(input("Cp = "))
if a > b:
  c = a - b
  print("Profit = ", c)
else:
  c = b - a
  print("Loss = ", c)



# 18 . Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

a = int(input("Enter the marks of Physics = "))
b = int(input("Enter the marks of Chemistry= "))
c = int(input("Enter the marks of Biology = "))
d = int(input("Enter the marks of Mathematics = "))
e = int(input("Enter the marks of Computer = "))
sum = a + b + c + d + e
per = sum / 5
if per >= 90:
  print("Grade = A")
elif per >= 80:
  print("Grade = B")
elif per >= 70:
  print("Grade = C")
elif per >= 60:
  print("Grade = D")
elif per >= 40:
  print("Grade = E")
else:
  print("Grade = F")




# 19 . Write a python program to input basic salary of an employee and calculate its Gross salary according to following:

salary = int(input("Enter the salary = "))
if salary <= 10000:
  hra = (salary * 20) / 100
  da = (salary * 80) / 100
  b = salary + hra + da
elif salary <= 20000:
  hra = (salary * 25) / 100
  da = (salary * 90) / 100
  b = salary + hra + da
else:
  hra = (salary * 30) / 100
  da = (salary * 95) / 100
  b = salary + hra + da
print(b)



# 20. Write a python program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit = int(input())
if unit <= 50:
  t = unit * 0.50
  sur = t / 5
elif unit <= 150:
  b = unit - 50
  t = b * 0.75 + 25
elif unit < 250:
  b = unit - 150
  t = b * 1.2 + 100
else:
  b = unit - 250
  t = b * 1.5 + 220
sur = t / 5
bill = sur + t
print(bill)




# 21 . A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and print total cost for user.

a = int(input("Enter the quantity ="))
b = a * 100
if b > 1000:
  b -= (b * 10) / 100
  print('Total cost = ', b)
else:
  print("Total cost = ", b)




#22. A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years. Ask users for their salary and year of service and print the net bonus amount.

year = int(input("Year = "))
salary = int(input("Salary = "))
if year > 5:
  salary += salary / 20
  print("salary = ", salary)
else:
  print('salary = ', salary)




# 23. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
#  Ask user to enter marks and print the corresponding grade

marks = int(input("Marks = "))
if marks < 25:
  print("F")
elif marks <= 45:
  print("E")
elif marks <= 50:
  print("D")
elif marks <= 60:
  print("C")
elif marks <= 80:
  print("B")
else:
  print("A")



  
#24 .Take the age of 3 people by user and determine oldest and youngest among them.#

a = int(input())
b = int(input())
c = int(input())
if a > b:
  max = a
  min = b
else:
  max = b
  min = a
if max > c:
  old = max
  d = c
else:
  old = c
  d = max
if min > d:
  young = d
else:
  young = min
print("old = ", old, "\nyoung = ", young)



# 25. A student will not be allowed to sit in an exam if his/her attendance is less than 75%.Take following input from the user. Number of classes held. Number of classes attended. And print, percentage of class attended. Is the student is allowed to sit in the exam or not.

a = int(input(" enter the no. attendence = "))
b = int(input(" enter the no. class held = "))
per = (a / b) * 100
if per > 75:
  print("Percentage = ", per, "%", ", Allow")
else:
  print("Percentage = ", per, "%", " , Don't Allow")




#  29.  Write a program to check whether a person is eligible for voting or not. (accept age from user)

a = int(input("Age ="))
if a >= 18:
  print("Eligible")
else:
  print(" Not Eligible")




# 30 . Write a program to check whether a number is divisible by 7 or not.

a = int(input("Enter the number ="))
if a % 7 == 0:
  print(" It is divisible by 7")
else:
  print(" It is not divisible by 7")




# 31. Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye"

a = int(input("Enter the number ="))
if a % 5 == 0:
  print("Hello")
else:
  print("Bye")



# 33.  Write a program to display the last digit of a number.

a = int(input("Enter the number ="))
if a != 0:
  b = a % 10
  print('Last digit = ', b)
else:
  print("invalid")




# 34 .  Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

a = int(input("Enter the number ="))
if a != 0:
  b = a % 10
  if b % 3 == 0:
    print("Divisible by 3")
  else:
    print("Not divisible by 3")
else:
  print("invalid")



# 40 . Write a program to check whether a number entered is a three digit number or not.

a = int(input("Enter the number ="))
if a > 99 and a < 1000:
  print('It is three digits number')
else:
  print('It is not three digits number')
