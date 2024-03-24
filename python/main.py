# single line comments
""" multiline ones
"""

# 1. datatype and operators
3 # 3
1+1 # 2
8-1 #7
10*2 # 20
35/5 #7

5//3 # -1
-5//3 # -2
-5//3.0 # -2.0
5.00/3.00 # 1.0

#modulo operation
7 % 3 # 1
-7 % 3 # 2

# exponentiation
2**3 # 8

# boolean values are primitives (note: capitalization)
True
False

not True
not False

True and False
False or True

# True equivalent to 1
# False equivalent to 0

True * 7 # 7

0 == False # true
2 > True # true

# none, 0 and empty strings/list/dicts/tuples/sets all evaluate to false
# all other values are true
bool(0) # false
bool("") # false
bool([]) # false
bool({}) # false
bool(()) # false
bool(set()) # false
bool(4) # true
bool(-6) # true


# using boolean logical operators on ints casts them to booleans for evaluation
# but for non-cast value is returned. don't mix up with bool(ints) and bitwise
# and / or (&, |)

bool(0) #false
bool(0) #false
0 and 2 #false
bool(-5) #false
bool(2) #false
-1 or 0 #false

# chaining operators
1 < 2 < 3 # true

# is vs == operator
# is checks if two variables refer to same object
# == checks if objects pointed have the same value
a = [1,2,3,4] # list to which a points
b = a # point b at what a is pointing to

b is a # true
b == a # true

b = [1,2,3,4] # point b to new object list
b is a # false
b == a # true, equal in value

# strings
"this is a string"
'this is also a string'

# concatenation
"hello" + "world" # hellow world
# string literals (but not variables) can be concatenated without using +
"hello" "world" # helloworld
# string = list of characters
"helloworld"[0] # h
# lenght
len("hi there")
# variables
name = "shadaab"
# formatted string
f"hi there {name}" # hi there shadaab

# None
# none is an object
# don't use equality '==' symbol to compare objects to none
# use "is" instead, this checks for equality of object identity
"etc" is None # false
None is None # true

# Variables and collections
print("i'm nice")

# by default print also prints out a new line
print("hello world", end="!") # changes the end of string to ! replacing '\n'

# input data
x = input("enter somehting") # returns data as string

# there are no declarations, only assignments
# convention in naming variables is snake_case style
some_var = 5
some_var # 5

# accessing a previously unassigned variable is exception
# name error exception NameError
# some_unknown_var # throws exception

# ternary operator
"if true" if 0 > 1 else "if false"

# lists store sequences
li = []
li.append(1)
li.append(2)

li.pop()
li.append(3)
# array like access
li[0] # 1
# last element
li[-1]
# ranges with slice syntax
# [a,b)
# li[start:end:step]
li[1:3] # from 1 to 3 index
li[2:] # list starting from index 2
li[::2] # list selecting with a step size 2
li[::-1] # step size 2 in reverse order
li2 = li[:] # one layer deep copy using slices
# deep copy means li2 is li will return false

del li[2] # remove arbitrary element from list
# remove first occurence of a value
li.remove(2)
li.remove(2) # exception. ValueError as 2 not present

li.insert(1,2) # insert at a specific index, idx 2 here

li.index(2) # index of first item occurence of 2
li.index(5) # valueError, as 5 not present

# lists can be added
li + li2
# concatenate lists with extend()
li.extend(li2)

# check for existence in a list with "in"
1 in li # true

len(li) # length of list

# Tuples tuples are like lists but are immutable
tup = (1,2,3)
tup[0] # 1
tup[0]  = 4 # typeError

# tuple of length one has to have a comma after the last element
# tuples of other lengths, even 0, do not need comma in end
type((1)) # class 'int'
type((1,)) # class 'tuple'
type(()) # class 'tuple'

# most of list operations on tuples too
len(tup)
tup2 = tup
tup + tup2
tup[:2] # first 2 elements
2 in tup # true

# unpack tuples (or lists) into variables
a,b,c = (1,2,3)
a, *b, c = (1,2,3,4) # a=1, b=[2,3], c=4

d,e,f = 4,5,6
e,d = d,e # d = 5, e = 4 swapping values

# dictionaries
empty_dict = {}
# prefilled dictionary
filled_dict = {"one": 1, "two": 2}

# keys of dictionary are immutable types. key can be converted to a constant hash value for quick lookups
# immutable types include ints, floats, strings, tuples
invalid_dict = {[1,2,3]: "123"} # TypeError: uhashable type list
valid_dict = {(1,2,3): [1,2,3]} # values can be of any type, however

# look up values with []
filled_dict["one"] # 1

# get all keys as an iterable with "keys()".
# wrap the call in list()
# for python <3.7 dictionary key ordering is not guaranteed.
# otherwise order is same as insertion order
list(filled_dict.keys()) # ["one", "two"]

# get all values as an iterable with values()
list(filled_dict.values()) # [1,2]

# check for existence of keys in dictionary with "in"
"one" in filled_dict # true
1 in filled_dict # false

# looking up a non-existent key is a keyError
filled_dict["four"] # KeyError

# get() method to avoid keyerror
filled_dict.get("one") # 1
filled_dict.get("four") # None

# get() with default argument
filled_dict.get("one", 4) # 1
filled_dict.get("four", 4) # 4

# setdefault() inserts into a dictionary only if given key isn't present
filled_dict.setdefault("five", 5) # filled_dict["five"] set to 5
filled_dict.setdefault("five", 6) # filled_dict["five"] set to 5 still

# adding to a dictionary
filled_dict.update({"four": 4}) # updates "four": 4
# remove keys from a dictionary with del 
del filled_dict["one"]

# additional unpacking options
{'a': 1, **{'b': 2}} # {'a': 1, "b": 2}
{'a': 1, **{'a': 2}} # {'a': 2}

# set, no duplicate values
empty_set = set()
# init a set with a bunch of values
some_set = {1,2,3,4,4,5} # some_set is now {1,2,3,4,5}

# similar to keys of dictionary, elements of a set have to be immutable
invalid_set = {[1], 1} # TypeError : unhashable type 'list'
valid_set = {(1,), 1}

# add one more item to set
filled_set = some_set
filled_set.add(5) # filled_set is now {1,2,3,4,5}

# do set intersection with &
other_set = {3,4,5,6}
filled_set & other_set # {3,4,5}

# do set union with | 
filled_set | other_set # {1,2,3,4,5,6}

# set difference with -
{1,2,3,4} - {2,3,5} # {1,4}

# symmetric difference with ^
{1,2,3,4} ^ {2,3,5} # {1,4,5}

# check if set on left is a superset of set on right
{1,2} >= {1,2,3} # false
# check if set on left is a subset of set on right
{1,2} <= {1,2,3} # true

# existence in set using in
2 in filled_set # true
10 in filled_set # false

# one layer deep copy
filled_set = some_set.copy() # filled_set is {1,2,3,4,5}
filled_set is some_set # false

# control flow and iterables
some_var = 5
if some_var > 10:
    print("some_var is bigger than 10")
elif some_var < 10: # optional
    print("some var less than 10")
else: # optional
    print(f"some_var equal to 10")

"""
for loops iterate over lists
"""
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

"""
range(number) returns an iterable of numbers from zero up to (but excluding) the given number
range(4) = [0, 4)
range(a,b) = [a, b)
range(a,b,step)
"""
for i in range(4):
    print(i)

for i in range(1,2):
    print(i) # prints 1

for i in range(1,10,3):
    print(i) # prints 1, 4, 7

"""
loop over list using enumerate
"""
animals = ["a", "b", "c", "d"]
for i, val in enumerate(animals):
    print(i,val)

"""
while Loop
"""
x = 0
while x < 4:
    print(x)
    x += 1

# handling exceptions
try:
    # use "raise" to raise an error
    raise IndexError("this is an index error")
except IndexError as e: 
    pass # refrain from this, provide a recovery
except (TypeError, NameError):
    pass # multiple errors can be processed jointly
else:
    # optional to use
    pass
finally:
    print("we can clean up resources here")

# instead of try/finally to cleanup resource you can use a with statement
with open("file.txt") as f:
    for line in f:
        print(line)

# writing to a file
contents = {"aa": 12, "bb": 21}
with open("file.txt", "w+") as file:
    file.write(str(contents)) # writes a string to file

# import package
# module = python file
# multiple modules = one package
import json

with open("file.txt", "w+") as file:
    file.write(json.dumps(contents)) # writes an object to a file
# reading from a file
with open('file.txt', "r+") as file:
    contents = file.read() # reads a string from a file
print(contents)

with open('file2.txt', 'r+') as file:
    contents = json.load(file) # reads a json object from a file
print(contents)

# fundamental abstraction called iterable
# iterable is an object that can be treated as a sequence.
# object returned by range funciton, is an iterable
filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable) # dict_keys(['one', 'two', 'three']), this is an object that implements an iterable interface

# can be looped over
for i in our_iterable:
    print(i) # 'one', 'two', three

# cannot address elements by index
our_iterable[1] # typeerror
# an iterable is an object that knows how to create an iterator
our_iterator = iter(our_iterable)
# our_iterator is an object that can remeber the state as we traverse through
# cannot address elements by index
our_iterable[1] # typeerror
# an iterable is an object that knows how to create an iterator
our_iterator = iter(our_iterables)
# iterator creation using iter() on iterable
# our iterator is object that can remember state as we traverse through it. we get next object with "next()"
next(our_iterator) # "one"
# it maintains state as we iterate
next(our_iterator) # "two"
next(our_iterator) # "three"
next(our_iterator) # StopIteration exeption in end

our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i) # one, two three

list(our_iterable) # ['one', 'two', 'three']
list(our_iterator) # [] becasue state is saved



#  Functions
# def keyword
def add(x,y):
    print(f"{x}{y}")
    print("x is {}, y is {}".format(x, y))
    return x + y

add(5,6)

add(x=5,y=6) # keyword args can arrive in any order

# positional args, variable number of positional args
def varargs(*args):
    return args

varargs(1,2,3) # (1,2,3)

# can define functions that take a variable number of keyword args, as well
def keyword_args(**kwargs):
    return kwargs

keyword_args(big="foot", loch="ness") # {"big":"foot", "loch":"ness"}

def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

# when calling functions, opposite of args/kwargs can be done
# use * to expand args(tuples) and use ** to expand kwargs(dictionaries)

args = (1,2,3,4)
kwargs = {"a":3,"b":4}
all_the_args(*args)
all_the_args(**kwargs)
all_the_args(*args, **kwargs)

def swap(x, y):
    return y,x # return multiple values as a tuple without paranthesis

x=1
y=2
x,y=swap(x,y) #multiple assignment of tuple

# global variable referred inside function using global keyword
x=5
def set_x(num):
    x = num #43
    print(x) #43

def set_global_x(num):
    # global indicates that particular var lives in global scope
    global x 
    print(x) # 5
    x = num # global var x is now set to 6
    print(x) # 6

set_x(43) #43
set_global_x(6) # 5 6

# python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3) # 13


# closures in nested functions:
# we can use nonlocal keyword to work with variables in nested scope which shouldn't be declared in inner functions
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1

        return total/count
    return avg
avg = create_avg()
avg(3) # 3
avg(5) # 3 + 5 / 2 = 4
avg(7) # 8+7/3 = 5

# anonymous functions
(lambda x: x > 2)(3)
# true

(lambda x,y: x**2+y**2)(2,1) # 5

# built-in higher order functions
list(map(add_10, [1,2,3])) # [11,12,13]
list(map(max, [1,2,3],[4,2,1])) # [4,2,3]
list(filter(lambda x: x>5, [3,4,5,6,7])) # [6,7]

# list comprehensions for nice maps and filters can be used
# list comprehension stores the output as a list(which itself may be nested)
[add_10(i) for i in [1,2,3]] # [11,12,13]
[x for x in [3,4,5,6,7] if x > 5] # [6,7]

# similarly set and dict comprehensions can be created
{x for x in 'abcdef' if x not in 'abc'} # {'d','e','f'}
{x: x**2 for x in range(5)} # {0:0, 1:1, 2:4, 3:9, 4:16}


# Modules 
# python modules = python files
# module = file
# module name = file name
# using import statement
import math
print(math.sqrt(16))

# can get specific functions from a module
from math import ceil, floor
print(ceil(3.7)) # 4
print(floor(3.7)) # 3

# can import all funcitons from a module
# not recommended
from math import *

# shorten names
import math as m
math.sqrt(15) == m.sqrt(15) # true

# module name = filename
import math
dir(math) # find out functions and attributes defined in module

# if math.py also present in same folder, folder math.py will be loaded instead of built-in module
# happens because the local folder has priority over python's builtin libraries


# Classes
# class keyword to create a class
class Human:
    # class attribute, shared by all instances of this class
    species = "khar"

    # basic init, this is called when this class is inited
    # double leading and trailing underscores denote objects  or attributes that are used by python but that live in user-controlled namespaces. methods(or objects or attributes) like: __init__, __str__, __repr__ etc are called special methods (or sometimes dunder methods).
    def __init__(self, name):
        # assign arg to instance's name attirbute
        self.name = name
        # init property
        self._age = 0 # leading underscore indicates "age" is private, do'nt rely on this to be enforced tho
    # an instance method. all methods take self as first arg
    def say(self, msg):
        print("{name}")

    # another instance method
    def sing(self):
        return "hi there"

    # class method shared among all instances, they're called with calling class as first arg
    @classmethod
    def get_species(cls):
        return cls.species

    # static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt"
    
    # a property is like a getter.
    # used to turn variables into read_only
    # no need to write trivial getters/setters in python tho
    @property
    def age(self):
        return self._age
    
    # sets the age
    @age.setter
    def age(self, age):
        self._age = age

    # this allows prop to be deleted
    @age.deleter
    def age(self):
        del self._age

# py interpreter reads a source file and executes all its code
# __name__ check makes sure this code block is only executed when this module is main program
if __name__ == '__main__':
    # instantiate a class
    i = Human(name='ahmed')
    i.say("hi")
    j = Human("shadaab")
    j.say("hello")
    # i and j are instances of type Human, i.e, objects

    # call our class method
    i.say(i.get_species()) # khar
    # change shared attribute
    Human.species = 'proper khar'
    i.say(i.get_species()) # proper khar
    j.say(j.get_species()) # proper khar

    # call the static method
    print(Human.grunt())

    # static methods can be called by instances too
    print(i.grunt())

# ##########
# inheritance
# ##########
# from <module_name> import Human
class Superhero(Human):
    # overriding
    species = "superhuman"
    # override constructor
    def __init__(self, name, movie):
        self.fictional = True
        self.movie = movie
        # super lets access parent class methods
        # this calls parent constructor
        super().__init__(name)
    # overriding other method
    def sing(self):
        return 'la la la'
    # add an additional instance method
    def boast(self):
        pass
if __name__ == '__main__':
    sup = Superhero(name='tick')
    if isinstance(sup, Human):
        print('i"m human')
    if type(sup) is Superhero:
        print("i'm superhero")

# bat.py
class Bat:
    species = 'bat'
    def __init__(self, can_fly=True) -> None:
        self.fly = can_fly

# multiple inheritancce
# superhero.py
# from superhero import Superhero
# from bat import Bat
class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        Superhero.__init__(self, 'ananoymous')



# generators
# generators help you make lazy code, #todo read more about it
def double_numbers(iterable):
    for i in iterable:
        yield i+i # yield #todo read more about it

# generators are memory efficient because they only load the data needed to process the next value in iterable. this allows them to perform operations on otherwise prohibitively large value ranges.
# note: `range` replaces `xrange` in python 3
for i in double_numbers(range(1,900000000)):
    # `range` is a generator
    print(i)
    if i >= 30:
        break

# just like you create a list comprehension, you can create generator comprehension as well
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x) # -1 -2 -3 -4 -5

# cast a generator comprehension directly to a list
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)

# decorators are syntatic sugar. they make code easier to read while accomplishing clunky syntax
# wrappers are one type of decorator.
# they're really useful for adding logging to existing functions without needing to modify them
def log_function(func):
    def wrapper(*args, **kwargs):
        print("entering function", func.__name__)
        result = func(*args, **kwargs)
        print("exiting function:", func.__name__)
        return result
    return wrapper

@log_function
def my_function(x, y):
    return x+y

# my_function = log_function(my_function)
# here my_function information is lost exmple: 
print(my_function.__name__) # wrapper
print(my_function.__code__.co_argcount) # 0, brecause both args in wrappers()'s signature are optionl

# wrapper has taken replaced the information of my_funcitons

# fix this using func tools
from functools import wraps
def log_function(func):
    @wraps(func) # this ensures are func props are copied
    def wrapper(*args, **kwargs):
        # do something
        pass
    return wrapper
    



    
