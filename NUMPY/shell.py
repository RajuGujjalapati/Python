Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> a=numpy.array([3,4,5,6,7])
>>> a
array([3, 4, 5, 6, 7])
>>> a/3
array([1.        , 1.33333333, 1.66666667, 2.        , 2.33333333])
>>> int(a/3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(a/3)
TypeError: only size-1 arrays can be converted to Python scalars
>>> lis=[2,34,65,4]
>>> lis/2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    lis/2
TypeError: unsupported operand type(s) for /: 'list' and 'int'
>>> import numpy as np
>>> help(np.array)
Help on built-in function array in module numpy:

array(...)
    array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
    
    Create an array.
    
    Parameters
    ----------
    object : array_like
        An array, any object exposing the array interface, an object whose
        __array__ method returns an array, or any (nested) sequence.
    dtype : data-type, optional
        The desired data-type for the array.  If not given, then the type will
        be determined as the minimum type required to hold the objects in the
        sequence.
    copy : bool, optional
        If true (default), then the object is copied.  Otherwise, a copy will
        only be made if __array__ returns a copy, if obj is a nested sequence,
        or if a copy is needed to satisfy any of the other requirements
        (`dtype`, `order`, etc.).
    order : {'K', 'A', 'C', 'F'}, optional
        Specify the memory layout of the array. If object is not an array, the
        newly created array will be in C order (row major) unless 'F' is
        specified, in which case it will be in Fortran order (column major).
        If object is an array the following holds.
    
        ===== ========= ===================================================
        order  no copy                     copy=True
        ===== ========= ===================================================
        'K'   unchanged F & C order preserved, otherwise most similar order
        'A'   unchanged F order if input is F and not C, otherwise C order
        'C'   C order   C order
        'F'   F order   F order
        ===== ========= ===================================================
    
        When ``copy=False`` and a copy is made for other reasons, the result is
        the same as if ``copy=True``, with some exceptions for `A`, see the
        Notes section. The default order is 'K'.
    subok : bool, optional
        If True, then sub-classes will be passed-through, otherwise
        the returned array will be forced to be a base-class array (default).
    ndmin : int, optional
        Specifies the minimum number of dimensions that the resulting
        array should have.  Ones will be pre-pended to the shape as
        needed to meet this requirement.
    
    Returns
    -------
    out : ndarray
        An array object satisfying the specified requirements.
    
    See Also
    --------
    empty_like : Return an empty array with shape and type of input.
    ones_like : Return an array of ones with shape and type of input.
    zeros_like : Return an array of zeros with shape and type of input.
    full_like : Return a new array with shape of input filled with value.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    zeros : Return a new array setting values to zero.
    full : Return a new array of given shape filled with value.
    
    
    Notes
    -----
    When order is 'A' and `object` is an array in neither 'C' nor 'F' order,
    and a copy is forced by a change in dtype, then the order of the result is
    not necessarily 'C' as expected. This is likely a bug.
    
    Examples
    --------
    >>> np.array([1, 2, 3])
    array([1, 2, 3])
    
    Upcasting:
    
    >>> np.array([1, 2, 3.0])
    array([ 1.,  2.,  3.])
    
    More than one dimension:
    
    >>> np.array([[1, 2], [3, 4]])
    array([[1, 2],
           [3, 4]])
    
    Minimum dimensions 2:
    
    >>> np.array([1, 2, 3], ndmin=2)
    array([[1, 2, 3]])
    
    Type provided:
    
    >>> np.array([1, 2, 3], dtype=complex)
    array([ 1.+0.j,  2.+0.j,  3.+0.j])
    
    Data-type consisting of more than one element:
    
    >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
    >>> x['a']
    array([1, 3])
    
    Creating an array from sub-classes:
    
    >>> np.array(np.mat('1 2; 3 4'))
    array([[1, 2],
           [3, 4]])
    
    >>> np.array(np.mat('1 2; 3 4'), subok=True)
    matrix([[1, 2],
            [3, 4]])

>>> import numpy as np
>>> a=np.array([1,2,3])
>>> a
array([1, 2, 3])
>>> a=np.array([[1,2,3],[23,44,54]])
>>> a
array([[ 1,  2,  3],
       [23, 44, 54]])
>>> np.array([1,2,3],"complex")
array([1.+0.j, 2.+0.j, 3.+0.j])
>>> 
>>> np.arrange(1,10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    np.arrange(1,10)
  File "C:\Users\New\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\__init__.py", line 219, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arange(1,10)
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(3.2)
array([0., 1., 2., 3.])
>>> np.arange(1,10,2)
array([1, 3, 5, 7, 9])
>>> np.arange(20,dtype="complex")
array([ 0.+0.j,  1.+0.j,  2.+0.j,  3.+0.j,  4.+0.j,  5.+0.j,  6.+0.j,
        7.+0.j,  8.+0.j,  9.+0.j, 10.+0.j, 11.+0.j, 12.+0.j, 13.+0.j,
       14.+0.j, 15.+0.j, 16.+0.j, 17.+0.j, 18.+0.j, 19.+0.j])
>>> np.arange(1,20,3)
array([ 1,  4,  7, 10, 13, 16, 19])
>>> help(np.zeros)
Help on built-in function zeros in module numpy:

zeros(...)
    zeros(shape, dtype=float, order='C')
    
    Return a new array of given shape and type, filled with zeros.
    
    Parameters
    ----------
    shape : int or tuple of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: 'C'
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.
    
    Returns
    -------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.
    
    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    full : Return a new array of given shape filled with value.
    
    Examples
    --------
    >>> np.zeros(5)
    array([ 0.,  0.,  0.,  0.,  0.])
    
    >>> np.zeros((5,), dtype=int)
    array([0, 0, 0, 0, 0])
    
    >>> np.zeros((2, 1))
    array([[ 0.],
           [ 0.]])
    
    >>> s = (2,2)
    >>> np.zeros(s)
    array([[ 0.,  0.],
           [ 0.,  0.]])
    
    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)],
          dtype=[('x', '<i4'), ('y', '<i4')])

>>> np.zeros(5)
array([0., 0., 0., 0., 0.])
>>> np.zeros(3,dtype="int")
array([0, 0, 0])
>>> np.zeros((2,3))
array([[0., 0., 0.],
       [0., 0., 0.]])
>>> np.zeros(4,5,dtype="C")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    np.zeros(4,5,dtype="C")
TypeError: data type not understood
>>> np.zeros(4,5,dtype="int",order="C")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    np.zeros(4,5,dtype="int",order="C")
TypeError: zeros() takes at most 3 arguments (4 given)
>>> np.zeros((4,5),dtype="int",order="C")
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
>>> np.zeros((4,5),dtype="int",order="F")
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
>>> np.ones(2,4)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    np.ones(2,4)
  File "C:\Users\New\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\core\numeric.py", line 207, in ones
    a = empty(shape, dtype, order)
TypeError: data type not understood
>>> np.ones(2)
array([1., 1.])
>>> np.ones(4,)
array([1., 1., 1., 1.])
>>> np.ones(4)
array([1., 1., 1., 1.])
>>> np.ones((5),dtype="int")
array([1, 1, 1, 1, 1])
>>> np.ones((4,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
>>> help.empty
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    help.empty
AttributeError: '_Helper' object has no attribute 'empty'
>>> np.empty(6)
array([0., 0., 0., 0., 0., 0.])
>>> np.empty(4)
array([1., 1., 1., 1.])
>>> 
================================ RESTART: Shell ================================
>>> import numpy as np
>>> np.empty(5)
array([0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 3.87347466e-321,
       2.50443854e+262])
>>> np.empty([3,4],dtype="int")
array([[  33554432,   34341130,   17039630,   35389708],
       [ -83753712,   17303302,   17826060, 2037514774],
       [ 687865856,    7369220,  131727360, 1885434487]])
>>> help(np.empty)
Help on built-in function empty in module numpy:

empty(...)
    empty(shape, dtype=float, order='C')
    
    Return a new array of given shape and type, without initializing entries.
    
    Parameters
    ----------
    shape : int or tuple of int
        Shape of the empty array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        Desired output data-type for the array, e.g, `numpy.int8`. Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: 'C'
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.
    
    Returns
    -------
    out : ndarray
        Array of uninitialized (arbitrary) data of the given shape, dtype, and
        order.  Object arrays will be initialized to None.
    
    See Also
    --------
    empty_like : Return an empty array with shape and type of input.
    ones : Return a new array setting values to one.
    zeros : Return a new array setting values to zero.
    full : Return a new array of given shape filled with value.
    
    
    Notes
    -----
    `empty`, unlike `zeros`, does not set the array values to zero,
    and may therefore be marginally faster.  On the other hand, it requires
    the user to manually set all the values in the array, and should be
    used with caution.
    
    Examples
    --------
    >>> np.empty([2, 2])
    array([[ -9.74499359e+001,   6.69583040e-309],
           [  2.13182611e-314,   3.06959433e-309]])         #uninitialized
    
    >>> np.empty([2, 2], dtype=int)
    array([[-1073741821, -1067949133],
           [  496041986,    19249760]])                     #uninitialized

>>> np.empty((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> 
================================ RESTART: Shell ================================
>>> import numpy as np
>>>  np.linspace(1,100,num=5)
 
SyntaxError: unexpected indent
>>> np.linspace(1,100,num=5)
array([  1.  ,  25.75,  50.5 ,  75.25, 100.  ])
>>> np.linspace(1,100,num=6)
array([  1. ,  20.8,  40.6,  60.4,  80.2, 100. ])
>>> np.linspace(1,100,num=5,endpoint="False")
array([  1.  ,  25.75,  50.5 ,  75.25, 100.  ])
>>> np.linspace(1,100,num=5,retstep=True)
(array([  1.  ,  25.75,  50.5 ,  75.25, 100.  ]), 24.75)
>>> np.linspace(1,100,num=5,retstep=False)
array([  1.  ,  25.75,  50.5 ,  75.25, 100.  ])
>>> np.linspace(1,50)
array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11., 12., 13.,
       14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26.,
       27., 28., 29., 30., 31., 32., 33., 34., 35., 36., 37., 38., 39.,
       40., 41., 42., 43., 44., 45., 46., 47., 48., 49., 50.])
>>> np.linspace(1,50,dtype=int)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
>>> np.array([-1,-3])
array([-1, -3])
>>> 
================================ RESTART: Shell ================================
>>> np.eye(2)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    np.eye(2)
NameError: name 'np' is not defined
>>> import numpy as np
>>> np.eye(5)
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
>>> np.eye(3,4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.]])
>>> np.eye(4,k=3)
array([[0., 0., 0., 1.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> np.eye(4,k=5)
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> np.eye(4,5,k=6)
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
>>> np.eye(4,5,k=-2)
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.]])
>>> np.identity(4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])
>>>  np.identity(4,dtype=int)
 
SyntaxError: unexpected indent
>>> 