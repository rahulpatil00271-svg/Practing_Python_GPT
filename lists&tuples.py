# ------------------------------------------------------------
# Loop Syntax - for variable in list, tuple, dictionary
# ------------------------------------------------------------

# Access an Element in Tuple
# num= (12,32,45,76,82)
# print(num[3])

# ------------------------------------------------------------
# Tuple Slicing
# ------------------------------------------------------------

# x=(23,43,44,11,87)
# print(x[0:5])

# ------------------------------------------------------------
# Check if Number Exists in Tuple
# ------------------------------------------------------------

# a=(23,43,21,56,55)
# print(23 in a)
# print(29 in a)

# Check if Number Exists - With User Input
# a = (23,34,22,76,99,39)
# n= int(input(("Enter a number "))) #if int not mentioned it will give error as it treats it as string
# if n in a :
#     print(n," Exist")
# else:
#     print(" Does not exists ")

# ------------------------------------------------------------
# Count Occurrences in Tuple
# ------------------------------------------------------------

# C=(22,33,33,22,11,88,99)
# print(C.count(33))

# ------------------------------------------------------------
# Repeat a Tuple
# ------------------------------------------------------------

# tuple= (22,1,9,31)
# print(tuple*3)

# ------------------------------------------------------------
# For Loop - Print Tuple Elements on Separate Lines
# ------------------------------------------------------------

# t=(23,34,88,91,3,444,132)
# for i in t:
#     print(i)
# # Here no increment i += i required

# ------------------------------------------------------------
# ------------------------------------------------------------
# Count Numbers Greater Than 20
# ------------------------------------------------------------

# t=(2,222,23,45,11,2,3,7,111,87,21)
# count = 0 # count is a variable used to track how many numbers satisfy the condition
# for n in t: # takes each number from t, stores in n
#     if n>20:
#        count += 1 # if n greater than 20 then increment by 1 (can also be written as count = count+1)
# print(count) # prints how many times count stopped at n>20

# ------------------------------------------------------------
# Print Numbers Greater Than 23
# ------------------------------------------------------------

# t=(2,222,23,45,11,2,3,7,111,87,21)
# for i in t:
#     if i>23:
#         print(i)

# ------------------------------------------------------------
# Count Even Numbers in Tuple
# ------------------------------------------------------------

# Num = (23,24,443,22,16,87,56,997,2124)
# count=0 # counter starts from 0
# for n in Num:
#     if n%2==0:
#         count += 1 # if above is true it stops, and runs again until value is true then stops
# print(count)

# ------------------------------------------------------------
# Reverse a Tuple
# ------------------------------------------------------------

# tuple=(1,3,32,1112,476)
# new_tup=tuple.reverse()
# print(print(new_tup))

# # Method 2 - Slicing
# tuple=(12,23,321,46,577,44)
# new_tup=tuple[::-1]
# rt=tuple[-1:-5] # This doesn't work because default step is +1
# print(new_tup)
# print(rt) # prints blank ()

# ------------------------------------------------------------
# Convert List to Tuple
# ------------------------------------------------------------

# L=[12,33,49,44,40]
# x=tuple(L)
# print(L) # Prints List
# print(x) # prints tuple

# ------------------------------------------------------------
# Check if Every Number is Positive (Greater Than Zero)
# ------------------------------------------------------------

# numbers = (11, 33, 1, 84, 20, 49, 25, 81)  # A collection of numbers to check

# # Assume all numbers are positive until we find one that isn't
# all_positive = True

# # Look at each number one by one
# for n in numbers:
#     # If we find a number that is zero or negative
#     if n <= 0:
#         # Mark that not all numbers are positive
#         all_positive = False
#         # Stop checking - we already know the answer
#         break

# # Show the result based on what we found
# if all_positive:
#     print("All numbers are positive")
# else:
#     print("At least one number is not positive")

# ------------------------------------------------------------
#Lists
#-------------------------------------------------------------

##############QuestionS#############
#-----------------------------------
#TO check a element exists 
#-----------------------------------
###########USING FOR LOOP#########

# numbers = [233,34,58,4,2,868,21]
# n= int(input("Enter a number "))
# for i in numbers:
#     if i == n :
#         print("exists")
#         break
# else:
#     print("Doesn't exists ")

#############NO FOR LOOP#################

# numbers = [233,34,58,4,2,868,21]
# n= int(input("Enter a number "))
# if n in numbers:
#     print("Exist ")
# else:
#     print("Doesn't exist ")

#-------------------------------------------------------------------
#To add an element to list
#-------------------------------------------------------------------

# numbers = []
# numbers.append(23)#append to add 1 element
# numbers.extend([22,56,33,21]) #to add multiple elements to list
# print(numbers)


#-------------------------------------------------------------------
#To replace an element
#-------------------------------------------------------------------

#________Gives Error as replace is strings method___________

# numbers=[22,43,22,17,93]
# new_num = numbers.replace(22,39)
# print(new_num)

#_________lists method_____________

# numbers=[22,43,22,17,93]
# numbers.remove(22)
# numbers.append(35)
# print(numbers)

#----------------------------------------------------------------------
#SUM of elemts of lists
#----------------------------------------------------------------------

# numbers=[22,43,22,17,93]
# print(sum(numbers))

#----------------------------------------------------------------------
#TO print Even numbers
#----------------------------------------------------------------------

# numbers=[22,24,778,43,22,17,93]

# for i in numbers:
#     if i%2==0:
#         print(i)
#         i+=1

#-----------------------------------------------------------------------
# To count Even numbers
#-----------------------------------------------------------------------

# A list of numbers to check - mix of even and odd numbers
numbers = [22, 43, 212, 468, 17, 93]

# Counter starts at zero - we haven't found any even numbers yet
count = 0

# Look at each number one by one using a for loop
for i in numbers:
    # Check if current number is even
    # The modulo operator (%) gives the remainder after division
    # If remainder is 0 when divided by 2, it's an even number
    if i % 2 == 0:
        # We found an even number, so print it
        print(i)
        # Increase counter by 1 (same as: count = count + 1)
        count += 1

# After checking all numbers, print the total count
# Expected output: 3 (because 22, 212, 468 are even)
print(count)

# ------------------------------------------------------------