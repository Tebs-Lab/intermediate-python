import os
from monsters import Fiend, Bear
from heroes import BasicHero, Wizard

def main():
    os.system('clear')
    hero = Wizard() 
    while hero.is_alive():
        current_enemy = Bear(hero.level) 
        while hero.is_alive() and current_enemy.is_alive():
            print('\n  ====BATTLE STATUS====\n')
            print(hero)
            print(current_enemy)
            print('\n  ====ROUND ACTIONS====\n')

            print("The hero attacks!")
            hero.attack(current_enemy)
            
            if current_enemy.is_alive():
                print("The monster attacks!")
                current_enemy.attack(hero)
            else: 
                print("The monster was defeated!")
                hero.defeat_enemy(current_enemy)

            print('\n  ====ROUND OVER====\n')
            s = input("Press enter to continue to the next round. Or 'exit' to end the game.\n")
            if s == 'exit': 
                exit(0)
            os.system('clear')

    print("The hero died.") 


if __name__ == '__main__':
    main()