from interfaces import Monster, Hero


class Fiend(Monster):
    """
    A fiend Monster.
    Attributes
    ----------
    level: int
        The level of the monster.
    max_hp: float
        The maximum hit points of the monster.
    current_hp: float
        The current hit points of the monster.
    attack_power: float
        The attack power of the monster.
    resistance: float
        The resistance of the monster, which reduces damage by this amount.
    _experience_reward: float
        The experience reward for defeating
    """

    def __init__(self, level: int) -> None:
        """
        Initialize a Fiend with the given level. Higher level fiends
        have higher attributes across the board.

        :param int level: The level of the fiend.
        """
        self.level = level
        self.max_hp = 10 + (10 * self.level)
        self.current_hp = self.max_hp
        self.attack_power = 3 + (2 * self.level)
        self.resistance = 0 + (1 * self.level)
        self._experience_reward = 10


    def attack(self, hero: Hero) -> None:
        """
        Attack a hero.
        
        :param hero: The hero to attack.
        """
        hero.receive_damage(self.attack_power)


    def receive_damage(self, damage_amount: float) -> None:
        """
        Receive damage from an attack.
        
        :param float damage_amount: The amount of damage to receive.
        """
        damage_amount -= self.resistance
        self.current_hp -= damage_amount


    def is_alive(self) -> bool:
        """
        Check if the monster is still alive.
        
        :return: True if the monster is alive, False otherwise.
        """
        return self.current_hp > 0
    

    @property
    def experience_reward(self):
        """
        Return the experience reward for defeating the monster.

        :return float: The experience reward for defeating the monster.
        """
        return self._experience_reward


    def __str__(self) -> str:
        """
        Return a string representation of the monster.
        
        :return: A string representation of the monster.
        """
        return(f"Level {self.level} Fiend: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}")

