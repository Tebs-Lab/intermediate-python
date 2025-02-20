# Exercise: Type Safety and Proper Documentation

In this exercise you'll practice using docstrings, type annotations, and your choice of 
`beartype` and `pydantic`. 

## Part 0: An important note

In order to avoid a circular import, which causes errors, but still allow proper type hinting, we have moved the two interfaces `Hero` and `Monster` to a new python file called `interfaces.py`. This way both `heroes.py` and `monsters.py` can reference the abstract classes in their type hints without creating a circular dependency that cannot be resolved.

## Part 1: Adding types and docs

For every class and function definition in the provided code, do the following:

1. Add type annotations.
2. Add runtime type validation with `beartype` or `pydantic`
3. Add a docstring that describes the class/method/function
4. For classes, ensure instance variables are also type-hinted and type-validated.

**Hint:** Since Python 3.5 docstrings are inherited. This means, where it makes sense, you can simply add a docstring to the interface, and leave it off of the subclass definitions. If your subclass makes a significant or important change to the interface behavior, you can also append to the docstring rather than rewrite it like this:

```python
class Wizard(Hero):
    __doc__ = Hero.__doc__ + " But this hero is a Wizard"

def attack(self):
    __doc__ = super().attack.__doc__ + "The wizard only fires a fireball if she has enough mana to do so"
```

## Part 2: Generate HTML Documentation

* Use the built in pydoc library to generate HTML pages for each of the classes.
* **bonus points**: Use Sphinx to do the same:
    * [Sphinx](https://www.sphinx-doc.org/en/master/)