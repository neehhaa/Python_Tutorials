str1 = "hello world"
str2 = "PYTHON"
str3 = "Lets"
str4 = "beGIN"


print(str1 * 3)  # REPETITION
# hello worldhello worldhello world

print(str1 + str2 + str3 + str4)  # CONCATENATION
# hello worldPYTHONLetsbeGIN

print('Hello world: %s' % str1)  # STRING FORMATTING
# Hello world: hello world


# BUILT-IN STRING FUNCTIONS


# I. CASE


# 1. CAPITALIZE 1ST LETTER ONLY
str = str1.capitalize()         # str1 = "hello world"
print(str)      # Hello world

# 2. KEEPS ONLY 1ST LETTER CAPITAL OF ALL THE WORDS
str = str4.title()      # str4 = "beGIN"
print(str)              # Begin
str = str1.title()      # str1 = "hello world"
print(str)              # Hello World

# 3. CONVERTS ALL THE STRING INTO LOWER CASE
str = str2.lower()       # str2 = "PYTHON"
print(str)     # python
str = str4.lower()      # str4 = "beGIN"
print(str)     # begin

# 4. CONVERTS ALL THE STRING INTO UPPER CASE
str = str4.upper()      # str4 = "beGIN"
print(str)      # BEGIN
str = str1.upper()      # # str1 = "hello world"
print(str)          # HELLO WORLD

# 5. CHANGES CASE OF ALL CHARACTER
str = str2.casefold()       # str2 = "PYTHON"
print(str)      # python

# 6. INVERTS ALL THE CASES(LOWER<-->UPPER)
str = str1.swapcase()      # str1 = "hello world"
print(str)      # HELLO WORLD
str = str4.swapcase()    # str4 = "beGIN"
print(str)      # BEgin


# II. ENCODE AND DECODE


# 1. FOR ENCODING AND DECODING
str5 = str1.encode()        # str1 = "hello world"
print(str5)     # b'hello world'

str6 = str5.decode()
print(str6)     # hello world


# III. ALIGNMENT AND PADDING

# 1. USED FOR ALIGNMENT(WIDTH IS IMPORTANT WHILE FILL CHAR IS OPTIONAL)

str = str1.center(20, '@')      # str1 = "hello world"
print(str)      # @@@@hello world@@@@@

# 2. PADS CHARACTER TO RIGHT SIDE (STRING ON LEFT), CAN ALSO DEFINE WIDTH
str = str1.ljust(20, '$')
print(str)      # hello world$$$$$$$$$

# 3. PADS CHARACTER TO LEFT SIDE (STRING ON RIGHT), CAN ALSO DEFINE WIDTH
str = str1.rjust(20, '$')
print(str)      # $$$$$$$$$hello world

# 4. ZERO PADDING FROM LEFT
str = str1.zfill(20) # str1 = "hello world"
print(str)      # 000000000hello world


# 5. REMOVES WHITE SPACES OR CHAR
char_str = "$$$hello world$$$$$"
str = char_str.strip('$')
print(str)      # hello world

# 6. REMOVES WHITE SPACES OR CHAR FROM LEFT SIDE
str = char_str.lstrip('$')
print(str)      # hello world$$$$$

# 7. REMOVES WHITE SPACES OR CHAR FROM RIGHT SIDE
str = char_str.rstrip("$")
print(str)      # $$$hello world


# IV. STRING, VALUE FORMATING


# STRING FORMATTING

str = "{} {} {} with {}".format(str1, str3, str4, str2)    # str1="hello world",str2="PYTHON",str3="Lets",str4="beGIN"
print(str)      # hello world Lets beGIN with PYTHON

val = 10
print("decimal :  {0:d}".format(val))   # 10
print("hex : {0:x}".format(val))        # a
print("octal : {0:o}".format(val))      # 12
print("binary : {0:b}".format(val))     #1010


# V. STRING LENGTH, COUNT, INDEX, FIND


# 1. RETURNS THE LENGTH OF THE STRING
str = len(str1)     # str1 = "hello world"
print(str)      # 11


# 2. TO COUNT THE STRING WITH BEGIN AND END INDEX
str = str1.count('l', 3, 20)     # str1 = "hello world"
print(str)      # 2


# 3. IF THE STRING STARTS WITH THE DEFINED STRING RETURNS TRUE ELSE FALSE
str = str1.startswith("h",0,9)
print(str)  # True

# 4. PRINTS TRUE IF IT ENDS WITH THE DEFINED SUFFIX
str = str1.endswith('o', 4, 5)      # str1 = "hello world"
print(str)      # True


# 5. FINDS THE INDEX OF A LETTER OR WORD *RETURNS -1 IF STRING NOT FOUND*
str = str1.find('ld', 1, 15)        # str1 = "hello world"
print(str)      # 9

# 6. INDEX FINDING (WORKS SAME AS FIND) *RETURNS TRACEBACK IF STRING NOT FOUND*
str = str1.index("world", 5, 11)        # str1 = "hello world"
print(str)      # 6

# 7. FINDS THE SUBSTRING RETURNS THE HIGHEST INDEX(RHS) (IF NOT FOUND RETURNS -1)
str = str1.rfind("l")        # str1 = "hello world"
print(str)      # 9

# 8. FINDS THE SUBSTRING RETURNS THE HIGHEST INDEX(RHS) (IF NOT FOUND RETURNS TRACEBACK)
str = str1.rindex("l")        # str1 = "hello world"
print(str)      # 9


# VI. STRING JOINING


# JOINS THE STRING IN ITERABLES

no_space = ""
colon = ":"

list1 = ['1', '2', '3', '4']
str = colon.join(list1)
print(str)      # 1:2:3:4

list2 = ['h', 'e', 'l', 'l', 'o']
str = no_space.join(list2)
print(str)      # hello


# VII. REPLACES CHARACTER

# USED TO REPLACE CHARACTER
str = str1.replace("world", "work")      # str1 = "hello world"
print(str)                               # hello work

str_rep = "AMONG PYTHON, JAVA, C, C++.JAVA IS THE WEB FRAMEWORK"
str = str_rep.replace("JAVA", "DJANGO", 1)      # ONLY REPLACES ONE WORD
print(str)      # AMONG PYTHON, DJANGO, C, C++.JAVA IS THE WEB FRAMEWORK

str = str_rep.replace("JAVA", "DJANGO")
print(str)      # AMONG PYTHON, DJANGO, C, C++.DJANGO IS THE WEB FRAMEWORK


# VIII. REMOVES THE DEFINED CHARACTER


# 1. SPLITS THE STRINGS AND CREATES A LIST (TOTALLY REMOVES THE STRING)
str_rem = "Django is a framework"
str = str_rem.split("Django")
print(str)      # ['', ' is a framework']

str = str_rem.split("a", maxsplit=1)
print(str)      # ['Dj', 'ngo is a framework']

# 2. SPLITS THE STRINGS FROM RIGHT  AND CREATES A LIST
str = str_rem.rsplit("a", maxsplit=1)
print(str)      # ['Django is a fr', 'mework']


# IX. SEPARATION


# 1. SEPARATION OF CHAR
str = str1.partition("el")       # str1 = "hello world"
print(str)      # ('h', 'el', 'lo world')

str = str1.partition("hello")
print(str)      # ('', 'hello', ' world')

str = str1.partition("world")
print(str)      # ('hello ', 'world', '')

# 2. MAKES PARTITION BETWEEN THE ONE WHICH IS DECLARED AND REST OTHER
str = str_rem.rpartition("is")
print(str)      # ('Django ', 'is', ' a framework')


# X. LINES AND SPACES


# 1. REMOVES NEW LINES AND RETURNS A LIST
str_new_lines = 'python\ntutorials\nby\nneha'
print(str_new_lines)
'''
python
tutorials
by
neha
'''
str = str_new_lines.splitlines()
print(str)  # ['python', 'tutorials', 'by', 'neha']
print(" ".join(str))    # python tutorials by neha

'''
' '  - WHITE SPACE
'\t' - HORIZONTAL TAB
'\n' - NEW LINE
'\v' - VERTICAL TAB
'\f' - FEED
'\r' - CARRIAGE RETURN

'''


# 2. CREATES SPACES IN BETWEEN USING \t
str7 = 'python\ttutorials'
str8 = str7.expandtabs(16)
print(str8)        # python          tutorials


# 3. RETURNS TRUE IF STRING DOESN'T CONTAIN ANY SPECIAL SPACE CHARACTER

str = str7.isprintable()    # str7 = 'python\ttutorials'
print(str)      # False


# XI. TRUE AND FALSE USING IS


# 1. RETURNS TRUE IF STRING IS AN ALPHABET AND NUMERIC
str9 = "24x7"
str = str9.isalnum()
print(str)      # True

# 2. RETURNS TRUE ONL IF STRING IS AN INTEGER
str10 = "4.3"
str = str10.isdecimal()
print(str)      # False
str11 = "555"
str = str11.isdecimal()
print(str)      # True

# 3. RETURNS TRUE IF STRING IS AN ALPHABET
str = str2.isalpha()         # str2 = "PYTHON"
print(str)      # True

# 4. RETURNS TRUE IF STRING IS DIGIT
str = str11.isdigit()      # str11 = "555"
print(str)      # True

# 5. RETURNS TRUE IF STRING IS 'True or False'
str12 = "True"
str = str12.isidentifier()
print(str)    # True
str13 = "False"
str = str13.isidentifier()
print(str)      # True

# 6. RETURNS TRUE IF STRING IS IN LOWER CASE
str14 = "hello"
str = str14.islower()
print(str)      # True

# 7. RETURNS TRUE IF STRING IS AN INTEGER NOT FLOAT
str = str10.isnumeric()     # str10 = "4.3"
print(str)      # False
str = str11.isnumeric()     # str11 = "555"
print(str)      # True

# 8. RETURNS TRUE IF STRING IS IN UPPER CASE
str = str2.isupper()         # str2 = "PYTHON"
print(str)      # True

# 9. RETURNS TRUE IF 1ST CHAR IS UPPER AND REST LOWER
str = str3.istitle()           # str3 = "Lets"
print(str)      # True

# 10. RETURNS TRUE IF WHITE SPACE
wb = " "
str = wb.isspace()
print(str)      # True