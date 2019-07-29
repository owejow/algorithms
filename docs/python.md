# Python

## Useful Syntax

### Compute number of elements in a range

```python
max(0, (stop - start + step - 1) // step)
```

### Getting mirror image indices

```python
    # ~x returns -x -1
    lst = [1,2,3,4,5]

    idx = 0

    right = lst[idx] # returns 0th element
    left = lst[~idx] # returns -idx-1 element
```

## Coroutines


Coroutines are advanced generators. The caller can post data to the 
coroutine via the **.send(...)..** method. The following methods
are available to the caller of a coroutine (Coroutine notes taken from Fluent Python Clear, Concise, and Effective Programming 1st Edition.)

- **.send(...)**
- **.throw(...)**
- **.close(...)**

!!! Note
    - A generator can now return a value.
    - **yield from** syntax enables complex generators to be refactored into smaller
        nested generators without much boilerplate code.

```python

# Simple Coroutine
def simple_coroutine():
    print('-> coroutine started')
    x = yield                     # simply yields None to the caller
    print('->coroutine received')

my_coro = simple_coroutine()  # call function to get generator back
next(my_coro)  
my_coro.send(42)  
```

A coroutine can be one of four states. The current state can be determined using 
the **inspect.getgeenratorstate(...)** function.

- **GEN_CREATED**: Waiting for start of execution
- **GEN_RUNNING**: Currently executing by the interpreter
- **GEN_SUSPENDED**: Currently suspended at a yield expression
- **GEN_CLOSED**: Execution has completed

Arguments to send become values of the pending **yield**. If the coroutine is suspended
you can send values to it. In order for the coroutine to be suspended it needs to
have been activated. The first activation of a coroutine requires **next(my_coro)** 
to be called. You can also call **my_coro.send(None)** which has the same
effect.

Creating a coroutine and immediately sending a value to it will result in a TypeError

```python
my_coro = simple_coroutine()
my_coro.send(1729)

# TypeError: can't send non-None value to a just-started generator

```

The initial call **next(my_coro)** is called priming a coroutine. Can use the
method **inspect.getgeneratorstate** to get current state of a coroutine:

```python
from inspect import getgeneratorstate

my_coro2 = simple_coro2(2)

getgeneratorstate(my_coro2) # 'GEN_CREATED'

next(my_coro2)  

getgeneratorstate(my_coro2) # 'GEN_SUSPENDED'

my_coro2.send(29) 

my_coro2.send(99)  

getgeneratorstate(my_coro2) # 'GEN_CLOSED'
```

This decorator simplifies working with coroutines in python:

```python
from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first `yield`"""

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer
```

### Coroutine Termination and Exception Handling

Two methods exist for explicitly sending exceptions to a coroutine:

- **generator.throw(exc_type[, exec_value[, traceback]])**: causes yield where generator was paused 
        to raise exception. If exection handled by generator the flow advances to next yeidl and 
        value yielded becomes value of the generator.throw call. If exception not handled it propagates
        to the context of the caller.

- **generator.close()** causes yield expression where the generator was paused to raise
    a GeneratorExit exception. No error is reported to the calller if generator does not handle that
    exception or raises StopIteration. When receing GeneratorExit, the generator must not yield
    a value otherwise RuntimeError is raised. Any exception raised by the generator propagates 
    to the caller.

Unhandled exceptions kill a coroutine:

```python
from coroaverager1 import averager

coro_avg = averager()

coro_avg.send(50)

coro_avg.send('spam') # raises TypeError exception

coro_avg.send(60)  # further attempts will raise StopIteration Error
```

### Coroutine close and throw

Sample code used for demonstrating **close** and **throw**

```python
class DemoException(Exception):
    """An exception type for demonstration."""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never be run')
```

The example below shows normal operation of demo_exc_handling

```python

exc_coro = demo_exc_handling()
next(exc_coro)

exc_coro.send(11)

exc_coro.send(22)

exc_coro.close()  # 'GEN_CLOSED'
```

Can throw DemoException without breaking code:

```python
exc_coro = demo_exc_handling()

next(exc_coro)

exc_coro.send(11)

exc_coro.throw(DemoException) # 'GEN_SUSPENDED'

```

Unhandles exceptions is thrown to the coroutine the state of the coroutine becomes 'GEN_CLOSED'

```python
exc_coro = demo_exc_handling()

next(exc_coro)

exc_coro.send(11)

exc_coro.throw(ZeroDivisionError) # ZeroDivisionError is raised the state of coroutine becomes 'GEN_CLOSED'

```

### Cleanup Code in Coroutine

Can used try and finally to return cleanly from a coroutine

```python
def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
            else:
                print(f'-> coroutined received: {r}')
        finally:
            print('-> coroutine ending')

```


## Iterators and Generators

### Iterator

**iterator** is an object that managers a series of values.

- if variable **i** identifies an iterator object
    ```python
        next(i) # returns subsequent elements
                # raises StopIteration to indicate
                #   no further elements.
    ```

**iterable** is an object that produces an **iterator**

```python
    iter(obj) # returns an iterator
```

A list is an iterable but not an iterator. Can 
use itera(lst) to create an iterator.

```python
   lst = [1,2,3,4]  # can't call next(lst)
   data = iter(lst) # can call next(data)
```

- possible to create multiple iterators based on same iterable object.
- each iterator maintains its own state of progress.
- iterator does not store its own copy of the list of elements. It maintains a current index to the original list.
!!! Note
    if contents of original list are modified after iterator is constructed but before iteration is complete the iterator will report the updated contents of the list.

### Class Iterator

Python provides automatic iterator implementation for any class that defines both **__len__** and **__getitem__**.

```python
class SequenceIterator:
    """An iterator for any of Python's sequence types"""

    def __init__(self, sequence):
        """Create an iterator for a given sequence"""
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1 # will increment to 0 on first call to next
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        self._k += 1 # advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k] # return the data element
        else:
            raise StopIteration() # there are no more elements
    
    def __iter__(self):
        """By convention an iterator must return self as an iterator"""
        return self
```

### Functions and classes as iterable Series

Functions and classes can produce an implicit series of values without constructing the data structure.

```python
    range(1000000) # does not return numbers
                   # lazy evaluation is used
```

Some examples of lazy evaluation:

- in dictionary class:
    - **keys()**
    - **values()**
    - **items()**

## Generators

**generator** is the most convenient technique for creating iterators in Python.

- implemented in a very similar syntax to a function
- use **yield** to return values instead of **return**. this indicates that we are defining a generator rather than a function

```python
def factors(n):      # generator that computes factors
    for k in range(1,n+1):
        if n % k ==  0: 
            yield k # yield factor as next result
```

!!! Warning
    It is illegal to combine **yield** and **return** statements in same implementation other than a zero-argument return statement to cause generator to end its execution.

When control flow naturally reaches the end of a procedure (or a zero-argument **return** statement) a StopIteration exception is automatically raised.

A generator can rely on multiple **yield** statements in different constructs.

```python
def factors(n): # generator computes factors
    k = 1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k
```

### Benefits of Lazy Evaluation

When using **generator** rather than traditional function the results are only computed if requested.

- entire series need not reside in memory at any one time
- generator can effectively produce an infinite series of values

```python
def fibonacci():
    a = 0
    b = 1
    while True: # keep going...
        yield a # report value, a, during this pass
        future = a + b
        a = b   # this will be next value report
        b = future # and subsequently this
```
