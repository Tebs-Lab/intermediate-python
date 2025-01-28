from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def receive_damage(self, damage_amount):
        pass
    
    @abstractmethod
    def defeat_enemy(self, enemy):
        pass

    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Monster(ABC):
    @abstractmethod
    def __init__(self, level):
        pass

    
    @abstractmethod
    def attack(self, hero):
        pass


    @abstractmethod
    def receive_damage(self, damage_amount):
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

