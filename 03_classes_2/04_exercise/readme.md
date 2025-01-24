# Exercise: Dungeonmons 2; Interfaces

Dungeonmons 2 is a very simple text-based roleplaying game designed to help you understand and practice the use of classes, objects, inheritance, and "interfaces."

One of the key features of using the inheritance pattern with abstract interfaces is the creation of "drop in" replacements. In this exercise you're being challenged to develop at least 2 such replacements, one that extends the abstract Hero class and another that extends the abstract Monster class. 

If you successfully implement these interfaces you will be able to play the game using your new hero and monster types. 

## The Tasks:

### 1: Create a New Hero

Write a class that implements the Hero interface. You may use the BasicHero as a guide or starting point. Things to consider:

* The interface defines all the methods that need to exist, but the selection of instance variables is up to you. 
    * As long as the hero instance has functions `attack`, `receive_damage`, `defeat_enemy`, `is_alive`, and `__str__` then the code in the game loop will run.
    * You could still create bugs and errors in implementing those functions, of course.
    * How you want these functions to behave, and how they modify the internal state of the hero is up to you.

* Only the `is_alive` method needs a return value, it should be a boolean. 

* Test your class by replacing the `BasicHero()` instantiation with a call to your class instead.
    * You'll need to add your class to the `from heros import BasicHero` statement as well. 

* Try to distinguish your new Hero from the BasicHero. Here are two common RPG "archetypes" for inspiration:
    * The Glass Cannon: does lots of damage, but dies easily. 
    * The Tank: Doesn't do a lot of damage, but has a lot of health or doesn't take as much damage.


### 2: Create a New Monster

Write a class that implements the Monster interface. You may use the Fiend as a guide or starting point.

* The interface defines all the methods that need to exist, but the selection of instance variables is up to you. 
    * As long as the monster instance has functions `attack`, `receive_damage`, `experience_reward`, `is_alive`, and `__str__` then the code in the game loop will run.
    * You could still create bugs and errors in implementing those functions, of course.
    * How you want these functions to behave, and how they modify the internal state of the hero is up to you.

* `is_alive` needs a return value, it should be a boolean. 

* `experience_reward` needs to return a value, it should be a number.

* Test your class by replacing the `Fiend()` instantiation with a call to your class instead.
    * You'll need to add your class to the `from monsters import Fiend` statement as well. 

* Similar to the Hero, try to distinguish your new monster from the Fiend.

### If You Finish Early... Bonus Points:

Make this game better. There are TONS of ways you might do this. Here are some ideas:

#### Add Some Randomness

Most games have an element of random behavior, like a dice roll or a shuffled deck of cards. Introduce mechanics based on the element of chance. Perhaps modifiers to do less or more damage, perhaps a "critical hit" mechanic, perhaps generate some of the stats randomly.

Python has very good built in support for lots of random behavior. See: [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)

#### Give the player some choices

Right now all the player can do is advance the round. That's not much of a game! Give the player some choices. You could add another type of attack and let the player pick. You could give the player options to heal, run, etc. 

#### Make the display prettier

Terminal displays support the use of color! Check out these two articles and try to implement colors to make the display easier to read, and more exciting!

* [https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/](https://saturncloud.io/blog/how-to-print-colored-text-to-the-terminal/)
* [https://chrisyeh96.github.io/2020/03/28/terminal-colors.html](https://chrisyeh96.github.io/2020/03/28/terminal-colors.html)

#### Make the player wait

This one is easy to implement, but really improves the games feel. The following code will pause python's execution for half a second, allowing messages to appear on the screen one by one rather than all at once.

```python
import time

time.sleep(0.5)
```

#### Do something else that sounds interesting to you

Be creative, this world is *your* world after all! 