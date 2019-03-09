class Player:
    # Constructor Player
    def __init__(self, name):
        self.name = name
        self.pvmax = 50
        self.pv = self.pvmax
        self.mpmax = 50
        self.mp = self.mpmax
        self.atk = 1
        self.matk = 1
        self.win = 0
        self.money = 100
        return

    # Apply upgrade module
    def apply_upgrade(self, upgrade):
        if upgrade['mod'] not in ['pv', 'mp']:
            actual_stat = self.__getattribute__(upgrade['mod'])
            self.__setattr__(upgrade['mod'], actual_stat + upgrade['value'])
            print("{} Augmente ses {} de {} et est maintenant à {} {}".format(
                self.name,
                upgrade['desc'],
                upgrade['value'],
                self.__getattribute__(upgrade['mod']),
                upgrade['mod']
            ))
        else:
            actual_stat = self.__getattribute__(upgrade['mod'])
            actual_stat_max = self.__getattribute__(upgrade['mod'] + 'max')
            if actual_stat + upgrade['value'] > actual_stat_max:
                amount = actual_stat_max - actual_stat
                self.__setattr__(upgrade['mod'], actual_stat_max)
            else:
                amount = upgrade['value']
                self.__setattr__(upgrade['mod'], amount)
            print("{} use an instant. He recover {} {}".format(
                self.name,
                amount,
                upgrade['desc']
            ))
        return

    # Win counter module
    def add_win(self):
        self.win += 1
        return


def create_player():
    global PLAYER
    name = input(" :: Then tell me your name : ")
    PLAYER = Player(name)
    return
