# ------------------------------------------------------------
# Variables - Basic Input & Output
# ------------------------------------------------------------

# Variables to store age, college and name
# name = input(" Enter your name")
# age = int(input("Enter your age"))
# college = input(" Enter your college ")
# print("MY name is ", name, " i am ", age, " Years old ", " i Study in  ", college)

# ------------------------------------------------------------
# Arithmetic Operations - Sum, Difference, Product, Quotient
# ------------------------------------------------------------

# a = int(input(" Enter num1 "))
# b = int(input(" Enter num2"))
# sum = a+b
# product=a*b
# diff=a-b
# q = a//b
# print(" Sum is ", sum)
# print(" Product is ",product )
# print(" difference is  ", diff)
# print(" The quotient ",q)

# ------------------------------------------------------------
# Variable Update - Increase by 10, then Multiply by 2
# ------------------------------------------------------------

# x = int(input("Enter no. "))
# y = x+10
# z=2*y
# print(z)

# ------------------------------------------------------------
# Chained Updates - Add 5, then Multiply by 2
# ------------------------------------------------------------

# x=int(input(" Enter value"))
# x=x + 5
# x = x*2
# print(x)

# ------------------------------------------------------------
# ------------------------------------------------------------
# Tough Questions
# ------------------------------------------------------------

# a=5, b=a, a=12, b=b+3 - Explain Output
# a=5 #5 is stored
# b=a # value of a in b
# a=12 # 5 changed to 12
# b=b+3 #new value i.e 3+5 in b
# print(a,b)

# ------------------------------------------------------------
# Calculate Price After Discount
# ------------------------------------------------------------

# price = int(input("Enter price : "))
# discount = int(input("Enter discount "))
# dis = (price*discount)/100
# print(price-dis)

# ------------------------------------------------------------
# Sum of Digits in a 3-Digit Number
# ------------------------------------------------------------

# a = int(input(" Enter 3 digit no. "))
# d1= a//100 #Used to find quotient
# d2= (a//10)%10 # 1st Quotient then remainder
# d3= a%10 #remainder
# sum = d1+d2+d3
# print(sum)

# ------------------------------------------------------------
# Swap Two Numbers Without Temp Variable
# ------------------------------------------------------------

# x=8
# y=3
# x=x+y
# y=x-y
# x=x-y
# print(x,y)

# ------------------------------------------------------------
# Convert Seconds to Minutes and Remaining Seconds
# ------------------------------------------------------------

# s=int(input("Enter in secs "))
# m=s//60
# ss=s%60
# print(m," minutes ", ss, " Secs")

# ------------------------------------------------------------
# Convert Input to Float, Add 2.5, Print Results & Types
# ------------------------------------------------------------

a=float(input("Enter a number "))
New_a=2.5+a
print(type(a))
print(type(New_a))
print(New_a)

# ------------------------------------------------------------
# Bank Balance Calculator - Deposit, Expense, Interest
# ------------------------------------------------------------

balance =int(input("Enter amount of balace"))
depo = int(input("Enter amount of deposite "))
expen=int(input("Enter amt of expences "))

total= balance + depo - expen
interest = (total*5)/100
print(total+interest)

# ------------------------------------------------------------