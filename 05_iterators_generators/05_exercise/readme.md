# Practice With Iterators and Generators

This exercise is a collection of short tasks to be achieved using the content from this lesson. You may wish to make a new file for each section to keep the code manageable.

## Part 1: Generators

* Write a generator that yields the first N square numbers
    * A square number is one formed by multiplying an integer by itself
    * So 1, 4, and 9 are the first 3 square numbers because `1*1=1, 2*2=4, 3*3=9`

* Write a generator that accepts any iterable as input and iterates through the list `n` times, where `n` is also an input parameter to the generator.
    * So `multiple_iter([1, 2, 3], 3)` would yield `1,2,3,1,2,3,1,2,3` then stop. 
    * Tip: This is easy to write in a way that works with just lists, but kinda tricky for arbitrary iterators.
    * Tip: You may not be able to keep the "low memory" advantages of iterators.

## Part 2: Iterators

* For both the generators in part one, write iterator classes that perform identically.

## Part 3: Comprehensions

The following code creates a short list of words...

```python
words = [
    'apple',
    'soda',
    'car',
    'intrepid',
    'water',
    'buffalo',
    'tepid',
    'enemy',
    'salvo'
]
```

* Use a list comprehension to generate a list that has the same words, but in all capital letters.
* Use a list comprehension to generate a list that only has the words which start with a vowel.
* Use a dictionary comprehension to map the words (as keys) to the length of the word (as values)

## Part 4: Iteration Tools in Action

* Write a function that returns True if a `list` is in sorted order, False otherwise
    * Hint: `enumerate` is useful.

* Write a function that computes item-wise vector addition.
    * It should accept two lists of numbers and check they have the same length
    * It should return a new list, also of that same length
    * Each item in the new list should be the sum of two numbers from at the same index position from the input vectors 
    * For example: `vec_add([1,2,3], [7,8,9])` -> `[8,10,12]`