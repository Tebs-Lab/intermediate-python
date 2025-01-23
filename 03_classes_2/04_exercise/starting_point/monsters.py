from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def __init__(self, level):
        pass

    
    @abstractmethod
    def attack(self, hero):
        pass


    @abstractmethod
    def recieve_damage(self, damage_amount):
        pass


    @abstractmethod
    def is_alive(self):
        pass


    @abstractmethod
    def experience_reward(self):
        pass

    @abstractmethod
    def __str__(self):
        pass



class Fiend(Monster):
    def __init__(self, level):
        self.level = level
        self.max_hp = 10 + (10 * self.level)
        self.current_hp = self.max_hp
        self.attack_power = 3 + (2 * self.level)
        self.resistance = 0 + (1 * self.level)
        self._experience_reward = 10


    def attack(self, hero):
        hero.recieve_damage(self.attack_power)


    def recieve_damage(self, damage_amount):
        damage_amount -= self.resistance
        self.current_hp -= damage_amount


    def is_alive(self):
        return self.current_hp > 0
    

    @property
    def experience_reward(self):
        return self._experience_reward


    def __str__(self):
        return(f"Level {self.level} Fiend: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}")


