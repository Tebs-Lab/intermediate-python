from interfaces import Monster, Hero

class BasicHero(Hero):
    """
    A basic implementation of a hero.
    """

    def __init__(self) -> None:
        """
        Initialize a BasicHero with default attributes.
        """
        self.max_hp = 40
        self.current_hp = self.max_hp
        self.attack_power = 5
        self.resistance = 1
        self.experience = 0
        self.level = 1

    def attack(self, enemy: Monster) -> None:
        """
        Attack an enemy hero.
        
        :param Monster enemy: The enemy hero to attack.
        """
        enemy.receive_damage(self.attack_power)

    def receive_damage(self, damage_amount: float) -> None:
        """
        Receive damage from an attack.
        
        :param float damage_amount: The amount of damage to receive.
        """
        damage_amount -= self.resistance
        self.current_hp -= damage_amount
    
    def defeat_enemy(self, enemy: Monster) -> None:
        """
        Defeat an enemy hero. This results in increased experience
        for the hero and possibly a level up.
        
        :param Monster enemy: The enemy hero to defeat.
        """
        self.experience += enemy.experience_reward

        if self.experience >= (self.level * 20):
            self.level_up()

    def is_alive(self) -> bool:
        """
        Check if the hero is still alive.
        
        :return: True if the hero is alive, False otherwise.
        """
        return self.current_hp > 0

    def level_up(self) -> None:
        """
        Level up the hero. This increases the hero's level, max HP,
        attack power, and resistance.
        """
        self.level += 1
        self.max_hp += 10
        self.current_hp = self.max_hp
        self.attack_power += 2
        self.resistance += 1

    def __str__(self) -> str:
        """
        Return a string representation of the hero.
        
        :return str: A string representation of the hero.
        """
        return(f"Level {self.level} Hero: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}\n  experience: {self.experience}")
    
