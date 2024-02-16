from re import *
text="abaacaaabbABCbbaaa K@$9eyz"
# pattern="[a-z]" # search lowr case(a to z)

# pattern="[A-Z]" UPPER CASE

# pattern="[0-9]" digit 

# pattern="[a-zA-Z0-9]" alphanumeric character

# pattern="[^a-zA-Z]" #exclude all alphabets

# pattern="[^a-zA-Z0-9]" #special char

#                                                predefined character
#pattern="\d" #  search digits
#pattern="\D" #  exclude digits

#pattern="\w" #  alphanumeric characters 
# pattern="\W"  #  special char
#                                                quantifiers

#pattern="a+" # +atleast one a
#pattern="a*" # matches for any number of a
#pattern="a?" # optional
pattern="a{2,3}" #minimum 2 maximum 3


matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())

