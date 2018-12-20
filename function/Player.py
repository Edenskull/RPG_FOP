PLAYER = []


class Player:
    def __init__(self, name, classe, race):
        self.name = name
        self.classe = classe
        self.race = race
        self.money = 1500
        self.hp = 50
        self.lvl = 1
        self.exp = 0
        self.inventory = []
        self.weapon = None

    def mod_money(self, amount):
        self.money = self.money + amount

    def damage(self, amount):
        self.hp = self.hp - amount

    def heal(self, amount):
        self.hp = self.hp + amount

    def experience(self, amount):
        print("{} gagne {} xp.".format(self.name, amount))
        next_amount = self.exp + amount
        if next_amount > self.lvl ** 2 + 1000:
            print("{} passe au niveau suivant")
            next_amount = next_amount - ((self.lvl ** 2) + 1000)
            self.level_up()
        self.exp = next_amount

    def level_up(self):
        self.lvl += 1
        print("{} passe au niveau suivant : niveau {}".format(self.name, self.lvl))

    def change_weapon(self, weapon):
        self.add_inventory(self.weapon)
        self.del_inventory(weapon)
        self.weapon = weapon
        print("L\'arme a bien été changée")

    def add_inventory(self, thing):
        self.inventory.append(thing)

    def del_inventory(self, thing):
        self.inventory.remove(thing)

    def get_name(self):
        return self.name

    def get_classe(self):
        return self.classe

    def get_race(self):
        return self.race

    def get_money(self):
        return self.money

    def get_hp(self):
        return self.hp

    def get_lvl(self):
        return self.lvl

    def get_exp(self):
        return self.exp

    def get_inventory(self):
        return self.inventory

    def get_weapon(self):
        return self.weapon

    def to_string(self):
        print("Name : {}\nClasse : {}\nRace : {}\nHP : {}\nMoney : {}\nLvl : {}\nExp : {}".format(self.name, self.classe, self.race, self.hp, self.money, self.lvl, self.exp))


def create_player(name, classe, race):
    player = Player(name, classe, race)
    PLAYER.append(player)


def display_all():
    for i in PLAYER:
        print(i.to_string())
