"""
https://py.checkio.org/en/mission/the-warriors/
"""

class Warrior:
    def __init__(self):
        self.is_alive = True
        self.health = 50
        self.attack = 5
        
    def damage(self, newhealth):
        self.health = newhealth
        if self.health <= 0:
            self.is_alive = False 

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack += 2
        
def fight(war1, war2):
    while war1.health > 0 and war2.health > 0:
        health_war2 = war2.health - war1.attack
        war2.damage(health_war2)
        if not war2.is_alive: return True
        health_war1 = war1.health - war2.attack
        war1.damage(health_war1) 
        if not war1.is_alive: return False

if __name__ == '__main__':
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")