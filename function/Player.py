class Player:
    def __init__(self):
        self.name = ""
        self.money = 15
        self.hp = 50
        self.maxhp = 50
        self.upgrade = None

    def set_player_name(self):
        retry = None
        while True:
            if retry:
                name = input("> ")
            else:
                name = input("Hero, I want to know you better. What is your name ?\n> ")
            if name == "":
                print("Please use a real name sir.")
                retry = True
                continue
            self.name = name
            print("Well, that's a pretty bad name there. But anyway, welcome {}.".format(name))
            break
        return True

    def set_player_upgrade(self, upgrade):
        self.upgrade = upgrade
        return True

    def heal(self, heal):
        if self.hp + heal > self.maxhp:
            heal = self.maxhp - self.hp
            self.hp = self.maxhp
        else:
            self.hp += heal
        print("You got healed for {} HP. You are now at {} HP.".format(heal, self.hp))
        return True

    def damage(self, damage, ia):
        from function.GameSystem import game_over
        if self.hp - damage <= 0:
            self.hp = 0
            print("You took {} damage from {}.".format(damage, ia.name))
            game_over()
        else:
            self.hp -= damage
            print("You took {} damage from {}. You are now at {} HP.".format(damage, ia.name, self.hp))
        return True
