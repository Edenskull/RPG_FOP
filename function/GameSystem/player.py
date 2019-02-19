class Player:
    def __init__(self, name):
        self.name = name
        self.pvmax = 50
        self.pv = self.pvmax
        self.pa = 1
        self.pd = 1
        self.pc = 1
        self.concentration = 0
        self.argent = 50
        self.combat_count = 0

    def heal(self, heal):
        if self.pv + heal > self.pvmax:
            heal = self.pvmax - self.pv
            self.pv = self.pvmax
        else:
            self.pv += heal
        print("{} a été soigné de {} pv".format(self.name, heal))
        print("Il est maintenant à {} pv".format(self.pv))
        return

    def damage(self, damage):
        if self.pv - damage <= 0:
            self.pv = 0
            # TODO trigger gameOver
        else:
            self.pv -= damage
        print("{} à subit {} dégats".format(self.name, damage))
        print("Il est maintenant à {} pv".format(self.pv))
        return

    def apply_upgrade(self, upgrade):
        self.__setattr__(upgrade['mod'], self.pa + upgrade['value'])
        print("{} Augmente ses {} de {} et est maintenant à {} {}".format(
            self.name,
            upgrade['desc'],
            upgrade['value'],
            self.__getattribute__(upgrade['mod']),
            upgrade['desc']
        ))
        return

    def win_count(self):
        self.combat_count += 1
        return


def create_player():
    name = input("Donne moi ton nom : ")
    return Player(name)
