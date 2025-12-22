# Basic Data Types

In python, every value has a data type, which tells Python how it can be used.

Basic Data Types:
* **String** - a piece of text ("Hello", "apple", ...)
* **Int** - an integer number (-10, -2, 0, 1, 7, 500, ...)
* **Float** - a real number (-10.5, 4.0, 3.3333, 20.16, ...)
* **Bool** - a boolean value (True, False)

<p align="center">
    <image src="images/DataTypeMeme.jpeg" width="300px" />
</p>

It’s important to understand what you can and cannot do with each data type. For example, adding a number to a boolean value usually doesn’t make sense and can lead to errors.

To check the type of a value, you can use the ```type()``` function.

```py
type(5)
```

Obviously this on its own won't show you anything, you can pair it with the ```print()``` function.

```py
print(type(5)) # Output: <class 'int'>
```

You can also use variables with this function:

```py
number = 5

print(type(number)) # Output: <class 'int'>
```

Or even store the output of the ```type()``` function itself in a variable:

```py
number = type(5)

print(number) # Output: <class 'int'>
```

## Casters

Casting is the proccess of converting a value from one data type to another.

There is a set of Python functions that allows you to do that:
* ```int()``` - turns the value to an integer
* ```float()```  - turns the value to a float
* ```str()```  - turns the value to a string
* ```bool()``` - turns the value to a boolean

## Strings

You can do a few things with strings.

You can concatenate them:

```py
print("Hello " + "world!") # Output: Hello world!
```

But what if you want to concatenate a string with a number?

```py
print("Number " + 5) # This will throw an error
```

You can either wrap your integer in quotes and it will turn into a string:

```py
print("Number " + "5") # Output: Number 5
```

Or you can cast your integer into a string:

```py
print("Number " + str(5)) # Output: Number 5
```

It will also work with variables:

```py
my_text = "Number "
my_number = 5

print(my_text + str(my_number)) # Output: Number 5
```

What if it is the other way around:

```py
number_1 = "5"
number_2 = "10"

print(number_1 + number_2) # Output: 510
```

You can just cast them to integers:

```py
number_1 = "5"
number_2 = "10"

print(int(number_1) + int(number_2)) # Output: 15
```

Or even floats:


```py
number_1 = "5"
number_2 = "10"

print(float(number_1) + float(number_2)) # Output: 15.0
```

Something useful you can also do is multiply a string with an integer n:

```py
print("a"*10) # Output: aaaaaaaaaa
```

It will just repeat the string n times.

## Int and Float

Ints and floats are different data types, but when python is doing calculations with them, it just converts them to the correct data type.

Take this example:

```py
print(5/2) # Output: 2.5
```

Despite using two integers, Python knows the output needs to be a float so it allows it and converts it automatically.

Another example:

```py
print(5 + 2.0) # Output: 7.0
```

We are doing the sum of an integer and a float, but Python just converts the integer to float, this is what is called **implicit type conversion**.

<p align="center">
    <image src="images/VariableIsVariable.jpeg" width="300px" />
</p>

Next topic: [ArithmeticOperators](ArithmeticOperators.md)