from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def attack(self, enemy):
        pass

    @abstractmethod
    def recieve_damage(self, damage_amount):
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


class BasicHero(Hero):
    def __init__(self):
        self.max_hp = 40
        self.current_hp = self.max_hp
        self.attack_power = 5
        self.resistance = 1
        self.experience = 0
        self.level = 1


    def attack(self, enemy):
        enemy.recieve_damage(self.attack_power)


    def recieve_damage(self, damage_amount):
        damage_amount -= self.resistance
        self.current_hp -= damage_amount


    def defeat_enemy(self, enemy):
        self.experience += enemy.experience_reward

        if self.experience >= (self.level * 20):
            self.level_up()


    def is_alive(self):
        return self.current_hp > 0


    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.current_hp = self.max_hp
        self.attack_power += 2
        self.resistance += 1


    def __str__(self):
        return(f"Level {self.level} Hero: {self.current_hp} / {self.max_hp}\n  attack: {self.attack_power}\n  resistance: {self.resistance}\n  experience: {self.experience}")
    


class Wizard(Hero):
    def __init__(self):
        self.max_hp = 20
        self.current_hp = self.max_hp
        self.max_mana = 40
        self.current_mana = self.max_mana
        self.spell_power = 20
        self.spell_cost = 5
        self.attack_power = 5
        self.resistance = 0
        self.experience = 0
        self.level = 1


    def attack(self, enemy):
        if self.current_mana >= self.spell_cost:
            self.current_mana -= self.spell_cost
            enemy.recieve_damage(self.spell_power)
        else:
            enemy.recieve_damage(self.attack_power)


    def recieve_damage(self, damage_amount):
        damage_amount -= self.resistance
        self.current_hp -= damage_amount


    def defeat_enemy(self, enemy):
        self.experience += enemy.experience_reward

        if self.experience >= (self.level * 20):
            self.level_up()


    def is_alive(self):
        return self.current_hp > 0


    def level_up(self):
        self.level += 1
        self.max_hp += 5
        self.current_hp = self.max_hp
        self.max_mana += 10
        self.current_mana = self.max_mana
        self.spell_power += 8
        self.attack_power += 2
        # Only gain resistance on even numbered levels
        if self.level % 2 == 0:
            self.resistance += 1


    def __str__(self):
        return(f"Level {self.level} Wizard: {self.current_hp} / {self.max_hp}\n  mana: {self.current_mana} / {self.max_mana}\n  spell power: {self.spell_power}\n  attack: {self.attack_power}\n  resistance: {self.resistance}\n  experience: {self.experience}")