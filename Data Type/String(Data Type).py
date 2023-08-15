''' string data type'''

name='sathishkumar'
print(name[1])


''' slicing '''
word="hello sathishkumar How Are You"

print(word[0:5])
print(word[0:])
print(word[6:12])

print(word[-1])
print(word[-15:-1])
print(word[:-1],)
print(word[-1:-15],)    # it s does not work it create an empty space


print(word[5:-5])
print(word[-20:20])

print(word[::-1])
print(word[:5:-1])

''' Modify on string using method function '''

Name="sathishkumar"
NAME="   SATHISHKUMAR"

print(Name.upper())                                                     # the function change lower to upper
print(NAME.lower())                                                     # The method change upper to lower
print(NAME.strip())                                                     # Remove the white space

txt='hello world wellcome my world'
tex_1="Hello Sathishkumar How Are You"
print(txt.capitalize())                                                 # upper case the first letter in this sentence
print(tex_1.casefold())                                                 # Make the String lower case.

TXT="umaiyal"
print(TXT.center(200))                                                  # Print the word its take up the space 200 characters

APPLE="i like a movie the movie teach lot of thing."
print(APPLE.count("movie"))                                            # Return the number of times the value "movie" appears in the string
print(APPLE.encode())                                                  # Return an encouded version of the string
print(APPLE.endswith("."))                                             # Returns true if the string ends with the specified value like("." ",")
print(APPLE.endswith(","))

Apple="H\te\tl\tl\to"
print(Apple.expandtabs(5))                                             # Set the tab size of the string

print(APPLE.find("movie"))                                             # Return the position of where it was found
print(APPLE.index("movie"))                                            # Return the position of where it was found

''' formate method '''

price="This phone amounr is {}".format(1000)
print(price)

price="This phone amounr is {Rs:.2f}".format(Rs=10000)
print(price)

friend="hello {} and {}".format("sathish","umaiyal")
print(friend)

friend_1="hello {name1} and {name2}".format(name1="sathish",name2='umaiyal')
print(friend_1)

friend_2="hello {1} and {0}".format("sathish","umaiyal")
print(friend_2)

alpha="sathish44399"                                                                  # check if all the characters in the text are alphanumeric
alpha1="sathish  @#$%^!&&*()"                                                         # these are not characters
print(alpha.isalnum())
print(alpha1.isalnum())

print(alpha.isalpha())                                                                # retur True text has only alpha without number

split="sathish,kumar,sai,saran"
print(split.split(","))

join=['sathish', 'kumar', 'sai', 'saran']
print(",".join(join))

replace="sathish,kumar,sai,saran"
print(replace.replace("sathish","SATHISH"))

