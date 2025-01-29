# In the code for our old Dungeonmon game, some of the classes
# have explicit interactions. These cannot be tested with unit
# tests, because they rely on the interactions between the classes.
# So we'll write integration tests for them. 

# NOTE: we __should__ also write unit tests for these classes, but in this
# file we are only writing integration tests.

# NOTE 2: We're using the pytest framework for these tests. Pytest allows us
# to write less boilerplate (e.g. we can write functions without subclassing TestCase)
# and it also makes the console output more beautiful and legible. 

from heroes import BasicHero
from monsters import Fiend
import pytest

def test_gain_experience():
    hero = BasicHero()
    fiend = Fiend(1)
    before = hero.experience
    hero.defeat_enemy(fiend)
    assert hero.experience == before + fiend.experience_reward

def test_level_up_trigger():
    hero = BasicHero()
    fiend = Fiend(1)

    # Candidly, this line of code demonstrates a problem with the current
    # implementation of hero. The level up condition just if the experience
    # is greater than the level * 20, but that's not codified in any instance variable
    # helper function, or anything like that. It's just a magic number.
    # We probably SHOULD refactor this. But it's also a source of brittleness
    # that makes a test suite like this relevant and useful.
    hero.experience = (hero.level * 20) - 1 
    before = hero.level
    hero.defeat_enemy(fiend)
    
    assert hero.level == before + 1

    # NOTE: A unit test that ensures the logic of level_up is correct would be a good idea.
    # But it's NOT an integration test, so it doesn't belong in this test case

# Mini-exercise: Write an integration test that ensures that the hero's
# HP is reduced by the correct amount when they are attacked by a monster.



if __name__ == '__main__':
    pytest.main()

### ADDITIONALLY: you can run these tests from the command line by running the
# following from the folder containing this file:
'pytest'
# or
'pytest test_hero_monster_integration.py'

