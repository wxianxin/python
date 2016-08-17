#Author: Steven Wang	Date:20151221
#codecademy python

{} #curly braces

no datatype
use white spave to structure(no ";", use indent)
"True" "False"
comments:
#comments

"""
comments
"""


string:
print text
print "a string"
print "a" + "big" + "hat" #concatenate

raw_input("Please input:") #input function with hint message
variable.isalpha() #False if there is non-letter characters

"cat"[0] == c
"cat"[2] == t
"cat"[1:2] == at
"cat"[0:len("cat")] == cat

len(variable)
variable.lower()
variable.upper()
str(variable)    #explicit string conversion
#methods that use dot notation only work with strings, or other words; len() and str() can work on other datatypes

% formatting
print ("Hello, %s") %(variable)     # %s, placeholder
print ("Hello, %s and %s") %(variable1,variable2)

'Alpha' "Bravo" "Thailand's people" #no need for backslash

data & time:
from datetime import datetime #inport "datetime" module
now = datetime.now()
now.year now.month now.day now.hour now.minute now.second

"**" #to the power of

boolean operator:
not, and, or
-----------> priority

if __:
elif __: #else if, elif is only checked if the original "if" statement is False
else __:

function:
1.header: def function_name(arguments):
2.optional comment
3.body    #indented

import module
1.generic import:  import math
	call: math.sqrt()
2.function import: from math import sqrt  #pulling in just a single function from a module
    call: sqrt()
3.universal import: from math import *    #CAUTION: fill the program with many variable and function names
	call: sqrt()
#best to stick with module name

	import math
	everything = dir(math)
	print everything
#show everything available in math

max()
min()
abs()
type()

list:
list_name = [item_1, item_2]
empty_list = []

list_name[0]    #call by index
list_name.append()
len(list_name)
list_name[1:3]   #return the 2nd to the 4th
#think of string as a list of characters
list_name[:3]
list_name[6:]

list_name.index() # search the first corresponding element
list_name.insert('index', value)

for variable in list_name:   #loop eg. for i in list_1:

list_name.sort()   #modify the list so it is in order

dictionary # map in c++
d = {'key1':1, 'key2':2, 'key3':3}
dict_name[new_key] = new value
empty_dict = {}

del dict_name[key_name]
list_name.remove()

LOOP:

for key in dict_name:
	print dict_name[key]
#CAUTION: dictionary is unordered

sum(variable) # summation

5/2 = 2
float(5)/ 2 = 2.5
"/" #continuation charater, next line is following up

list_name.pop(index) # return value and remove
list_name.remove(item) # find the item and remove
del(list_name[index]) # like 'pop' but no return

range # a shortcut to generate a list
range(6) #=> [0,1,2,3,4,5]  range(stop)
range(1,6) #=> [1,2,3,4,5]  range(start,stop)
range(1,6,3) #=> [1,4]  range(start,stop,step)

for item in my_list:
	print item

for i in range(len(my_list)):
	print my_list[i]

["0"] * 5 #=> ['0','0','0','0','0']

my_list = ['a','b','c']
#turn list into string
' '.join[my_list] #=> a b c
"---".join[my_list] #=> a---b---c
# '' and "" are interchangeable

form random import randint
int(raw_imput("hint")) #raw_input always returns string type

if x not in range(8) or y not in range(5)
break # to get out of the loop

print a,b

while loop_condition:

while/else: #else executes as long as while loop condition is evaluated False; if the loop exits as the result of break, [else] will not be executed

for/else: # [else]excutes after [for] only if [for] ends normally(not because of [break])

print char, #[,] character after [print char] keeps next [print] keep its output in the same line

for key in my_dict: #you get key

enumerate: # return index
	for index, item in enumerate(list):
	print index, # output the index
	print item # output the list element

zip: #create pairs of elements, stops at the end of shorter list
	for a,b in zip(list_a, list_b):
		print a, b

"*" * 4 # return "****"

my_string.split() #split the string into a list of strings

if a not in b:

sorted(list) # return the ordered list

sum[my_list] #returns sum of all list elements

!!! # always devide by 2.0
float(len(my_list))

#dictionary is unordered key/value pairs
print my_dict.item() #=> print all keys and its values in random order
my_dict.keys() # returns an array of dictionary's keys
my_dict.item() # returns an array of dictionary's values

# tuple: a sequence of immutable object
# tuples are surrounded by "()"

print item, # the trailing comma keeps printing on the same line

#list comprehension: for/in if
my_list = [ i for i in range(51) if i % 2 == 0]
my_list = [x*2 for x in range(1,6)]
my_list = [x*2 for x in range(1,6) if (x*3) % 3 == 0]

#list slicing:
[start:end:step] #start is inclusive; end is exclusive
#omitting indices:
Python will pick up default:
#default start index is 0
#default ending index is the end
#default step is 1
my_list = [1,2,3,4,5]
my_list[3:] #=>[4,5]
my_list[:2] #=>[1,2]
my_list[::2] #=>[1,3,5]
my_list[::-1] #=>[5,4,3,2,1] {reversing a list)

#functional programming(anonymous function):
lambda; filter
	my_list = range(16)
	filter(lambda x: x%3 == 0, my_list)

#bitwise operator:
#In python: to write numbers in bianry format by starting the number with [0b].
	0b100
	0b1101
bin() # takes an integer as input and returns its binary
oct() # like bin()
hex() # like bin()

int("42") #=> 42
int("110") #=> 6
int("0b110") #=> 6

# floor division in python is integer division;
# in python 3: 5/2 = 2.5; 5//2 = 2

0b0001 << 2 #=> 0b0100
0b0100 >> 2 #=> 0b0001

#bitwise compare
a = 0b0101010
b = 0b0001111

& #AND
0&0=0
0&1=0
1&0=0
1&1=1
a&b = 0b1010

| #OR
0|0=0
0|1=1
1|0=1
1|1=1
a|b = 0b0101111

^ #XOR: exclusive or operator; for a bit, either of the two is 1 but not both
0^0=0
0^1=1
1^0=1
1^1=0

a^b = 0b0100101

~ #NOT opeartor: add one the number and then make it negative

# bit mask
# a bit mask can help you turn specific bits on, turn others off, or just collect data from an integer

data = 0b010011010
mask = 0b000010000
print data&mask

& # using[&] to turn on bits
| # using[|] to turn a corresponding bit on if it is off and leave it on if it is already on
^ # using[^] to flip bits
<< >> # using [<<] and [>>] to slide mask into place

# class:
# when a class has its own functions, those functions are called methods
# ["Eric"] and [my_dict] are instances of the [str] and [dict] class.
class NewClass(object):	# in the parenthesis is the class from which the new class inherits
						# [object] is the simplest, most basic class
						# by convention, user-defined Python class names start with a capital letter
	def __init__(self, age, name):	#[__intit__()] exist by default
		self.age = age				#Python will use the 1st parameter that [__init__()] receives to refer to the object being created.
		self.name = name			#Python convention: it's overwhelming common to use [self] as the 1st parameter in [__init__()]

	def method_1(self):	# for any method in a class, you need to provide [self] as the 1st argument
		pass						# [pass] statement is a null operation; nothing happens when it executes; works as a placeholder
	
	def method_d(self,a,b):
		pass
	
	member_variable_1 = True
	member_variable_2 = "test"

my_object = NewClass(18, "python")	# parameter list starts from the parameter after [self] (you don't need to give [self])
print my_object.name				# dot notation: to access attributes of out objects

# class scope:
# needs further attention
global variable	#like [public] in c++
member variable	#like [protected] in c++
instance veriable	#like [private] in c++

# Inheritance: "is-a" relationship
superclass	subclass
baseclass	derivedclass
parentclass	childclass

class BaseClass(object):
	def __init__(self,a,b):
		pass

class DerivedClass(BaseClass):

#override(overload): # in a new Derived class, override a function is to define a function with the same function name

super # [super] directly access the attributes or methods of a superclass
	def method(self,a,b):
		return super(DerivedClass, self).method(a,b)
	
# 2 ways of initialization
#1.
	def __init__(self,a,b,c,d):
		BaseClass.__init__(self,a,b)
		self.c = c
		self.d = d

#2.
	def __init__(self,a,b,c,d):
		super(DerivedClass, self).__init__(a,b)	# no [self] in the 2nd parenthesis
		self.c = c
		self.d = d

__repr__() # a built-in methods: representation, tell Pyhon how to represent an object of our class
	def __repr__(self):
		return 'DerivedClass(a=%s, b=%s)' % (self.a, self.b)

DerivedClass #=> "DerivedClass(a=1, b=2)" (assume a="1" and b="2")

#__repr__ goal is to be unambiguous
#__str__ goal is to be readable
#Container’s __str__ uses contained objects’ __repr__

#file I/O:
my_file = open("output.txt", "w")	# open "output.txt" in "w" mode("w" stands for "write"), store the result of this operation in a file object [my_file]
# "w": write only mode
# "r": read only mode
# "r+": read and write mode
# "a": append mode

my_file.write("abcd\n")
my_file.read()
my_file.close() # During I/O process, data is buffered. Python doesn't flush the buffer, that is, write data to the file until it's sure you've done writing. One way to do this is to close the file.

#automatically close the files: file objects contain a pair of built-in methods: 
__enter__()
__exit__()	#when [__exit__()] is invoked, the file will be closed

with/as # use [with][as] to invoke [__exit__()]
with open("text.txt","w") as my_file:
	my_file.write("abcd")

#check if the file is closed:
print my_file.closed #Python file objects have a [closed] attribute, [True] for closed, [False] for not closed

#End of file
