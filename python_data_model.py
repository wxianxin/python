# source https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
__author__ = 'Steven Wang'

# Every object has an identity, a type and a value. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.
# CPython implementation detail: For CPython, id(x) is the memory address where x is stored.

# An object’s type determines the operations that the object supports (e.g., “does it have a length?”) and also defines the possible values for objects of that type. The type() function returns an object’s type (which is an object itself). Like its identity, an object’s type is also unchangeable.

# The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable. (The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value, it is more subtle.) An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

# The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is unchangeable once they are created are called immutable. (The value of an immutable container object that contains a reference to a mutable object can change when the latter’s value is changed; however the container is still considered immutable, because the collection of objects it contains cannot be changed. So, immutability is not strictly the same as having an unchangeable value, it is more subtle.) An object’s mutability is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

# Some objects contain references to other objects; these are called containers. Examples of containers are tuples, lists and dictionaries. The references are part of a container’s value. In most cases, when we talk about the value of a container, we imply the values, not the identities of the contained objects; however, when we talk about the mutability of a container, only the identities of the immediately contained objects are implied. So, if an immutable container (like a tuple) contains a reference to a mutable object, its value changes if that mutable object is changed.

# Types affect almost all aspects of object behavior. Even the importance of object identity is affected in some sense: for immutable types, operations that compute new values may actually return a reference to any existing object with the same type and value, while for mutable objects this is not allowed. E.g., after a = 1; b = 1, a and b may or may not refer to the same object with the value one, depending on the implementation, but after c = []; d = [], c and d are guaranteed to refer to two different, unique, newly created empty lists. (Note that c = d = [] assigns the same object to both c and d.)

################################################################################
# The standard type hierarchy

None

NotImplemented

Ellipsis

numbers.Number
    numbers.Integral
        int
        bool
    numbers.Real
        float
    numbers.Complex
        complex

sequence
# These represent finite ordered sets indexed by non-negative numbers.
# The built-in function len() returns the number of items of a sequence.
# Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j.
# Sequences are distinguished according to their mutability:
    # Immutable sequences An object of an immutable sequence type cannot change once it is created.
    str
    tuple
    bytes

    # Mutable sequences can be changed after they are created.
    list
    bytearray # Aside from being mutable (and hence unhashable), byte arrays otherwise provide the same interface and functionality as immutable bytes objects.

Set
    set         # mutable
    frozenset   # immutable and hashable, it can be used again as an element of another set, or as a dictionary key.


dict # Mappings: it can be used again as an element of another set, or as a dictionary key.

################################################################################

