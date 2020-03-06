#  File: RPG.py

class Weapon():
    """A selection of RPG weapons"""

    def __init__(self, type, damage):
        self.type = type
        self.damage = damage

#weapons
dagger = Weapon('dagger', 4)
axe = Weapon('axe', 6)
staff = Weapon('staff', 6)
sword = Weapon('sword', 10)
none = Weapon('none', 1)


class Armor():
    """A selection of RPG armor"""
    def __init__(self, type, AC):
        self.type = type
        self.AC = AC

#armor
plate = Armor('plate', 2)
chain = Armor('chain', 5)
leather = Armor('leather', 8)
naked = Armor('none', 10)


class RPGCharacter():
    """A selection of RPG subclasses"""

    def __init__(self, name):
        self.name = name
        self.armor = naked
        self.weapon = none
        self.health = self.max_health
        self.magic = self.max_magic

    def wield(self, weapontype):
        self.weapontype = self.weapon
        if self.weapontype in allowed_weapon:
            self.weapon = self.weapontype
            print(self.name + ' is now wielding ' + weapontype + '.')
        elif:
            print('Weapon not allowed for this character class.')

    def unwield(self):
        self.weapon = none
        print(self.name + ' is no longer wielding anything.')

    def put_on_armor(self, selected_armor):
        if selected_armor in self.allowed_armor:
            self.armor = selected_armor
            print(self.name + ' is now wearing ' + self.armor + ' armor.')
        elif:
            print('Armor not allowed for this character class.')

    def take_off_armor(self):
        self.armor = naked
        print(self.name + ' is no longer wear any armor.')


    def select_weapon(self):


    # def character_health(self):
    #     if self.health <= 0:
    #         print('You died.')
    #     elif self.health > max_health:
    #         print("You're at max health!")
    #         self.health = max_health



class Fighter(RPGCharacter):
    """A subclass of RPG character"""

    def __init__(self):
        """Initialize attributes of the parent class."""
        super().__init__(name, health, magic)
        self.allowed_weapons = [dagger, axe, sword, none]
        self.allowed_armor = [plate, chain, leather, naked]
        self.max_health = 40
        self.max_magic = 0



class Wizard(RPGCharacter):
    """A subclass of RPG character"""

    def __init__(self, name, health=16, magic=20):
        """Initialize attributes of the parent class."""
        super().__init__(name, health, magic)
        self.allowed_weapons = [staff, none]
        self.allowed_armor = [chain, leather, naked]
        self.max_health = 16
        self.max_magic = 20






my_wizard = Wizard('Murphus')

print(my_wizard.name)