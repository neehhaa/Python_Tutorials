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

# CAPITALIZE 1ST CHARACTER
str = str1.capitalize()         # str1 = "hello world"
print(str)      # Hello world


# CHANGES CASE OF ALL CHARACTER
str = str2.casefold()       # str2 = "PYTHON"
print(str)      # python


# USED FOR ALIGNMENT(WIDTH IS IMPORTANT WHILE FILL CHAR IS OPTIONAL)
str = str1.center(10, '#')      # str1 = "hello world"
print(str)      # hello world


# TO COUNT THE STRING WITH BEGIN AND END INDEX
str = str1.count('l', 3, 6)     # str1 = "hello world"
print(str)      # 1

# FOR ENCODING AND DECODING
str5 = str1.encode()        # str1 = "hello world"
print(str5)     # b'hello world'


str6 = str5.decode()
print(str6)     # hello world


# PRINTS TRUE IF IT ENDS WITH THE DEFINED SUFFIX
str = str1.endswith('o', 4, 5)      # str1 = "hello world"
print(str)      # True


# CREATES SPACES IN BETWEEN USING \t
str7 = 'python\ttutorials'
str8 = str7.expandtabs(8)
print(str8)        # python  tutorials


# FINDS THE INDEX OF A LETTER OR WORD *RETURNS -1 IF STRING NOT FOUND*
str = str1.find('ld', 1, 15)        # str1 = "hello world"
print(str)      # 9


# STRING FORMATTING
str = "{} {} {} with {}".format(str1, str3, str4, str2)    # str1="hello world",str2="PYTHON",str3="Lets",str4="beGIN"
print(str)      # hello world Lets beGIN with PYTHON

val = 10
print("decimal :  {0:d}".format(val))   # 10
print("hex : {0:x}".format(val))        # a
print("octal : {0:o}".format(val))      # 12
print("binary : {0:b}".format(val))     #1010


# INDEX FINDING (WORKS SAME AS FIND) *RETURNS TRACEBACK IF STRING NOT FOUND*
str = str1.index("world", 5, 11)        # str1 = "hello world"
print(str)      # 6

# RETURNS TRUE IF STRING IS AN ALPHABET AND NUMERIC
str9 = "24x7"
str = str9.isalnum()
print(str)      # True

# RETURNS TRUE ONL IF STRING IS AN INTEGER
str10 = "4.3"
str = str10.isdecimal()
print(str)      # False
str11 = "555"
str = str11.isdecimal()
print(str)      # True

# RETURNS TRUE IF STRING IS AN ALPHABET
str = str2.isalpha()         # str2 = "PYTHON"
print(str)      # True

# RETURNS TRUE IF STRING IS DIGIT
str = str11.isdigit()      # str11 = "555"
print(str)      # True

# RETURNS TRUE IF STRING IS 'True or False'
str12 = "True"
str = str12.isidentifier()
print(str)    # True
str13 = "False"
str = str13.isidentifier()
print(str)      # True

# RETURNS TRUE IF STRING IS IN LOWER CASE
str14 = "hello"
str = str14.islower()
print(str)      # True

# RETURNS TRUE IF STRING IS AN INTEGER NOT FLOAT
str = str10.isnumeric()     # str10 = "4.3"
print(str)      # False
str = str11.isnumeric()     # str11 = "555"
print(str)      # True

# RETURNS TRUE IF STRING IS IN UPPER CASE
str = str2.isupper()         # str2 = "PYTHON"
print(str)      # True

# RETURNS TRUE IF 1ST CHAR IS UPPER AND REST LOWER
str = str3.istitle()           # str3 = "Lets"
print(str)      # True

# RETURNS TRUE IF STRING DOESN'T CONTAIN ANY SPECIAL CHARACTER

str = str7.isprintable()    # str7 = 'python\ttutorials'
print(str)      # False


# RETURNS TRUE IF WHITE SPACE
wb = " "
str = wb.isspace()
print(str)      # True

'''
' '  - WHITE SPACE
'\t' - HORIZONTAL TAB
'\n' - NEW LINE
'\v' - VERTICAL TAB
'\f' - FEED
'\r' - CARRIAGE RETURN

'''

# JOINS THE STRING IN ITERABLES
no_space = ""
colon = ":"

list1 = ['1', '2', '3', '4']
str = colon.join(list1)
print(str)      # 1:2:3:4

list2 = ['h', 'e', 'l', 'l', 'o']
str = no_space.join(list2)
print(str)      # hello

# RETURNS THE LENGTH OF THE STRING
str = len(str1)     # str1 = "hello world"
print(str)      # 11


# PADS WITH CHARACTER FROM LEFT SIDE, CAN ALSO DEFINE WIDTH
str = str1.ljust(20, '$')
print(str)      # hello world$$$$$$$$$

# PADS WITH CHARACTER FROM LEFT SIDE, CAN ALSO DEFINE WIDTH
str = str1.rjust(20, '$')
print(str)      # $$$$$$$$$hello world

# CONVERTS ALL THE STRING INTO LOWER CASE
str = str2.lower()       # str2 = "PYTHON"
print(str)     # python
str = str4.lower()      # str4 = "beGIN"
print(str)     # begin

# CONVERTS ALL THE STRING INTO UPPER CASE
str = str4.upper()      # str4 = "beGIN"
print(str)      # BEGIN
str = str1.upper()      # # str1 = "hello world"
print(str)          # HELLO WORLD


# REMOVES WHITE SPACES OR CHAR
char_str = "$$$hello world$$$$$"
str = char_str.strip('$')
print(str)      # hello world

# REMOVES WHITE SPACES OR CHAR FROM LEFT SIDE
str = char_str.lstrip('$')
print(str)      # hello world$$$$$

# REMOVES WHITE SPACES OR CHAR FROM RIGHT SIDE
str = char_str.rstrip("$")
print(str)      # $$$hello world


# SEPARATION OF CHAR
str = str1.partition("el")       # str1 = "hello world"
print(str)      # ('h', 'el', 'lo world')
str = str1.partition("hello")
print(str)      # ('', 'hello', ' world')
str = str1.partition("world")
print(str)      # ('hello ', 'world', '')

# USED TO REPLACE CHARACTER
str = str1.replace("world", "work")      # str1 = "hello world"
str_rep = "AMONG PYTHON, JAVA, C, C++.JAVA IS THE WEB FRAMEWORK"
str = str_rep.replace("JAVA", "DJANGO", 1)
print(str)      # AMONG PYTHON, DJANGO, C, C++.JAVA IS THE WEB FRAMEWORK
str = str_rep.replace("JAVA", "DJANGO")
print(str)      # AMONG PYTHON, DJANGO, C, C++.DJANGO IS THE WEB FRAMEWORK

# FINDS THE SUBSTRING RETURNS THE HIGHEST INDEX(RHS) (IF NOT FOUND RETURNS -1)
str = str1.rfind("l")        # str1 = "hello world"
print(str)      # 9

# FINDS THE SUBSTRING RETURNS THE HIGHEST INDEX(RHS) (IF NOT FOUND RETURNS ERROR)
str = str1.rindex("l")        # str1 = "hello world"
print(str)      # 9

# SPLITS THE STRINGS AND CREATES A LIST
str_rem = "Django is a framework"
str = str_rem.split("Django")
print(str)      # ['', ' is a framework']

str = str_rem.split("a")
print(str)      # ['Dj', 'ngo is ', ' fr', 'mework']

# SPLITS THE STRINGS FROM RIGHT  AND CREATES A LIST
str = str_rem.rsplit("a", maxsplit=1)
print(str)      # ['Django is a fr', 'mework']

# MAKES PARTITION BETWEEN THE ONE WHICH IS DECLARED AND REST OTHER
str = str_rem.rpartition("is")
print(str)      # ('Django ', 'is', ' a framework')


# REMOVES NEW LINES AND RETURNS A LIST
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


# IF THE STRING STARTS WITH THE DEFINED STRING RETURNS TRUE ELSE FALSE
str = str1.startswith("h",0,9)
print(str)  # True

# INVERTS ALL THE CASES(LOWER<-->UPPER)
str = str1.swapcase()      # str1 = "hello world"
print(str)      # HELLO WORLD
str = str4.swapcase()    # str4 = "beGIN"
print(str)      # BEgin

# KEEPS ONLY 1ST LETTER CAPITAL
str = str4.title()      # str4 = "beGIN"
print(str)      # Begin

# ZERO PADDING FROM LEFT
str = str1.zfill(20) # str1 = "hello world"
print(str)      # 000000000hello world

