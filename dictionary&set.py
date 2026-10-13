# ------------------------------------------------------------
#Dictionary and Sets
# ------------------------------------------------------------

# A dictionary is a collection of key-value pairs.
# It stores data in the form of {key: value}.
# Syntax:
 #########my_dict = {"name": "Rahul"}# ------------------------------------------------------------


# A set is an unordered collection of unique elements.
# It does not contain duplicate values.
# Syntax:
# my_set = {1, 2, 3, 4}

#-----------------------------------------------------------------------
#Dictionary to write name and branch
#-----------------------------------------------------------------------

# dict = {"Name": "Rahul", "Branch": "ai&DS"}
# print(dict["Name"])

#-----------------------------------------------------------------------
#To a new Key value pair to the dictionary
#-----------------------------------------------------------------------

# students = {"name ": "Rahul", "branch": "AI&DS"}
# students["age"] = 21
# print(students)

#-----------------------------------------------------------------------
#TO change the value of a key in the dictionary
#-----------------------------------------------------------------------

# Students = {"name ": "Rahul", "branch": "AI&DS", "age": 21}
# Students["age"] = 22
# print(Students)

#-----------------------------------------------------------------------
#To check if a key exists in the dictionary
#-----------------------------------------------------------------------

# students = {"name ": "Rahul", "branch": "AI&DS", "age": 21}
# key = input("Enter a key to check: ")
# if key in students:
#     print("Key exists in the dictionary.")
# else:
#     print("Key does not exist in the dictionary.")

#-----------------------------------------------------------------------
#Student with the highest Marks
#-----------------------------------------------------------------------

# Score = {
#     "aditya": 88,"Shivam ": 99, "Lokesh ": 98
# }
# print(max(Score),max(Score.values()))

#----------------------------------------------------------------------
#count each character in string(it counts repeated char)
#----------------------------------------------------------------------

# text = input("Enter a String ")
# for char in text:
#     print(char,text.count(char),text.find(char))
# #count : counts the number of times a num is repeated
# #find : used to find when a char appeard first time in index

#----------------------------------------------------------------------
#Count each char in Dictionary #Counts how many times it exists
#----------------------------------------------------------------------


# text = "apple"             #Stores the word apple
# count={}                   #Creats a empty dictionary

# for char in text:          #Stores characters in char and creats a loop to go to the next line
#     if char in count:      #checks whether it already exist or No
#         count[char] += 1   #If already exist ex. 'p' then prints 1+1 = 2
#     else:
#         count[char]=1      #If it doesn't then asigns a value of 1
# print(count)               #At the end it's used to display Values


#-----------------------------------------------------------------------
#Creat a dictionary from to lists
#-----------------------------------------------------------------------

# Names=["Rahul","RAj","Aryan","Shreya"] #Listr containing names
# Ages=[18,15,12,19]                     #List containing Ages
# Dict={}                                #Empty Dictionary to store value
# for i in range(len(Names)):            # Starts a loop and Stores value in i 
#     Dict[Names[i]]=Ages[i]             #Used to asign value to both Lists 

# print(Dict)                            # To print dictionary values 


#Easier method---------------------------------------------------------

# Names=["Rahul","RAj","Aryan","Shreya"] 
# Ages=[18,15,12,19]  

# Dict=dict(zip(Names,Ages)) #here Dict is just variable..... dict is to tell to convert it into dictionary... zip basically pairs both lists
# print(Dict)

#-----------------------------------------------------------------------
#Products containing values more then 200
#-----------------------------------------------------------------------

prices = {
    "pen":100, "Bag": 760, "Book":190,"uniforn ": 900 # Dictionary 
}
result = {}                                            #Empty dictionary to store Product>200
for i in prices:                                       # Values of prices stored in i one by one
    if prices[i]>200:                                  # if >200
        result[i]=prices[i]                            # if Prices > 200 it stores it in Result


print(result)