text = """Put several strings within parentheses 
to have them joined together.""" 


list = [1, 2, 3, 4, 5]

print(list[1:3])

print(text)


print("Fibonnaci")
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

print("Iterando uma lista")
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

print("Usando step")
for i in range(0, 10, 3):
    print(i)

print('Obtendo o índice dos itens')
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print("Break")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

print("Continue")

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


def fib(n):
    """Print a Fibonnaci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

print("fib2")
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)         # write the result


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

soma = lambda a, b: a + b

print(soma(12, 4))


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))

"""Coding style

Use 4-space indentation, and no tabs.
4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). Tabs introduce confusion, and are best left out.
Wrap lines so that they don’t exceed 79 characters.
This helps users with small displays and makes it possible to have several code files side-by-side on larger displays.
Use blank lines to separate functions and classes, and larger blocks of code inside functions.
When possible, put comments on a line of their own.
Use docstrings.
Use spaces around operators and after commas, but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
Name your classes and functions consistently; the convention is to use UpperCamelCase for classes and lowercase_with_underscores for functions and methods. Always use self as the name for the first method argument (see A First Look at Classes for more on classes and methods).
Don’t use fancy encodings if your code is meant to be used in international environments. Python’s default, UTF-8, or even plain ASCII work best in any case.
Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

"""

a = [-1, 1, 66.25, 333, 333, 1234.5]
del(a[0])
print(a)

my_first_name = 'João Paulo'
my_last_name = 'Gomes'
print(f'{my_last_name}, {my_first_name}')


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


import json
print(json.dumps([1, "simple", "list"]))

print("Exceptions")

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x1, y1 = inst.args     # unpack args
    print('x =', x1)
    print('y =', y1)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message    


print("Classes")

class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, data):
        self.data = data

    def f(self):
        return 'hello world'

    def f2(self):
        return self.data

my_class = MyClass([1, 2, 3])
print(my_class.i)
print(my_class.f())
print(my_class.f2())

class Animal:
    pass

class CanBark:
    pass

class Dog(Animal, CanBark):

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000