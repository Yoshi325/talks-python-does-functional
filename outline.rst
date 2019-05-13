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

- What are you looking for from this Talk?
- I might call a L.A.F.O.

.. notes::

  Start off with Q&A about what people would like to get from this talk.
  Mention LAFO (Listen and find out, from: Read And Find Out, but for presentations).

  Mention that it is okay to ask questions mid-talk.

  Also mention that Functional Programming is a very old idea (atleast as old
  as Lisp; 1950s). So there isn't much original content for this talk. Rather,
  it is a packaging of and a focus on how Python does functional.

  Oh, and on that, Lisp is multi-paradigm too...

  I don't cover monads. That's a whole 30 minute talk in itself.


*******
Summary
*******

.. notes::

  This talk is not exhaustive. My intention is to address specific items and
  help you "dip your toe" into Functional Programming with Python.


******
Secret
******

.. notes::

  I'll tell you a secret.

  You're already doing this if you've done any serious Python work.

  You just might not realize it.


****************
Want More Later?
****************

Want more information, with more accurate terms?

https://docs.python.org/3.7/howto/functional.html


****************
Terms & Concepts
****************

Let's learn the lingo.

- Side Effects
- Pure Functions
- Referential Transparency
- First-Class Functions
- Higher-Order Functions
- Partial Function Application
- Currying
- Function Composition
- Pipeline Style


************
Side Effects
************

Manipulation of state outside the function.

.. code:: python

  def add(a, b):
    print('Hello!') # side effect
    global c; c = 5 # side effect
    with open('./README.rst') as handle:
        handle.write('abcd') # side effect
    return (a + b)

.. notes::

  the concern here is hidden or unpredictable behavior, which makes understanding and testing harder


**************
Pure Functions
**************

Functions without Side Effects.

.. code:: python

  def add(a, b):
    return (a + b)

.. notes::

  Math lends itself well to this. At it's core, functional programming was born
  from math (lambda calculus).


************************
Referential Transparency
************************

One or more Pure Functions (composed to) create a result that is repeatable
from the same set of initial inputs.

.. code:: python

  def add(a, b):
    return (a + b)

  def sub(c, d):
    return (c - d)

  e = sub(6 - 4)
  f = add(1, e)
  # f == 3

.. notes::

  f will always equal 3

  we can use this with `memoization`, "an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again."

  https://en.wikipedia.org/wiki/Memoization


*********************
First-Class Functions
*********************

  This means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures

  https://en.wikipedia.org/wiki/First-class_function


**********************
Higher-Order Functions
**********************

Functions that operate on (and return) Functions.

.. code:: python

  def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

.. notes::

  source: https://stackoverflow.com/a/309000

  anyone think they might recognize a way Python might specifically utilize these?

  (decorators)

  these are also called "combinators"

  anyone have another name for the inner function?

  (closure)

  we will get back to that later


****************************
Partial Function Application
****************************

  [...] fixing a number of arguments to a function, producing another function of smaller arity.

  https://en.wikipedia.org/wiki/Partial_application


.. notes::

  Can be used to reduce the number of arguments. (arity == number of arguments)


****************************
Partial Function Application
****************************

.. code:: python

  import operator
  from functools import partial

  add_one = partial(operator.add, 1)
  # add_one == functools.partial(<built-in function add>, 1)

  a = add_one(2)
  # a == 3

.. notes::

  Possibly could be used to reduce the `arity` to 1. Which leads into...


********
Currying
********

Taking a function with multiple arguments, and re-expressing it as a series of functions with one argument.

.. code:: python

  # see previous example

.. notes::

  But it can be taken further. Much further.


********************
Function Composition
********************

Composing multiple functions to produce a single result.

.. code:: python

  add_two = partial(add, 2)
  mul_two = partial(mul, 2)
  x = add_two(mul_two(10))

  add_and_mul_two = lambda y: add_two(mul_two(y))

  z = add_and_mul_two(10)

  # x == z


**************
Pipeline Style
**************

Nope.

.. notes::

  Python doesn't have this. We will talk about it later.

  But basically it's taking an input, then passing it to subsequent callables with arity of one.


****************
Terms & Concepts
****************

More lingo.

- Tail Call Optimization
- Pattern Matching
- Data Modeling
- Immutability
- Algebraic Data Types


**********************
Tail Call Optimization
**********************

Nope. Python doesn't have this either.


**********************
Tail Call Optimization
**********************

  Tail-call optimization is where you are able to avoid allocating a new stack frame for a function because the calling function will simply return the value that it gets from the called function. The most common use is tail-recursion, where a recursive function written to take advantage of tail-call optimization can use constant stack space.

  https://stackoverflow.com/a/310980/135342


**********************
Tail Call Optimization
**********************

You'll know you want this when you hit the recursion limit in Python.


****************
Pattern Matching
****************

Ugh. Still Nope. Python doesn't have this either.


.. notes::

  Switch statement on steriods.

  (yeah, I know, Python doesn't have those).

  Often used to match on types, as well as other attributes.


*************
Data Modeling
*************

Phew. Back on track.

Accurate Data Modeling is very important to Functional Programming, because the data and functionality are firmly separated.


*************
Data Modeling
*************

- dataclasses
- type hints

.. notes::

  Now in Python 3.7, we have dataclasses and type hints that allow for very robust modeling.

  Also, Python 3.6 via a package.


*************
Data Modeling
*************

.. code:: python

  from typing import List
  from typing import Optional
  from dataclasses import dataclass

  @dataclass(frozen=True)
  class LineItem:
    item_id :int
    notes   :Optional[str]

  @dataclass(frozen=True)
  class Orders:
    order_number :str
    items        :List[LineItem]


************
Immutability
************

by ref? by val?

stop the madness!

.. code:: python

  Person = namedtuple('Person', ['name', 'favorite_color'])
  that_guy = Person('Barry', 'yellow')
  that_guy._replace(favorite_color='blue')

  @dataclass(frozen=True)
  class Person:
    name :str
    favorite_color :str

  # inst.replace(favorite_color='blue')


********************
Algebraic Data Types
********************

Here we go again...

Python does not natively have Algebraic Data Types.

.. notes::

  (sum types)

  foundation of `Maybe` or `option`


********************
Algebraic Data Types
********************

But! We can emulate this with things from `typing`.

.. code:: python

  @dataclass
  class ItemShapeEmpty: pass

  @dataclass
  class ItemShapeLegacy:
    name        :str
    description :str

  @dataclass
  class ItemShapeModern:
    id        :int
    name      :str
    detail_id :int

  Item = NewType('Item', Union[
      ItemShapeEmpty,
      ItemShapeLegacy,
      ItemShapeModern,
  ])


***********
What is it?
***********

  Functional programming can be considered the opposite of object-oriented programming.

.. notes::

  Functionality is kept separate from data. There are many advantages to this.


***********
What is it?
***********

  Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input.

.. notes::

  That doesn't sound very useful. How can we operate without side effects?

  But there is alot of good that can come from having a "functional" core,
  with a shiny, interop/side effect candy shell.



************************************
Native Python Functional Affordances
************************************

(batteries included doesn't just apply to system calls)

- functions are first class objects
- boolean expressions are short-circuited
- enumerate
- any
- all


************************************
Native Python Functional Affordances
************************************

- iterators
- generators
- itertools
- functools
  - map / filter / reduce
- dataclasses (with `frozen=True` for immutability)
- named tuples (which are immutable by nature)


******
Lambda
******

.. notes::

  Lambda might not be what you think it is. In Python, even when creating what
  Functional Programming would call a lambda, you probably don't want to use
  Python's ``lambda``. Rather, you probably want to create a closure. Python's
  lambdas are "anonymous functions", but are limited to a single line that
  can often make them less understandable. They can operate like a closure,
  but often times that is an unintentional behavior that is subtle enough to be
  missed.


*********
Drawbacks
*********

(specifically when using Functional concepts in Python)

- Tail Call Optimization (recursion limit)
- Pattern Matching
- Automatic Currying
- Pipeline Syntax
- Clean Algebraic Data Types
- Clean Function Composition

.. notes::

  There are a few key things missing from Python for me to consider it a full-fledged Functional Programming Langauge.

  F# type pipeline syntax.


********
Benefits
********

- Modularity
- Composability
- Optimization
- Testing


**********
Modularity
**********

Small pieces (functions) that are composed and applied to a model allows for reusibility.

.. notes::

  espically in Python where Duck Typing rules


*************
Composability
*************

Instead of trying to write W.E.T. functions, or putting them into odd places, composability allows you to build small pieces that you can fit in your head.


************
Optimization
************

These small pieces of functionality lend themselves to inspection, and therefore easy optimization.

One example: memoization


*******
Testing
*******

Similar to what may be said about optimization, testing is easy with Functional Programming.

.. notes::

  traits like immutability and pure functions also provide a solid path to testing


************************
What does it mean to me?
************************

.. notes::

  Personally, this maps to the way I think. I break things down into data, and operations I would like to preform on that data.

  It helps to maintain scope.

  It produces D.R.Y. code.

  It helps me define ways to test units.

  All of this leads to maintainability.


*****
Bonus
*****

`Coconut <http://coconut-lang.org/>`_

  "Coconut is a functional programming language that compiles to Python."

.. notes::

   Which cures all the things I feel are lacking from Python for Functional Programming.


**************
Pipeline Style
**************

.. code:: coconut

  add_two = partial(add, 2)
  mul_two = partial(mul, 2)
  x = add_two(mul_two(10))

  10 |> (mul_two..add_two) |> print


**********************
Tail Call Optimization
**********************

Yup. Coconut does this too.


****************
Pattern Matching
****************

Of course! Coconut adds the `match` keyword.

.. code:: coconut

  match [head] + tail in [0, 1, 2, 3]:
    print(head, tail)


*****
Other
*****

`toolz <https://pypi.org/project/toolz/>`

  A functional standard library for Python.

.. notes::

  maybe you prefer a library to a whole different language?


*****
Other
*****

https://www.pyfunctional.org

  PyFunctional’s API takes inspiration from Scala collections, Apache Spark RDDs, and Microsoft LINQ.


*****
Other
*****

`https://github.com/radix/sumtypes/ <sumtypes>`_

  Sum Types, aka Tagged Unions, for Python


*******
The End
*******