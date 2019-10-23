################################################################################
# numpy
# homogeneous multidimensional array: Every numpy array is a grid of elements of the same type.
# NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
# In NumPy dimensions are called axes.
# The number of axes is rank.

# NumPy’s array class is called ndarray.
ndarray.ndim
ndarray.shape
ndarray.size
ndarray.dtype
ndarray.itemsize


a = np.array([1, 2, 3])
print(type(a))
print(a.shape)

a = np.zeros((2, 2))
b = np.ones((1, 2))
c = np.full((2, 2), 7)
d = np.eye(2)
e = np.random.random((2, 2))
y = np.empty_like(x)  # Create an empty matrix with the same shape as x
np.arange(0, 9, 1.7)  # sequences of numbers | use like `range`
np.linspace(0, 2, 9)  # easier to predict the number of elements obtained

x = np.array([1, 2], dtype=np.int64)

################################################################################
# indexing, slicing and iterating
a[::-1]
# When fewer indices are provided than the number of axes, the missing indices are considered complete slices.
# The expression within brackets in b[i] is treated as an i followed by as many instances of : as needed to represent the remaining axes. NumPy also allows you to write this using dots as b[i,...].
# The dots (...) represent as many colons as needed to produce a complete indexing tuple.
x[4, ..., 5, :]

# Iterating over multidimensional arrays is done with respect to the first axis
for row in b:
    print(row)
# if one wants to perform an operation on each element in the array, one can use the flat attribute which is an iterator over all the elements of the array
for element in b.flat:
    print(element)

################################################################################
# Shape Manipulation
a.ravel()  # returns the array, flattened
# The order of the elements in the array resulting from ravel() is normally “C-style”, that is, the rightmost index “changes the fastest”, so the element after a[0,0] is a[0,1]. If the array is reshaped to some other shape, again the array is treated as “C-style”.
a.reshape(6, 2)  # returns the array with a modified shape
a.reshape(
    3, -1
)  # If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated.
a.T  # returns the array, transposed

################################################################################
# Stacking together different arrays/Splitting one array into several smaller ones
np.vstack((a, b))
np.hstack((a, b))
# For arrays of with more than two dimensions, '-----------' stacks along their second axes, 'vstack' stacks along their first axes, and 'concatenate' allows for an optional arguments giving the number of the axis along which the concatenation should happen.

np.hsplit(a, 3)  # Split a into 3
np.hsplit(a, (3, 4))  # Split a after the third and the fourth column
np.vsplit()  # splits along the vertical axis, and
np.array_split()  # allows one to specify along which axis to split.

################################################################################
# Copies and Views
# Simple assignments make no copy of array objects or of their data.
a = np.arange(12)
b = a
b is a

# Python passes mutable objects as references, so function calls make no copy.
id(x)  # id is a unique identifier of an object

# Different array objects can share the same data. The 'view' method creates a new array object that looks at the same data.
c = a.view()
c is a  # False
c.base is a  # True
c.flags.owndata  # False
c.shape = 2, 6  # a's shape doesn't change
c[0, 4] = 1234  # a's data changes

# Slicing an array returns a view of it.


# The copy method makes a complete copy of the array and its data.
d = a.copy()  # a new array object with new data is created
d is a  # False
d.base is a  # False

################################################################################
# Broadcasting rules
# 1. If all input arrays do not have the same number of dimensions, a “1” will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.
# 2. Arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the “broadcast” array.


################################################################################
np.ix_(*args)  # Construct an open mesh from multiple sequences.
# This function takes N 1-D sequences and returns N outputs with N dimensions each, such that the shape is 1 in all but one dimension and the dimension with the non-unit shape value cycles through all N dimensions.


################################################################################
a.transpose()
u = np.eye(2)
np.dot(j, j)  # matrix product
np.trace(u)  # trace
np.linalg.solve(
    a, y
)  # Solve a linear matrix equation, or system of linear scalar equations.
np.linalg.eig(j)  # Compute the eigenvalues and right eigenvectors of a square array.
np.linalg.inv(a)  # Compute the (multiplicative) inverse of a matrix.

################################################################################
np.random.random()  # Return random floats in the half-open interval [0.0, 1.0).
np.random.rand()  # Random values in a given shape.
np.random.randn()  # Return a sample (or samples) from the “standard normal” distribution.


# Basic mathematical functions operate elementwise on arrays, and are available both as operator overloads and as functions in the numpy module。
print(x / y)
print(np.divide(x, y))
print(np.sqrt(x))

# dot function to compute inner products of vectors, to multiply a vector by a matrix, and to multiply matrices. dot is available both as a function in the numpy module and as an instance method of array objects:

print(x.dot(y))
print(np.dot(x, y))

# Perform computations on arrays
# full list of mathematical functions provided by numpy: https://docs.scipy.org/doc/numpy/reference/routines.math.html
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

# transpose
a.T

# broadcasting
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting

# When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing dimensions, and works its way forward. Two dimensions are compatible when
# 1. they are equal, or
# 2. one of them is 1
# If these conditions are not met, a ValueError: frames are not aligned exception is thrown.

# Functions that support broadcasting are known as universal functions. Full list: https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs

################################################################################
# numpy vectorization

# caveat: Alway comment the code！ It is a very powerful library and you can make wonders with it but, most of the time, this comes at the price of readability.

from tools import accumulate

steps = random.choices([-1, +1], k=n)
return [0] + list(accumulate(steps))

import numpy as np

steps = np.random.choice([-1, +1], n)
return np.cumsum(steps)
