# Acronym creator 
# ________________

inp_string = input("Enter the Phrase or Full form : ") #Taking phrase as an input
list_of_inp_string = inp_string.split()                #Assigning the phrase into list of words using split method of string
acronym = ""                                           #Taking acronym as an empty string so that we can concatenate first letters of each word while iterating the list

for words in list_of_inp_string:                       # Iterating the list
    acronym = acronym + words[0]                       #Concatenating each word's first letter from the phrase 

acronym_in_uppercase = acronym.upper()                 #Assigning the acronym by converting the letters of words in Uppercase using upper method of string
print(acronym_in_uppercase)                            #Printing the acxronym


'''
--------------------------------------------------------------------
Example output:

Enter the Phrase or Full form : Automated Teller Machine
ATM

--------------------------------------------------------------------
'''