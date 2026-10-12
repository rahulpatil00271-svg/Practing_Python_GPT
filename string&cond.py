#Easy
#_____________________________________________________________________________________________________________________________-

#print name, length, first character and last

# name = input(" Enter name ")
# print(name)

# print(name[0])#for 1st char
# print(name[-1])#for last char

#________________________________________________________________________________________________________________________________

#take name as input print in uppercase lowercase and title

# Name = input("Enter name ")
# print(Name.upper())
# print(Name.lower())
# print(Name.title())

#______________________________________________________________________________________________________________________________________________________-

#Take a sentence and find how many a & A... and only a

# sen= input("Enter a sentence ")

# print(sen.lower().count("a"))#both a and A
# print(sen.count("a"))#only a


#___________________________________________________________________________________________________________________________________________________________-


#To count num of words
# Sen=input("Enter a sentence ")
# words = Sen.split() # splits a sentence whereever there is a space 
# print(len(words))


#______________________________________________________________________________________________________________________________________________________

#Pallindrom code
# a = input("Enter a word ")

# if a == a[::-1]: #reads the code backwards #Basically Reverses a string
#     print("Palindrome ")

# else:
#     print("Not a palindrome ")


# #Pallimdrome using copy and reverse(works only for list not string)
# word = list(input("Enter a word "))
# word_copy = word.copy()
# word_copy.reverse()

# if word == word_copy:  #This also counts spaces 
#     print("Palindrome ")
# else:
#     print("Not a pallindrome ")


#____________________________________________________________________________________________________________________________________________________________-

#excahnge the first and last char

# word = input("Enter a word ")
# new_w = word[-1] + word[1:-1] + word[0] #adds last, mid and first 
# print(new_w)

#___________________________________________________________________________________________________________________________________________________________________

#Cheack whether a char is vowel or consonant

# character = input("Enter a char ")
# if character in "aeiou" :
#     print("Vowel ")
# else:
#     print("Not a vowel ")


#_____________________________________________________________________________________________________________________________________________________________________________

# #To check no. of char in password n print length
# password = input("Enter pass ")
# print("Length", len(password))

#__________________________________________________________________________________________________________________________________________________________________________

#To remove the spaces

# word = input("Enter a word ") #Enter a word
# new_word= word.replace(" ","") #replaces space with no space
# print(new_word)

#______________________________________________________________________________________________________________________________________________________________________________________________________________________

#__________#IMP Question!!!!!!!!!!!!!!_______#
### TO CHECK WHETHER A STRING CONTAINS BOTH LETTERS AND DIGITS

string = input(" Enter a string ")

has_letter= any(i.isalpha() for i in string ) 
#i or char represents the characters in variable string 
# #isalpha checks alphabates 
# for- starts a loop, i= stores each letter of string, in- inside of something, string- that something is string  
has_digits= any(i.isdigit() for i in string )

if has_letter and has_digits :
    print(" Has both letters and Digits ")

else:
    print(" Doesn,t contain both ")

#any basically goes through and checks whether atleast one condn is true, if true then print True