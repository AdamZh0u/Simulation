



### Lecture1:Introduction to Computation

Fundamental Operation support imperative knowledge?
the basic elements of a computer?
how-to recipes[^1]

#### Basics of computation

What does a computer do?           **2 things and 2 things only**

- performs calculations
  - built in primitives
  - creating our own methods 
- remembers results

```
how quickly can a computer calculate?   **light,ball**
	1G = 1,000,000,000bytes
	my computer  = 8*2.5Ghz = 20Gflops
	whuchaosuan =  300,000Gflops
	shenwei  = 93,000,000Gflops

how many can a computer remember?  
```

Are simple calculations enough/sufficient?

- search the web
- playing chess

good algorithm is needed

So,Are there limits of computer?
despite its speed and its size and the cleverness of the algorithm,it still has some limitations:

- Some problems still too complex    **weather,encryption schemes[^2]**
- Some problems are fundamentally impossible to compute 
  - being able to predict whether a piece of code will always stop with an answer for an input(Turing Halting Problem)

#### Computational problem solving

What is computation?

- what is knowledge?
  - declarative knowledge           $x*x = y$
    - statements of fact
  - imperative knowledge          **how to find x?**
    - "how to "methods

> Statements of facts give us truth ,but,they don't necessarily help us think about how to find new information. Imperative knowledge,how-to methods or recipes ,give us ways of finding new information,and that's going to be really valuable to us.
>
> 	--Eric Grimson

Algorithms are recipes
	recipe to cook

How do we capture a recipe in a mechanical process?

- Fixed Program Computers
  - calculator
  - Alan Turing bombe
- Stored Program Computer 

#### Stored Program Computer

Sequence of instructions stored inside computer

- built from predefined set of primitive instructions
  - simple Arithmetic,Logic
  - simple Tests
  - move data

Special program (interpreter) executes each instructions in order

![image](.\TIM截图20180716231241.png)

What are basic primitives?

Turing showed that using six primitives,can compute anything

--Turing Complete

#### Primitive Constructs

Static semantics

Syntactic Error

[^1]: n 秘方
[^2]: n加密，编密码 /n 计划，阴谋 v 策划，图谋

----

### Lecture 2 :Core Elements of Programs

#### Types of program language

Low Level Language
High Level Language
Compiled Language
Interpreter Language

#### Objects

- Scalar objects
  - int
  - float
  - bool
- Non-scalar objects
  - str

#### Expressions

#### Binding Variables

```python
"a"+str(3)
3*"a"
"abc"[0]
```

#### Branch Program

```python
x=1
if x%2 ==0:
    print("done")
elif x%3 ==0:
    print("done.")
else:
    print("Done")
```

```python
for i in range(0,20):
    y = i+1
    print(y)
    
```

---

### Lecture 3: simple algorithms

#### Intro

Iteration
loop constructions
Successive Approximation[^3]
Bisection Search[^4]
Improving Approximate Estimate of answer to solve Numerical Problems

#### Iteration

```python
x = 3
ans = 0 
itersleft = x#剩下的累加次数
while(itersleft != 0 ):
    ans = ans +x
    itersleft = itersleft - 1
print(str(x)+ "*"+str(x)+ "="+str(ans))
```

循环要素：变量、测试、改变变量

循环内和循环外定义的变量的差异？

It's a generalization of a conditional.

**Branching structures** :jump to different pieces of code base on a test/Programs are constant time[^5]
**Loop structures**:repeat pieces of code until a condition is satisfied /time depends on value of variables and length of program

####Classes of algorithms

#### Guess and check

find a cube root of an integer

```python
x = int(input("enter an integer:"))
ans = 0
while ans**3<abs(x):
    ans = ans + 1
if ans**3!=abs(x):
    print(str()+"is not a perfect cube")
else:
    if x < 0 :
        ans = -ans
    print("Cube root of "+str(x)+ " is "+str(ans))
```

Exhaustive Enumeration[^6]

####Loop characteristic

* need a loop variable
  * Initialized outside loop
  * Changes within loop
  * Test for termination depends on variable
* Useful to think about a **decrementing function**
  * Maps set of program variables into a integer
  * When loop is entered ,values is non-negative
  * When value is <= 0,loop terminates
  * Value is decreased every time 

#### For loops

While loops generally iterate over a sequence of choices

```python
for <identifier> in <sequence>:
    <code block>
    if <identifier2>:
        break
```

generate a sequence of integer

```python
x = int(input("enter an integer"))
for ans in range(0,abs(x)+1):
    if ans**3 ==abs(x):
        break
if ans**3 != abs(x):
    print(str(x)+"is not a perfectcube")
else:
    if x < 0:
        ans = -ans
    print("Cube root of "+str(x)+" is "+str(ans))
```

####Dealing with floats

How float are represented inside computer?

* Floats approximate real numbers,but useful to understand how
* Decimal number
* Binary number

Convert decimal integer to binary

x /2 --x/2/2--x/2/2/2...

```python
num = 302
if num <0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ""
if num ==0:
    result = "0"
while num >2:
    result = str(num%2)+result
    num = num/2
if isNeg:
    result = "-"+result
    
```

####Dealing with Fractions

```python
x = float(input("enter a decimal number between 0 and 1:"))
p = 0
while((2**p)*x)%1 != 0:
    print("Remainder = "+str((2**p)*x)-int((2**p)*x))
    p+=1
```

####Approximate Solutions	

```python
x= 25
epslion = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while (abs(ans**2-x))>= epsilon and ans<=x:
    ans+=step
    numGuesses +=1
print("numGuesses =" + str(numGuesses))
if abs(ans**2-x)>= epsilon:
    print("Failed on square root of "+str(x))
else:
    print(str(ans)+ " is close to the square root of "+ str(x))
```

step could by any number

####Bisection Search

the difference between Bisection Search and Exhaustive  Enumeration?

```python
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x)>=epsilon:
    print("low = "+str(low)+"high = "+str(high)+"ans = "+str(ans))
    numGuesses +=1
    if ans **2 <x:
        low = ans
    else:
        high =ans
    ans = (high + low)/2.0
print("numGuesses = "+str(numGuesses))
print(str(ans)+"is close to square root of "+str(x))
```

It radically reduces computation time

It should work on problems with "ordering"  property

####Newton-Raphson

simple case :cx^2^+k
First derivative:2cx
Guess is g -(g^2-k^)/2g

```python
epsilon = 0.01
y =24.0
guess = y/2.0
while abs(guess*guess - y)>=epsilon:
    guess = guess -(((guess**2)-y)/(2*guess))
    print(guess)
print("Squre root of "+str(y)+ " is about "+str(guess))
```

* Guess and check methods builds on reusing same code
  * Use a looping construct to generate guesses,then check and continue
* Generating guesses
  * Exhaustive enumeration
  * Bisection search
  * Newton-Raphson (for root finding)



[^3]: 逐次逼近
[^4]: 二分查找
[^5]: 常数时间
[^6]: 完全枚举

---

### Lecture4:Fuctions

#### Intro

Looping computation and abstract them
Black box abstraction

Formalism called environments
assignment of names to values
how those values are retrieved
 how we can use those ideas to conceptualize[^7] new algorithms

看起来简单的东西听他讲起来格外厉害点？

####Functions

* Numbers,assignments,input/outputs,comparisons,looping constructs

  --Sufficient to be Turing Complete--can compute everything

* but code lacks abstraction
* Functions give us abstraction -allow us to capture computation and treat as if primitive

####Capturing computation as a function

* idea is to encapsulate this computation within a scope such that can treat as primitive

  * Use by simply calling name ,and providing input
  * Internal details hidden from users

* Syntax

  ```python
  def <function name>:
      <function body>
  ```

  ```python
  def max(x,y):
      if x>y:
          return x
      else:
          return y
  ```

  Function returns

  * body can consist of any number of legal Python expressions
  * Expressions are evaluated until
    * Run out of expressions, in which case special value None is returned
    * Keyword ==Return==

#### Environments to understand bindings

* Environments are formalism for tracking bindings of variables and values
* Assignments pair name and value in environments
* Asking for value of name just look up in current environment
* Python shell is default environment
* Definitions pair function name with details of function

> Encapsulation can protect the interior details

```python
x = float(input(“enter a number:”))
p = int(input("enter an integer:"))
def iterativePower(x,p):
    result =1
	for turn in range(p):
    	print("iteration:"+str(turn)+"current result:"+str(result))
    	result = result*x
	return result
```

Formal Parameters:形式参数

Understand E1 and E2

![](TIM截图20180719045332.png)

> All of this computation takes place in the local environment.
>
> Procedures give us this wonderful notion of abstraction.

```python
def f(x):
	y = 1
	x = x+y
	print("x= “+str(x))
	return x
```

* each function call creates a new environment, which scopes bindings of formal parameters and values ,and of local variables 
* Scoping often called static or lexical[^8], because scope within which variable has value is defined by extent of code boundaries

Invoke[^9]functions

```python
def findRoot1(x,power,epsilon):
    low = 0 
    high = x
    ans = (high +low)/2.0
    while abs(ans**power - x)>epsilon:
        if ans**power <x:
            low =ans
        else:
            high = ans
        ans = (high+low)/2.0
        return ans
```

Specifications

* A contract between implementer of function and user
  * Assumptions:conditions,constraints
  * Guarantee:Conditions,

Functions Properties

* Decomposition:Break problem into modules ,can be reused in other settings
* Abstraction: Hide details ,interior details

####Using functions in Modules

* Modularity suggests grouping functions together that share common theme
* place in .py file
* Use import command to access
  * import circle
  * from circle import *
    * bring all into the environment

armamentarium of tools

[^7]: 概念化
[^8]: 静态域 语汇域
[^9]: 祈求

---

###Lecture 5:Recursion

#### Intro

Recursion:Reduce a computation to a simple version of the same problem

#### Iterative Algorithms

* Looping construction lead naturally to **iterative** algorithms
* Can conceptualize as capturing computation in a set of "state variables" which update on  each iteration through the loop

状态变量！！！！

####Example:Iterative multiplication by successive additions

- To multiply a by b, add a to itself b times
- State variables
  - i - iteration number; starts at b
  - result - current value of computation; starts at 0
- Update rules

```python
def iterMul(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
```

#### Recursive version

* Reduce a problem to a simpler version of the same problem
  * Recursive step
* Keep reducing until reach a simple case that can be solved directly
  * Base case

```python
def recurMul(a,b):
    if b ==1:#Base case
        return a
    else:# Recursive Step
        return a + recurMul(a,b-1)
#amazing
```



> definitions where you defined a term in terms of itself

* Each recursive call to a function creates its own environment,with local scoping of variables
* Bindings for variables in each frame are distinct , and binding are not changed by the recursive call
* Flow of control will pass back to earlier frame once function call return value

> So hopefully this give us a better sense of how the rules of evaluation allow a recursive thinking of a problem to create a very nice version of the code.

####Mathematical induction

* To prove a statement indexed on integers is true for all values of n:
  * prove it is true when n is smallest value (n=0,n=1)
  * Then prove that if it is true for an arbitrary value of n, one can show that it must be true for n+1
  *  数学归纳法 induction

####The "classic" recursive problem

* Factorial : n!

  * $$
    n! = \begin{cases}
    n*(n-1)! &\text{n>1}\\
    1 &\text{n=1}
    \end{cases}
    $$







```python
#递归
def factR(n):
    if n==1:
        return n
    return n*factR(n-1)

#迭代
def factI(n):
    res = 1
    while n>1:
        res = res*n
        n-=1
    return res
```

####Towers of Hanoi

```python
def printMove(fr,to):
    print("move from " +str(fr)+"to"+str(to))
    
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,spare,to)
        Towers(n-1,spare,to,fr)
```

####Recursion with multiple base cases

* 第二数学归纳法
* Fibonacci numbers
  * Leonardo of Pisa(aka Fibonacci)

```python
def fib(x):
    assert type(x)==int and x>=0:
    if x==0 or x==1:
        return 1
    else:
        return fic(x-1)+fib(x-2)
```

####Recursion on non-numerics

```python
def isPalindrome(s):
	def toChars(s):
		s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
       
    return isPal(toChars(s))
```

#### Global Variables

```python
def fibMetered(x):
    global numCalls
    numCalls+=1
    if x==0 or x==1:
        return 1
    else:
        return fibMetered(x-1)+frbmetered(x-2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print("fib of "+str(i)+"="+ str(fibMetered(i)))
        print("fib called "+ str(numCalls)+" times")
```

***

### Lecture 6:Compound data objects

#### Intro

tuple
list
dictionary
scalar 

#### Tuples

* Ordered sequence of elements

* Elements can be more than just characters,even other structures

* Operations

  * concatenation     t~1~+t~2~
  * Indexing               t~1~[3]
  * Slicing                   t~1~[2:5]
  * Singletons             t~3~=(3,)

* can iterate over tuples just as we can iterate over strings

  * ```python
    def findDivisors(n1,n2):
        divisors = ()
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                divisors = divisors + (i,)#add tuple way
        return divisors
    ```

####Lists

* Ordered sequence of values,each identified by an index

* Operations

  * Singletons	[3]

  * append           list.append()

  * Iteration         for i in list 

  * Flat                 +

  * remove

  * Cloning

    * ```python
      def removeDups(L1,L2):
          L1Start=L1[:]
          for e1 in L1:
              if e2 in L2:
                  L1.remove(e1)
          return L1+L2
      ```

* **Big Difference**

  * Lists are mutable!
  * Tuple,integer,float,string are immutable(think about change a string)
  * List can be modified after created

```python
Techs = ["MIT","Cal Tech"]
Ivys = ["Harvard","Yale","Brown"]
Univs = [Techs,Ivys]
Univs1 = [["MIT","Cal Tech"],["Harvard","Yale","Brown"]]
#evaluate
Techs.append("RPI")
print(Univs,Univs1)
```

* Aliasing
  * two distinct paths to a data object
    * through the variable Techs
    * through the first elements of the list object to which Univs is  bound
  * can mutate object through either path,but effect will be visible through both
  * Convenient but **treacherous**

> Mutation , that ability to change things, is really important.

####Dictionaries

* Dict is generalization of lists,but now indices don't have to be integer -can be values of any immutable type
* Refer to indices as keys ,since arbitrary in form
* A dict is then a collection of <keys,Values> pair
* Syntax
* Operation
  * Index by key
  * insert     Dict[""]=
  * iteration    for i in Dict:
  * Dict.keys   Dict.values
* keys can be complex
  * Dict[(1,2)]
  * Keys must be immutable,so have to use a tuple,not a list

***

### Lecture 7:Testing and debug

#### Testing and debugging

* would be great if our code always worded properly the first time we run it 
* Focusing on black box testing , where we exercise paths through the specification
* Glass box testing where we exercise paths through the code 
* Isolating the location of bugs in our code 
* Treating debugging as a search process ,and use the ideas of binary search to help isolate and detect bug sources

####When should we debug and test? 

* Design you code for ease of testing and debugging 
  * break program into components that can be tested and debugged independently
  *  Document constraints on modules
    * Expectations on input /outputs
    * Even if code does not enforce constraints ,valuable for debugging to have description
  * Document assumptions behind code design

#### When are you ready to test?

* ensure that code will actually run
  * remove syntax errors
  * remove **static semantic errors**
  * Both of these are typically handled by python interpreter
* Have a set of excepted results ready

#### Testing

* Goal:
  * show that bug exist
  * would be great to prove code is bug free,but generally hard
    * Usually can't run on all possible inputs to check
    * Formal methods sometimes help,but usually only on simpler code 

#### Test Suite

* Want to find a collection of inputs that has high likelihood of revealing bugs ,yet is efficient
  * Partition space of inputs into subsets that provide equivalent information about correctness  
    * Partition divides a set into group of subset such that each elements of set is in exactly one subset 
  * Construct test suite that contains one input from each element of partition
  * Run test suite

```python
def isBiggr(x,y):
     """Assumes x and y are ints
     returns True if x is less than y
     else False
     """
```

* input space is all pairs of integers
* Partition
  * x + ,y -
  * x +, y +
  * x - , y +
  * x - , y -
* Why this partition?
  * Lots of other choices
    * x prime ,y not (质数)
    * y prime, y not
  * Spaces of inputs often have natural boundaries
    * integers are positive ,negative or zero
    * From this perspective , have 9 subsets
      * split x = 0 ,y!= 0 into ,x= 0 ,y positive ....

#### Partitioning 

* What if no natural partition to input space?
  * Random testing -- probability that code is correct increases with number of trials;but should be able to use code to do better 
  * Use heuristics based on exploring paths through the specifications --black box testing 
  * Use heuristics based on exploring paths through the code -- glass box testing

#### Black box testing 

* test suite designed without looking at code 
  * can be done by someone other than implementer 
  * Will avoid inherent biases of implementer , exposing potential bugs more easily
  *  Testing designed without knowledge of implementation, thus can be reused even if implementation changed

> that sort of separation of the details of the implementation from the use of the implementation .That abstract is an important part of how we build modules .And testing should take advantage of that.

```python
def sqrt(x,eps)：
	""""
	Assumes x,eps floats
    	x >= 0
        eps >= 0
    return res such that 
    	x- eps <= res *eps <= x +eps
    """
```

* paths through specification:
  * x>0
  * x<0

#### Glass box  testing

* use code directly to guide design of test cases
* glass box test suite is **path-complete** if every potential path through the code is tested at least once
  * no always possible if loop can be exercises arbitrary times, or recursion can be arbitrarily deep
* Even path-complete suite can miss a bug,depending on choice of examples

```python
def abs(x):
    if x <-1:
        return -x
    else:
        return x
    
```

* test suite of {-2,2} will be path complete
* but -1 have a bug
* Rules of thumb for glass box testing
  * exercise both branches of all if statements
  * ensure each except clause is executed
  * for each for loop ,have tests where:
    * loop is not entered
    * body of loop executed exactly once
    * body of loop executed more than once
  * for each while loop
    *  same cases as for loops
    * cases that catch all ways to exit loop
  * for recursive functions,test with no recursive calls,one recursive call ,and more than one recursive call

#### Conducting tests

* Start with unit testing
  * Check that each module works correctly
* Move to **Integrations testing**（集成测试）
  * check that system as whole works correctly
* cycle between these phases

#### Test Drivers and stubs

* drivers are code that
  * set up environment needed to run code 
  * invoke code on predefined sequence of inputs
  * save results and report
* Drivers simulate parts of program that use unit being tested
* Stubs（存根） simulate parts of program used by unit being tested
  * allowed you to test units that depend on software not yet written 

#### good testing practice

* Start with unit testing
* move to integration testing
* After code is corrected,be sure to do regression testing:
  * Check that program still passes all the tests it used to pass, that your code fix hasn't broken something that used yo work 

#### Runtime bugs

* Overt vs covert(显式与隐式)
  * Overt has an obvious manifestation - code crashes or runs forever
  * Covert has no obvious manifestation - code returns a value,which may be incorrect but hard to determine
* Persistent vs intermittent(持续与间歇)
  * Persistent occurs every time code is run 
  * Intermittent only occurs some times ,even if run on same input

#### Categories of bugs

* Overt and persistent
  * use **defensive programming**
* Overt and intermittent
* Covert

#### debugging skills

* Treat as a search problem : looking for explanation for incorrect behavior
  * Study available data - both correct test cases and incorrect ones
  *  Form an hypothesis consistent with the data
  * Design and run a repeatable experiment with potential to refute[^10] the hypothesis
  * keep record of experiment performed : use narrow range of hypothesis

#### Debugging as search

* want to narrow down space of possible sources of error
* Design experiments that expose intermediate stages of computation and use results to further narrow search
*  Binary search can be a powerful tool for this

把print作为分界点进行二分查找的思想 

eliminate[^11] locations

[^10]: 驳回反对
[^11]: 淘汰

***

### Lecture 8 : Assertions and Exceptions

#### Intro

* Two approaches
  * Exception :how to have code deal with unexpected conditions in structured ways 
  * Assertion:ensure that the assumptions we make on both the input and the output of code are correct

#### Exception

* Exceptions to what was expected
  * Index Error list[5]
  * Type Error int(test)
  * Name Error a
  * Type Error "a"/4 
* deal with it: What to do when procedure execution is stymied[^12] by an error condition?
  * Fail silently:substitute default values, continue
  * Return an "error" value 
  * Stop execution,signal error condition
    * in python :raise an exception
* python code can provide handlers for exceptions

```python
try:
    f = open("grade.txt")
except:
    raise Exception("can't ...")
    
```

* Exceptions raised by statements in body of **try** are handled by the **except** statement and execution continues with the body of the **except** statement

* handling specific exception

  * Usually the handler is only meant to deal with a particular type of exception.Sometimes we need to clean up before continuing

  * ```python
    try:
        f= opne("grade.txt")
    except IOerror,e:#e:error object
        print("can't open grades file:"+str(e))
        sys.exit(0)
    except ArithmeticError,e:
        raise ValueError("Bug in grades calculation"+str(e))
    ```

* Types of exceptions

  * SyntaxError
  * NameError
  * AttributeError
  * TypeError
  * ValueError
  * IOError

* Other extensions to try

  * else:when **try** completes with no exceptions
  * finally:executed after **try,else, except**,even if raised another error or executed a **break,continue or return** 

```python
def ivide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        divide(int(x),int(y))
    else:
        print("result is ",result)
    finally:
        print("executing finally clause")
```

#### An example of exceptions:As a way of controlling the flow through code 

* Assume we are given a class list for a subject:each entry is a list of two parts - a list of first and last name for a student ,and a list of grades on assignments
* create a new subject list.

```python
def getSubjectStats(subject,weights):
    def:
        return[[elt[0],elt[1],avg(elt[1],weights)] for elt in subject]
	except ZeroDivisionError:
        print("no grades data")
        return 0.0
    
def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

def avg(grades,weights):
    try：
    	return dotProduct(grades,weights)/len(grades)
	except ZeroDivisionError:
        print("no grades data")
        return 0.0
    except TypeError:
        newgr = [convertLetterGrade(elt) for elt in grades]
        return dotProduct(newgr,weights)/len(newgr)
    
def convertLetterGrade(grade):
    if type(grade)== int:
        return grade
    elif grade =="A":
        return 90.0
    else:
        return 50.0
```

#### Exception as flow of control

* In traditional programming languages,one deals with errors by having functions return special values
* Any other code invoking a function has to check whether "error value" was returned
* In python , can just raise an exception when unable produce a result consistent with function's specification
  * raise exceptionName(arguments)

```python
def getRatios(v1,v2):
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float("NaN"))
        except:
            raise ValueError("getRatios called with bad arg")
    return ratios
```

#### Compare to traditional code

* harder to read, and thus to maintain or modify
* Less efficient
* Easier to think about processing on data structure abstractly, with exceptions to deal with unusual or unexpected cases

#### Assertions

* If we simply want to be sure that assumptions on state of computation are as expected,we can use an **assert** statement
* We can't control response, but will raise an **Assertion Error** exception if this happens
* This is good defensive programming

#### Extending use of assertions 

* While pre-conditions on inputs are valuable to check, can also apply post-conditions on outputs before proceeding to next stage

```python
def avg(grades,weights):
    assert not len(grades)==0,"no grades data"# pre conditions
    assert len(grades)==len(weights),"wrong number grade"
    newgr = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgr,weights)/len(newgr)
    assert 0.0<=result<=100.0# post conditions
    return assert
```

[^12]: 陷入困境

***

### Lecture 9：Efficiency and Orders of Growth

#### Intro

* measure complexity of different algorithms
* What is complexity,different classes of algorithms and their inherent complexity
  * constant
  * linear
  * polynomial
  * exponential

#### Measuring complexity

* returns the correct answer on all legal inputs 

* performs the computation efficiently

* balance minimizing computational complexity with conceptual complexity

* how do we measure complexity?

  * problem it depends on :

    * speed of computer 
    * specifics of python implementation
    * value of input

  * how to avoid 1,2?

    * use random access machine(RAM)as model of computation
      * Steps are executed sequentially
      * step is an operation that takes constant time 
        * assignment
        * comparison
        * Arithmetic operation
        * Accessing object in memory 

  * how to avoid 3?

    * ```python
      def linearSearch(L,x):
          for e in L:
              if e ==x:
                  return True
          	return False # complexity depends on input L
      ```

    * Best cases: minimum running time over all possible inputs of a given size 

    * Worst cases : maximum running time 

    * Average case:

    * we focus on worst case - a kind of upper bound on running time 

```python
def fact(n):
    answer = 1
    while n>1:
        answer *= n 
        n -= 1
    return answer    
```

* number of steps :
  * 1(assignment)
  * 5*n
  * 1（return）
* Given the difference in iterations through loop, multiplicative factor probably irrelevant
* Focus on measuring the complexity as a function of input size 
  * focus on the largest factor in this expression
  * concerned with the worst case scenario

#### Asymptotic notation

* Need a formal way to talk about relationship between running time and size of inputs

* Mostly interested in what happens as size of inputs gets very large i.e. approaches infinity

*  ```python
  def f(x):
      for i in range(1000):
          ans = i
      for i in range(x):
          ans+=1
      for i in range(x):
          for j in range(x):
              ans+=1
  ```

  Complexity is 1000+2x+2x^2^,if each line takes one step

  * if x is small, constant term dominates
  * if x in large, quadratic term dominates 

#### Rules of thumb for complexity

* Asymptotic complexity
  * describe running time in terms of number of basic steps
  * if running time is sum of multiple terms, keep one with the largest growth rate 
  *  if remaining term is a product,drop any multiplicative constants

#### Complexity classes

* O(1)denotes constant running time 
* O(log n )denotes logarithms 
* O(n) linear 
* O(n log n) log linear
* O(n^c^)polynomial
* O(c^n^)exponential

$\omicron$

#### Constant complexity

* Complexity independent of inputs 
* Very few interesting algorithms in this class,but can often have pieces that fit this class
* Can have loops or recursive calls, but number of iterations or calls independent of size of input 

#### Logarithms complexity

* Complexity grows as log of size of one of its input
* Example:
  * Bisection search
  * Binary search of a list

为什么二分法是对数算法？

```python
def inToStr(i):
    digits = "0123456789"
    if i == 0 :
        return "0"
    result = ""
    while i >0:
        result = digits[i%10]+result
        i = i/10
    return result
```

#### Linear complexity

* Searching a list in order to see if an element is present
* Add characters of a string , assumed to be composed of decimal digits 

```python
def addDigits(s):
    val = 0 
    for c in s:
        val+= int(c)
    return val
```

* Complexity can depend on number of recursive calls 

```python
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
```

* number of recursive calls ?
  * Fact(n),then fact(n-1)
  * Complexity of each call is constant
  * O(n)

#### Log-linear complexity

* many practical algorithms are log-linear
* Very commonly used log-linear algorithms is merge sort
* Will return to this 
  * merge sort

#### Polynomial complexity

* most common polynomial algorithms are quadratic
* Commonly occurs when we have nested loops or recursive function calls

```python
def isSubset(L1,L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True 
                break
        if not matched:
            return False
    return True
```

O(len(L1)*len(L2))

#### Quadratic complexity

```python
def intersect(L1,L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not( e in res):
            res.append(e)
    return res
```

####Exponential complexity

* Recursive functions where more than one recursive call for each size of problem
* Many important problems are inherently exponential 

```python
# 集合的所有子集  写的真好
def genSubsets(L):
    res = []
    if len(l)==0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
	return smaller + new
```

* O(2^n^)

#### Comparing complexity

* So does it really matter if code is of a particular class of complexity?
* Depends on size of problem, but for large scale problems , complexity of worst case makes a difference

####Observations

* a logarithmic algorithms is often almost as good as a constant time algorithms
* Logarithms costs grow very slow
* Logarithms$??????$

离散过程到连续的理解

***

### Lecture 10: Memory and Search

#### Algorithms and data structures

* how to find efficient algorithms?
  * hard to invent new ones 
  * Easier to reduce problems to known solutions
    * understand inherent complexity of problem
    * think about how to break problem into sub-problems 
    * Relate sub-problems to other problems for which there already exist efficient algorithms 

#### Search algorithms

* search algorithms - methods for finding an item or group  of items with specific properties within a collection of items 
* Collections called the search space
* Saw examples - finding square root as a search problem 
  * Exhaustive enumeration
  * Bisection search 
  * Newton-Raphson

#### Linear search and indirection

* simple search methods

  * ```python
    def search(L,e):
        for i in range(len(L)):
            if L[i] == e:
                return True
        return False
    ```

  * O(len(L))

* Complexity?

  * if element not in list ,O(len(L)) tests
  * so at best linear in length of L
  * why "at best linear?"
    * assume each test in loop can be done in constant time 
    * But does python retrieve the i^th^ element of a list in constant time?

#### Indirection

如果知道每个元素大小是固定的，位置可以在常数时间中计算出来 ，不需要遍历整个列表

* but what if list is of objects of arbitrary size？

* Use indirection

* Represent a list as a combination of a length(number of objects),and a sequence of fixed size pointers to objects(or memory addresses)

  > each elements of the list  isn't going to be the element itself, it's going to be a pointer(指针) to an object, a pointer to a structure in memory

![](TIM截图20180729112115.png)

* If length filed is 4 units of memory, and each pointer occupies 4 units of memory
* the address of i^th^ element is stored at $start + 4+ 4 \times i $
* this address can be found in constant time , and value stores at address also at address also found in constant time  
* so search in linear 
* **Indirection** - accessing something by first accessing something else that contains a reference to thing sought

#### Binary search 

* can we do better than O(len(l)) for search?

* if know nothing about values of elements in list , then no 

* Worst case , would have to look at every element

* Suppose elements are sorted in ascending order 

* ```python
  def search(l,e):
      for i in range(len(L)):
          if L[i] == e:
              return True
          if L[i]>e:
              return False
      return False 
  ```

  Improves average complexity, but worst case still need look at every element

  * Use binary search

  * ```python
    def search(L,e):
        def bSearch(L,e,low,high):
            if high == low:
                return L[low] == e
            mid = low +int((high - low )/2)
            if L[mid]==e :
                return True
            if L[mid]>e:
                return bSearch(L,e,low, mid-1)
            else:
                return bSearch(L,e,mid+1,high)
        if len(L) ==0:
            return False
        else:
            return bSearch(L,e,0,len(e)-1)
    ```

#### Analyzing binary search

* Does the recursion halt?
  * decrementing function
    * maps values to which formal parameters are bound to non-negative integer
    * when value is <= 0 ,recursion terminates
    * for each recursive call, value of function is strictly less than value on entry to instance of function
  * here function is high- low 
    * at least 0 first time called (1)
    * when exactly 0, no recursive call ,return (2)
    *  otherwise , halt or recursively call with value halved
* So terminates
* What's complexity
  * how many recursive calls?
  * how many times can divide high - low in half before reaches 0?
  * $log_2(high - low)$
  * thus search complexity is O(log(len(L)))

#### Sorting algorithms

* what about cost of sorting?
* assume complexity of sorting a list is O(sort(L))
* then if we sort and search we want to know if $sort(L)+ log(len(L))<len(L)$
  * should we sort and search using binary, just use linear search

```python
#Selection Sort
def selSort(L):
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j<len(L):
            if minVal>L[j]:
                minIndx = j
                minVal = L[j]
            j +=1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
```

#### Analyzing collection sort 

* loop invariant
  * Given prefix of list L[0:i] and suffix L[i+1:len(L)-1],then prefix is sorted and no element in prefix is larger than smallest element in suffix 
  * base case : Prefix empty,suffix whole list- invariant true 
  * Induction step: move minimum element from suffix to end of prefix.Since invariant true before move, prefix sorted after append

#### Amortized cost analysis

#### Merge Sort

* Use a divide-and-conquer approach 
  * if list is of length 0 or 1 ,already sorted 
  * if list has more than one element, spilt into two lists, and sort each
  * merge results 
    * to merge , just look at first element of each, move smaller to end of result 
    * when one list empty, just copy rest of other list

#### Complexity of merge

* Comparison and copying are constant
* Number of comparison O(len(L))
* number of copying - O(len(L1))+O(len(L2))

```python
def merge(left,right,compare):
    result = []
    i,j = 0,0
    while i <len(left) and j < len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[i])
            j+=1
    while (i<len(left)):
        result.append(left[i])
        i+=1
    while (j<len(right)):
        result.append(right[j])
        j+=1
    return result
```

#### Putting in together

```python
import operater
def mergeSort(L,compare = operater.lt):
    if len(L)< 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle],compare)
        right = mergeSort(L[middle:],compare)
        return merge(left,right,compare)
```

Complexity of merge sort

* Merge is O(len(L))
* Mergesort is O(len(L))*number of calls to merge 
  * O(len(L))*number of calls to mergesort
  * O(len(L)*log(len(L)))
* Log linear - O(n log n ),where n is len(L)
* does come with cost in space,as makes new copy of list

#### Improving efficiency

* Combining binary search with merge sort very efficient
* can we do better?
* Dictionaries use concept of hashing 
  * lookup can be done in time almost independent of size of dictionary

####hashing

* convert key to an int
* use int to index into a list
* Conversion done using a hash function 
  * map large space of inputs to smaller space of inputs
  * thus a many-to-one mapping[^13]
  * when two inputs go to same output -a collision
  * a good hash function has a uniform distribution-minimizes probability of a collision

#### Complexity

* if no collisions,then O(1)
* if everything hashed to same bucket, then O(n)
* but in general. can trade off space to make hash table large, and with good function get close to uniform distribution, and reduce complexity to close to O(1)

[^13]: 映射

***

### Lecture 11: Classes

#### Objects

* each kind of data is an object
* object have:
  * a type(a particular object is said to be an instance of a type)
  * behavior really belongs to the type
  * an internal data representation
  * a set of procedures for interaction with the object
* example:[1,2,3,4]
  * type:list
  * internal data representation
    * int length L,an object array of size S>=L 
    * a linked list of individual cells
      * <data, pointer to next cell
  * procedures for manipulating lists
    * l[i,j,k]
    * len(),del l[i]
    * l.append(),l.extend(),l.count(),l.index(),l.insert(),l.pop(),l.reverse(),l.sort()

#### Object-Oriented programming

* everything is a object and has a type
* objects are a abstraction that encapsulate
  * internal representation
  * Interface for interacting with object
    * defines behaviors, hides implementation
    * attributes: data , methods
  * One can 
    * create new instances of objects 
    * destroy objects
      * explicitly using del or just "forget" about them
      * python system will reclaim destroyed or inaccessible objects

#### Advantage of OOP

* divide and conquer development
  * implement and test behavior of each class separately
  * increased modularity reduces complexity
* classes make it easier to code 
  * each class has a individual environment
  * inheritance allows subclasses to redefine or extend a selected subset of a superclass's behavior

#### Create an instance 

* Usually when creating an instance of a type ,we  will want to provide some initial values for the internal data.To do this , define an \_\_init\_\_ method

  * method is another name for a procedure attribute, or an procedure that belongs to this class

* ```python
  class Coordinate(object):
      def __init__(self,x,y):#作用于任何Coordinate实例的初始化方法,self指向实例，python自动将他传给任何方法，将它作为一个参数
          self.x = x
          self.y = y
          
  c = Coordinate(3,4)
  c.x
  ```

* when calling  a method of an object, python always passes the object as the first argument.By convention,we use self as the name of the first argument of methods

* The "." operator is used to access an attribute of an object. So the \_\_init\_\_ method above is defining two attributes for the new Coordinate object:x and y  

* when accessing an attribute of an instance, start by looking within the class definition,then move up to the definition of a superclass, then move to the global environment

![](TIM截图20180801212957.png)

####An environment view of classes

* class definition creates a binding of class name in global environment to a new frame or environment

* that frame contains any attribute bindings ,either variables or local procedures

* that frame also knows the parent environment from which it can inherit

* In this case, the only attribute is a binding of a name to a procedure 

* but if a class definition bound local variables as part of its definition,those would also be bound in this new environment 

* we can access parts of a class using Coordinate.\_\_init\_\_

* python interprets this by finding the binding for the first expression,and then using the standard rules to lookup the value for the next part of the expression in the frame

  ![](TIM截图20180801213708.png)

* suppose the class is invoked 

  * c = Coordinate(3,4)

* A new frame is created(instance)

* the init method is then called, with self bound to this object, plus any other arguments

* then instance knows about the frame in which init was called 

* Evaluating the body of init creates bindings in the frame of the instance 

* Given such bindings ,calls to attributes are easily found

* c.x will return 3 because c points to a frame ,and within that frame x is locally bound

* Note that c has access to any binding in the chain of environment

* c.\_\_init\_\_(5,6)

* will change the bindings for x and y within c

  ![](TIM截图20180801220330.png)

#### print representation of an object

* can define a \_\_str\_\_ method for a class, which python will call when it needs a string to print.This methods will be called with the object as the first argument and should return a str

```python
class Coordinate(obkect):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<"+self.x+self.y+">"
```

* use isinstance() to check if an object is a particular class

其他的内置方法？

#### add other methods

```python
def distance(self,other):
    return math.sqrt(sq(self.x-other.x)+sq(self.y-other.y))
```

#### example:a set of integers

```python
class intStr(object):
    def __init__(self):
        self.vals=[]
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    def __str__(self):
        self.bals.sort()
        return "{"+".".join([str(e) for e in self.vals])+"}"
    def member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueErro(str(e)+"not found")
a = intSet()
a.insert(3)
a.__str__
print(a)
```

### Lecture 12:Object Oriented Programming

#### Inheritance

```python
import datatime
class Person(object):
    def __init__(self,name):
        self.name = name
        self.birthday = None
        self.lastname = name.spilt(" ")[-1]
    def getLastName(self):
        return self.lastName
    def __str__(self):
        return self.name
    def getBirthday(self,month,day,year):
        self.birthday = datatime.data(year,month,day)
    def getAge(self):
        if self.birthday ==None:
            raise ValueError
        return (datatime.data.today()- self.birthday).days
    def __lt__(self,other):
        if self.lastName ==other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
```

#### How plist.sort() works

* python use the timsort algorithms for sorting sequences - a highly-optimized combination of merge and insertion sorts that has very good average case performance 

#### Using inheritance subclass to extend behavior

```python
class MITPerson(Person):
    nextIfNum = 0
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum +=1
        
    def getIdNum(self):
        return self.idNum
    def __lt__(self,other):
        return self.idNum<other.idNum
```

***

### Lecture 13:Trees

#### Tree definition

* a tree consist of one or more  nodes 
* Nodes are connected by branches
* A tree starts with a root node
* Except for leaves,each node has one or more children
* In simple tree, ==no child has more than one parent==, but the generalization(often called graph) is also very useful

#### Binary tree

* a binary tree is a special version of a tree, where each node has at most two children
* Binary trees are very useful when storing and searching ordered data, or when determining the best decision to make in solving many classes of problems (decision tree)

```python
class binaryTree(object):
    def __init__(self,value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
    def setLeftBranch(self,node):
        self.leftBranch = node
    def setRightBranch(self,node):
        self.rightBranch = node
    def setParent(self,parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getPrant(self):
        return self.parent
    def __str__(self):
        return self.value
    
n5 = binaryTree(5)
n2 = binaryTree(2)
n5.setLeftBranch(n2)
n2.setParent(n5)
```

#### search a tree

* depth first search
  * Start with the root
  * At any node,if we haven't reached our objective,take the left branch first
  * When get to a leaf,backtrack to the first decision point and take the right branch
* Breadth first search
  * start with the root
  * Then proceed to  each child at the next level,in order
  * Continue until reach objective

#### Depth first search for containment

* Idea is to keep a data structure (called a stack(盘子的堆叠，后进先出)) that holds nodes still to be explored
* Use an evaluation function to determine when reach objective
* Start with the root node 
* Then add children ,if any,to front of data structure ,with left branch first
* Continue in this manner

```python
def DFSBinary(root,fcn):
    stack = [root]
    while len(stack)>0:
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(o)
            if temp.getRightBranch():
                stack.insert(0,temp,getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
    return False
```



####Breadth first search

```python
#BFS,queue FIFO:先进先出
def DFSBinary(root,fcn):
    queue = [root]
    while len(queue)>0:
        if fcn(queue[0]):
            return TracePath(stack[0])
        else:
            temp = queue.pop(o)
            if temp.getRightBranch():
                queue.append(temp,getRightBranch())
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
    return False

def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node]+TracePath(node.getParent())
```

#### Ordered  Search

* suppose we know that the tree is ordered,meaning that for any node,all the nodes to the "left" are less than that node's value,and all the nodes to the "right" are greater than that node 's value 

```python
def DFSBinaryOrdered(root,fcn,ltFcn):
    stack = [root]
    while len(stack)>0:
        if fcn(stack[0]):
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(o)
            if temp.getRightBranch():
                stack.insert(0,temp,getRightBranch())
        else:
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
    return False
```

#### Decision Tree

* a decision tree is a special type of binary tree 
* at each node ,a decision is made , with a position decision taking the left branch,and a negative decision taking the right branch 
* when we reach a leaf that satisfies some goal,the path back to the root node defines the solution to the problem captured by the tree

#### Building a decision tree

* one way to approach decision trees is to construct an actual tree, then search it 
* an alternative is to implicitly build the tree as needed
* As an example, we will build a decision tree for a knapsack problem

#### Knapsack problem

* at the root level,we decide whether to include the first element or not 
* at the nth level,  we make the same decision for the nth element 
* by keeping track of what we have included so far,and what we have left to consider ,we can generate a binary tree of decisions

```python
def buildDTree(sofar,todo):
    if len(todo)==0:
        return binaryTree(sofar)
    else:
        withelt = buildDTree(sofar + [todo[0]],todo[1:])
        withoutit = buildDTree(sofar,todo[1:])
        here = binayTree(sofar)
        here.setLeftBranch(withelt)
        here.setRightBranch(withoutit)
        return here
```

#### Implicit search

* approach is inefficient,as it constructs the entire decision tree,and than searches it 
* An alternative is only generate the nodes of the tree as needed

```python
def DTImplicit(toConsider,avail):
    if toConsider ==[] and avail == 0:
        result = (0,())
    elif toConsider[0][1]> avail:
        result = DTImplicit(toConsider[1:],avail)
    else:
        nextItem = toConsider[0]
        withVal,withToTake = DTImplicit(toConsider[1:],avail-nextItem[1])
        withVal += nextItem[0]
        withoutVal,withoutToTake =  DTImplicit(toConsider[1:],avail)
        if withVal>withoutVal:
            result = (withVal,withToTake+(nextItem,))
        else:
            result = (withoutVal,withoutToTake)
    return result
```

***

## 6.00.2X 计算思维与数据科学导论

### Lecture 1：Plotting

#### plot

```python
import pylab as pl
pl.figure(1)
pl.plot([1,2,3,4],[1,7,3,5])
pl.show()
```

```python
import pylab as pl
pl.figure(1)
pl.plot([1,2,3,4],[1,7,3,5])
pl.figure(2)
pl.plot([1,2,3,4],[1,2,3,4])
pl.savefig("Figure-Eric")#默认.png
```

```python
import pylab as pl
principal = 10000
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal*interestRate
pl.plot(values,linewidth = 10)
pl.title("123")
pl.xlabel("123")
pl.ylabel("13")
pl.show()
```

```python
class Mortgage(object):
    def __init__(self,loan,annRate,months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months= months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None
    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1]-reduction)
    def getTotalPaid(self):
        return sum(self.paid)
    def __str__(self):
        return self.legend
```

```python
import pylab
#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles 
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortgage of size
    loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))
class MortgagePlots(object):
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)
        
class Mortgage(MortgagePlots, object):
    """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage
    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)
    def __str__(self):
        return self.legend

# fixed-rate mortgage
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'

# fixed-rate mortgage with up-front points
class FixedWithPts(Fixed):
    def __init__(self, loan, r, months, pts):
        Fixed.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend += ', ' + str(pts) + ' points'

# mortgage that changes interest rate after 48 months
class TwoRate(Mortgage):
    def __init__(self,loan,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100)
            + '% for ' + str(self.teaserMonths)
            + ' months, then ' + str(r*100) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate,
                                       self.months - 
                                       self.teaserMonths)
        Mortgage.makePayment(self)

class MortgagePlots(object):
    
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
        
    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)

def plotMortgages(morts, amt):
    styles = ['b-', 'r-.', 'g:']
    payments = 0 #number to identify a figure
    cost = 1 #number to identify a figure
    pylab.figure(payments)
    pylab.title('Monthly Payments of Different $' + str(amt)
                + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Monthly Payments')
    pylab.figure(cost)
    pylab.title('Cost of Different $' + str(amt) + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Total Payments')
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
    pylab.figure(payments)
    pylab.legend(loc = 'upper center')
    pylab.figure(cost)
    pylab.legend(loc = 'best')

def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                    varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths,
                      varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)

compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05, varRate1=0.045,
                 varRate2=0.095, varMonths=48)
pylab.show()
```



![](download.png)

![](download-1533475450899.png)

***

### Lecture 2:Simulations and Random Walks

#### Random walks

* simulation attempts to build an experimental device called a model
  * descriptive not prescriptive
    * Deterministic  vs. stochastic
      * deterministic simulations are completely defined by the model 
        * rerunning the simulation will not change the result
      * stochastic simulations include randomness 
        * different runs can generate different results
      * in a discrete model,value of variables are enumerable
      * in a continuous mode , they are not enumerable
    * static vs. dynamic
    * discrete vs. continues
* simulation physics sports finance 
* "All models are wrong, but some useful"

#### Brownian Motion

#### Drunken Walks

```python
class Location(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def move(self,deltaX,deltaY):
        return location(self.x+deltaX,self.y+deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self,other):
        ox =other.x
        oy = other.y
        xDist = self.x -ox
        yDist = self.y - oy
        return (xDist**2+yDist**2)**0.5
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
```

```python
class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError("Dupilcate drunk")
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self,drunk):
        if not drunk in self.drunks:
            raise ValueError("Drunk not in field")
        xDist,yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist,yDist)
        
    def getLoc(self,drunk):
        if not drunk in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]
```

```python
class Drunk(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "this frunl is named "+self.name
import random
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(1.0,0.0),(0.0,-1.0),(-1.0,0.0)]
        return random.choice(stepChoices)
```

#### Drunk tests

```python
def walk(f,d,numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))
def simWalks(numSteps,numTrials):
    homer = UsualDrunk("Homer")
    origin = Location(0,0)
    distance = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer,origin)
        distance.append(walk(f,homer,numTrials))
    return distance
def drunkTest(numTrials=20):
    #randome.seed(0)
    for numSteps in [10,100,1000,10000,10000]:
    #for numSteps in [0,1]:
        distance = simWalks(numSteps,numTrials)
        print("Random work of "+str(numSteps)+" steps")
        print("mean = ",sum(distance)/len(distance))
        print("max = ",max(distance),"min = ",min(distance))
```

```python
import pylab
def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
    pylab.plot(stepsTaken, meanDistances)
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.show()
```

```python
def drunkTestP1(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    meanDistances = []
    squareRootOfSteps = []
    for numSteps in stepsTaken:
        distances = simWalks(numSteps, numTrials)
        meanDistances.append(sum(distances)/len(distances))
        squareRootOfSteps.append(numSteps**0.5)
    pylab.plot(stepsTaken, meanDistances, 'b-',
               label = 'Mean distance')
    pylab.plot(stepsTaken, squareRootOfSteps, 'g-.',
               label = 'Square root of steps')
    pylab.title('Mean Distance from Origin')
    pylab.xlabel('Steps Taken')
    pylab.ylabel('Steps from Origin')
    pylab.legend()
    pylab.show()
```

```python
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.95), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        deltaX = random.random()
        if random.random() < 0.5:
            deltaX = -deltaX
        deltaY = random.random()
        if random.random() < 0.5:
            deltaY = -deltaY
        return (deltaX, deltaY)
```

```python
def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')#给各类传递同一参数
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances


def drunkTestP(numTrials = 50):
    stepsTaken = [10, 100, 1000, 10000]
    for dClass in (UsualDrunk, ColdDrunk, EDrunk):
        meanDistances = []
        for numSteps in stepsTaken:
            distances = simWalks(numSteps, numTrials, dClass)
            meanDistances.append(sum(distances)/len(distances))
        pylab.plot(stepsTaken, meanDistances,
                   label = dClass.__name__)
        pylab.title('Mean Distance from Origin')
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        pylab.legend(loc = 'upper left')
    pylab.show()
```

![](download (1).png)

### Lecture 3:Probability and Hashing

#### Rolling a Die

* Newtonian Mechanics
* The behavior of the physical world cannot be predicted
  * causal non-determinism[^20]: not every event is caused by previous events
  * Predictive non-determinism:the lack of knowledge about the world makes it impossible make accurate about future states

> The essentially statistical character of contemporary theory is solely to be ascribed to the fact that this theory operates with an incomplete description of physical system.
>
> 当代理论在本质上具有统计特性，只能归因于一个事实——这种理论对物质世界的描述是不完整的
>
> 											--Einstein
>
> It's pretty dangerous to treat them as predictably deterministic

#### Stochastic Processes

* an ongoing process where the next state might depend on both the previous states and **some random elements** 

```python
def rollDie():
    "return an int between 1 and 6"
    return random.choice([1,2,3,4,5,6])
def rollN(n):
    result =""
    for i in range(n):
        result = result +str(rollDie())
    return result
def getTarget(goal):
    numTries = 0
    numRolls = len(goal)
    while True:
        numTries +=1
        result = rollN(numRolls)
        if result ==goal:
            return numTries
def runSim(goal,numTrials):
    total = 0
    for i in range(numTrials):
        total +=genTarget(goal)
    aveNumTries =total/float(numTrials)
    print("probability = ",1.0/aveNumTries)
```

* 今天不是某人生日的概率
  * 假设：均匀分布uniformly distribution
  * $1-(364/365)^{100}\approx 0.24$

#### Introduction to hashing

```python
def strToInt(s):
    number = ""
    for c in s:
        number = number +str(ord(c))
    index = int(number)
    return index
def hashStr(s,tableSize = 101):
    number =""
    for c in s :
        number = number +str(ord(c))
    index = int(number)%tableSize#牛逼
    return index
```

* collisions
  * many to one mappings 
  * hash bucket
  * time-space trade off

#### Using hashing to look up information

```python
import random


class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}' #res[:-1] removes the last comma


D = intDict(29)
for i in range(20):
    #choose a random int in range(10**5)
    key = random.choice(range(10**5))
    D.addEntry(key, i)

print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket

```

* what is the algorithms complexity of hashing 
  * hash function is uniform
  * k bucket and n insertions ,average is n/k
* hash tables are really useful 
* hash function to provide a uniform distribution
* hash table is an example of date structure to trade time for space

[^20]: 因果不确定性

***

### Lecture 4:Stochastic Programming and Statistical Thinking

#### the laws of large numbers(bernoulli's law) 

* In repeated independent tests with the same actual probability p of a particular outcome in each test, the chance that the fraction of times that outcome occurs differs from p converges to zero as the number of trails goes to infinity
*  Gambler's fallacy
  * If deviations from expected behavior occur,these deviations are likely to be evened out by opposite deviations in the future
  * converge/linear scaling
  * it's never possible to be assured of perfect accuracy through sampling, unless you sample the entire population

```python
def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
       Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios)

def flipPlot(minExp, maxExp):
    """Assumes minExp and maxExp positive integers; minExp < maxExp
       Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios)
    #Additional code to produce different plots from the
    #same data
    pylab.figure()
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios, 'bo')
    pylab.semilogx()
    
random.seed(0)
flipPlot(4, 20)
pylab.show()

```

#### How much is enough?

* how many samples do we need to look at in order to have a justified confidence that something that is true about the population of samples is also true about the population from which the samples were drawn?
* ==Depends upon the variance in the underlying distribution== 
* Variance 
  * we measure the amount of variance in the outcomes of multiple trails 
* Standard Deviation
  * $\sigma(x) = \sqrt{\frac{1}{|x|}\sum\limits_{x=1}^{n}(x-\mu)}$

```python
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
def runTrial(numFlips):
    numHeads = 0
    for n in range(numFlips):
        if random.random() < 0.5:
            numHeads += 1
    numTails = numFlips - numHeads
    return numHeads, numTails
def flipPlot(minExp, maxExp, numTrials):
    meanRatios = []
    meanDiffs = []
    ratiosSDs =  []
    diffsSDs =  []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    pylab.plot(xAxis, meanRatios, 'bo')
    pylab.title('Mean Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.figure()
    pylab.plot(xAxis, ratiosSDs, 'bo')
    pylab.title('SD Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
def flipPlot2(minExp, maxExp, numTrials):
    meanRatios = []
    meanDiffs = []
    ratiosSDs =  []
    diffsSDs =  []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    pylab.plot(xAxis, meanRatios, 'bo')
    pylab.title('Mean Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean Heads/Tails')
    pylab.semilogx()
    pylab.figure()
    pylab.plot(xAxis, ratiosSDs, 'bo')
    pylab.title('SD Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()
    #Additional code to look at difference in abolute
    #number of heads and tails
    pylab.figure()
    pylab.title('Mean abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Mean abs(#Heads - #Tails')
    pylab.plot(xAxis, meanDiffs, 'bo')
    pylab.semilogx()
    pylab.semilogy()
    pylab.figure()
    pylab.plot(xAxis, diffsSDs, 'bo')
    pylab.title('SD abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Standard Deviation')
    pylab.semilogx()
    pylab.semilogy()

```

#### Standard deviation and histograms

```python
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1.0
    return heads/numFlips
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    sd = stdDev(fracHeads)
    return (fracHeads, mean, sd)
def labelPlot(numFlips, numTrials, mean, sd):
    pylab.title(str(numTrials) + ' trials of '
                + str(numFlips) + ' flips each')
    pylab.xlabel('Fraction of Heads')
    pylab.ylabel('Number of Trials')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))

def makePlots(numFlips1, numFlips2, numTrials):
    val1, mean1, sd1 = flipSim(numFlips1, numTrials)
    pylab.hist(val1, bins = 21)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    labelPlot(numFlips1, numTrials, mean1, sd1)
    pylab.figure()
    val2, mean2, sd2 = flipSim(numFlips2, numTrials)
    pylab.hist(val2, bins = 21)
    pylab.xlim(xmin, xmax)
    ymin, ymax = pylab.ylim()
    labelPlot(numFlips2, numTrials, mean2, sd2)
```

***

### Lecture 5:Monte Carlo Simulations

#### Monte Carlo Methods

```python
def rollDie():
    return random.choice([1,2,3,4,5,6])
def checkPascal(numTrials, roll):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = roll()
            d2 = roll()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing =', 1.0 - yes/numTrials
##checkPascal(10000, rollDie)
def rollLoadedDie():
    if random.random() < 1.0/5.5:
        return 6
    else:
        return random.choice([1,2,3,4,5])

##checkPascal(10000, rollLoadedDie)
def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)

for i in range(5): #number of trials
    print flip(10)
```

#### The history of estimate Pi

* Egyptian Rhine's Rhind Papyrus BC1650 $4\times(\frac{8}{9})^2\approx3.16$
* Old Testament BC
*  Archimedes of Syracuse 96sides BC250$\frac{221}{71}\leq\pi\leq\frac{22}{7}$
* Buffon and Laplace

```python
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print 'Est. = ' + str(curEst) +\
          ', Std. dev. = ' + str(round(sDev, 6))\
          + ', Needles = ' + str(numNeedles)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst

random.seed(0)
estPi(0.005, 100)
```

***

### Lecture 6:Using Randomness to Solve Non-Random Problems 

#### Normal distribution

* in honor of the astronomer Carl Friedrich Gauss
  * they have nice mathematical properties
  *  actually occur quite frequently in practice

```python
def makeNormal(mean, sd, numSamples):
    samples = []
    for i in range(numSamples):
        samples.append(random.gauss(mean, sd))
    pylab.hist(samples, bins = 101)

makeNormal(0, 1.0, 100000)
pylab.show()
```

#### Confidence Levels and Intervals 

#### Exponential Distribution

* inter-arrival times
* the only continuous distribution and has memoryless property

```python
def clear(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))
    pylab.plot(numRemaining, label = 'Exponential Decay')

##clear(1000, 0.01, 500)
##pylab.xlabel('Number of Steps')
##pylab.ylabel('Number of Molecules')
pylab.semilogy()
##pylab.show()
def clearSim(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb: 
                numLeft -= 1
        numRemaining.append(numLeft)
    pylab.plot(numRemaining, 'ro', label = 'Simulation')

clear(10000, 0.01, 1000)
clearSim(10000, 0.01, 1000)
pylab.xlabel('Number of Steps')
pylab.ylabel('Number of Molecules')
pylab.legend()
pylab.show()
```

#### The monty hall problem

>  the monty's choice is not independent of the choice made by the player 

```python
import pylab
import random

def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])
    
def simMontyHall(numTrials, chooseFcn):
    stickWins, switchWins, noWin = (0, 0, 0)
    prizeDoorChoices = [1,2,3]
    guessChoices = [1,2,3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)

def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(100000, montyChoose)
displayMHSim(simResults, 'Monty Chooses a Door')
pylab.figure()
simResults = simMontyHall(100000, randomChoose)
displayMHSim(simResults, 'Door Chosen at Random')
pylab.show()
```

***

***

### Lecture 10 : More on Graphs

#### Exploring Graphs

* Have seen examples of finding paths through graphs that represent physical networks
* use graph search to explore changes to state of a physical system
  * nodes represent states of system
  * edges represent actions that cause a change of state
  * want to find sequence of actions to convert system to desired state

#### Slides 

* each state in graph is a state of the puzzle 
  * specific layout of tiles in puzzle 
* each edge of the graph specifies which tile to slide to get to a new state of the puzzle 

#### an implicit graph

* suppose we represent each node in graph as a state of the puzzle 
  * specific layout of tiles 
  * rather than generate nodes, only generate as needed to explore paths 
  * edges then become implicit - create to generate new node 

#### A node and edge

* convert sequence of tiles into a string of labels 
* need to encode legal shift
* could keep track of these 



```python
class puzzle(object):
    def __init__(self, order):
        self.label = order
        for index in range(9):
            if order[index] == '0':
                self.spot = index
                return None
    def transition(self, to):
        label = self.label
        blankLocation = self.spot
        newBlankLabel = str(label[to])
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0'
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    def __str__(self):
        return self.label



def DFSWithGeneratorShortest(start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    if start.label == end.label:
        return path
    for shift in shiftDict[start.spot]:
        new = start.transition(shift)
        if new.label not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSWithGeneratorShortest(new,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFSWithGenerator(start, end, q = []):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath):
                newPath = tmpPath + [new]
                q.append(newPath)
    return None

def DFSWithGenerator(start, end, stack = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    initPath = [start]
    stack.insert(0, initPath)
    while len(stack)!= 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath): #avoid cycles
                newPath = tmpPath + [new]
                stack.insert(0, newPath)
    return None


def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True


shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

goal = puzzle('012345678')
test1 = puzzle('125638047')


def printGrid(pzl):
    data = pzl.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print ''

def printSolution(path):
    for elt in path:
        printGrid(elt)

path = BFSWithGenerator(test1, goal)
print printSolution(path)
```

#### Maximal Cliques

* find all subgraphs of a graphs 
* test each one to see if complete
* keep track of the largest

```python
class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)





def powerGraph(gr):
    nodes = gr.nodes
    nodesList = []
    for elt in nodes:
        nodesList.append(elt)
    pSet = powerSet(nodesList)
    return pSet

def powerSet(elts):
    if len(elts) == 0:
        return [[]]
    else:
        smaller = powerSet(elts[1:])
        elt = [elts[0]]
        withElt = []
        for s in smaller:
            withElt.append(s + elt)
        allofthem = smaller + withElt
        return allofthem

def maxClique(gr):
    candidates = powerGraph(gr)
    keepEm = []
    for candidate in candidates:
        if allConnected(gr, candidate):
            keepEm.append(candidate)
    bestLength = 0
    bestSoln = None
    for test in keepEm:
        if len(test) > bestLength:
            bestLength = len(test)
            bestSoln = test
    return bestSoln

def allConnected(gr,candidate):
    for n in candidate:
        for m in candidate:
            if not n == m:
                if n not in gr.childrenOf(m):
                    return False
    return True


def testGraph():
    nodes = []
    for name in range(5):
        nodes.append(Node(str(name)))
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[0]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[4],nodes[3]))
    return g


trialGraph = testGraph()
myClique = maxClique(trialGraph)

```

***

### Lecture 11:Machine learning

#### machine learning

* automating automation

* Ml focus on getting computers to  to program themselves

* generalization

  * deduce new facts from old one
  *  Major component


####Major component

* method for representing the data 
* metric for assessing goodness of the model 
* optimization method for learning the model

#### two broad classes 

* Supervised
* unsupervised

#### Clustering

* find an intrinsic grouping in set of unlabeled examples 

#### Hierarchical clustering

* clustering is an optimization problem 

* an objective function and a constraint 

* usually rely on a greedy approximation

  * Hierarchical clustering
