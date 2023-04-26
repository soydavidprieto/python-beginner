# So where is a magic?

Python provides built-in data structures (classes).
- Numeric (int, float) to store numbers
- Strings (str) to store text
- Collections (list, dict, set, tuple) to store sequences, key-value pairs

So why do we write programs? Usually because we have to process data.
- Store records
- Calculate totals
- Transfer data from one place to another

Even if we write games, it's still manipulations with data. 
Store score, increase it for one player and decrease it for another player.

So built-in types gives you an abstraction and functionality to achieve your needs.

Now, any business operate numbers, strings and collections. But usually on higher-level. 
Business people use more complex abstractions. 
For example Invoice (which under the hood stores some string like product names, some numbers like prices and totals).
Or Car Catalog which under the hood has 
- Car abstraction (class) to store fields needed to describe car
- Catalog abstraction (class) to store key value pairs of car names and car objects, or list of car objects

So those higher-level abstractions are not available out of the box because 
you can have millions of slightly different types. 
So Python gives you built-in primitives,
and a way to create custom classes on top of those primitives to handle your needs.

If your class is very similar to collection like list, or dict. 
You want to work with it's instances in at least similar way 
you work with and instances of list or dict (use for loops, access by key).

Use magic when you need to explain Python how to operate on your custom classes.
So other developers can work more natively with such classes.

Let's consider following example:
```python
if __name__ == '__main__':
    # So here, we are using built-in int type. 
    # Consider <int> as a class created by other developer.
    a = int('1')
    b = int('2')
    # <int> class provides certain level of abstraction to you
    # you don't care how it's works, but you expect to be able 
    # to sum 2 integers (instances of class int) using `+` sing.
    c = a + b
    print(c)  # 3

    # limitations here:
    d = int('1x')  # ValueError: invalid literal for int() with base 10: '1x'
```

Now let's assume you're asked to parse text file which contains millions of numbers and calculate total sum. 
Some of those numbers may have typos. Customer asks you to consider 
those numbers as `0` and print them to console right away when it happens (kind an alert or error log).
What are your options?

* Option 1. Straight forward, only built-in abstractions. This may lead to repetitive blocks of code.
```python
if __name__ == '__main__':
    total = int('0')
    sequence = [1, '2', 3, '1x']
    for value in sequence:
        try:
            value = int(value)
        except ValueError:
            print(f'invalid value: {value}')
            value = int('0')
        total = total + value
```

* Option 2. Abstraction `to_int`. You hide complexity of the logic under custom function which can be reused. 
  Nobody except you actually may not care about how it works, it's just does the job. 
  If you need to change it later on, you have to do it in one place of your program only.
```python
def to_int(value):
    try:
        value = int(value)
    except ValueError:
        print(f'invalid value: {value}')
        value = int('0')
    return value


if __name__ == '__main__':
    total = int('0')
    sequence = [1, '2', 3, '1x']
    for value in sequence:
        total = total + to_int(value)
```

* Option 3. Hide complexity under the class definition.
```python
class MyInt:
    def __init__(self, value):
        try:
            self.value = int(value)
        except ValueError:
            print(f'invalid value: {value}')
            self.value = int('0')


if __name__ == '__main__':
    total = int('0')
    sequence = [1, '2', 3, '1x']
    for value in sequence:
        value = MyInt(value)
        # print(value)  <__main__.MyInt object at 0x7f964a9c4fa0> and so on
        total = total + value.value

# But for other developers, int-like class should work similarly to built-in int class.
# They already know how to work with int, and now have to learn how to work with your custom class.
# Your code should be easy to use, easy to support, but not always easy to write.
# You have to think about others, so if you have something very similar to int, but not exactly int, 
# make it act like an int.
```

* Option 3.1 More native class.
```python
class MyInt:
    def __init__(self, value):
        try:
            self.value = int(value)
        except ValueError:
            print(f'invalid value: {value}')
            self.value = int('0')
    
    def __add__(self, other):
        """
        To support + sign for instances of class MyInt
        """
        if isinstance(other, MyInt):
            return MyInt(self.value + other.value)
        raise ValueError(f'Expected type: {MyInt.__class__.__name__}, but got: {type(other)}')
    
    def __str__(self):
        """
        To print nicely instances of class MyInt to console like usual numbers
        """
        return str(self.value)

if __name__ == '__main__':
    total = MyInt('0')
    sequence = [1, '2', 3, '1x']
    for value in sequence:
        value = MyInt(value)
        # print(value)  # 1 and so on
        total = total + value
```
In the last example we explained Python how exactly to sum 2 instances of custom class MyInt using 
magic method `__add__` in class definition. Limitations that we covered only `+` operation.
Also we explained how to print instances of class MyInt to console nicely using `__str__` magic method.
There are other magic methods which will tell Python how to operate with your custom classes if needed.
