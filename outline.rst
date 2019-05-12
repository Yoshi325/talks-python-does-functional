######################
Python DOES Functional
######################


:Author: Charles L. Yost
:Date: 2019-05


***********
Speaker Bio
***********

.. include:: speaker-bio.rst


**************
Binary Defense
**************

.. include:: binary-defense.rst


***************
Speaker Contact
***************

Twitter: @CHARLESLYOST

GitHub & YouTube: Yoshi325

| This Talk:
| https://github.com/Yoshi325/talks-python-does-functional


**************
Pre-Talk Q & A
**************

- L.A.F.O.

..

  Start off with Q&A about what people would like to get from this talk.
  Mention LAFO (aka RAFO, but for presentations).

  Ask questions mid-talk.


*******
Summary
*******


..

  This talk is not exhaustive. My intention is to address specific items and
  help you "dip your toe" into Functional Programming.


******
Secret
******


..

  I'll tell you a secret. You're already doing this if you've done any serious
  Python work. You just might not realize it.


**********
Want More?
**********

Want more information, with more accurate terms? https://docs.python.org/3.7/howto/functional.html


*******************
Functional Concepts
*******************

- Side Effects
- Pure Functions
- Higher-Order Functions
- Separating Data from Function
- Accurate Data Modeling
- Referential Transparency




"higher-order function takes one or more functions as input and returns a new function. The most useful tool in this module is the functools.partial() function."


********
Benefits
********

- Modularity
- Composability
- Testing

Native Python Functional Affordances:
(batteries included doesn't just apply to system calls)
- functions are first class objects
- boolean expressions are short-circuited
- iterators
- generators
- itertools
- functools
- map
- filter
- reduce
- enumerate
- any
- all
- dataclasses (with Frozen for immutability)
- named tuples (which are immutable by nature)

Drawbacks:
- Tail call optimization (recursion limit)
- Pattern matching
- Automatic currying
- Concise way to compose functions
- Syntax


"Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input."

"In a functional program, input flows through a set of functions. Each function operates on its input and produces some output. Functional style discourages functions with side effects that modify internal state or make other changes that aren’t visible in the function’s return value. Functions that have no side effects at all are called purely functional. Avoiding side effects means not using data structures that get updated as a program runs; every function’s output must only depend on its input."


"Functional programming can be considered the opposite of object-oriented programming."


Lambda might not be what you think it is. In Python, even when creating what Functional Programming would call a lambda, you probably don't want to use Python's ``lambda``. Rather, you probably want to create a closure. Python's lambdas are "anonymous functions", but are limited to a single line that can often make them less understandable. They can operate like a closure, but often times that is an unintentional behavior that is subtle enough to be missed.







data modeling via unions and records

