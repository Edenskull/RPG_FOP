import plugins.GameSystem.properties as properties

from plugins.GameSystem.upgrade import UPGRADES
from random import choices


def trigger_shop(player):
    print("Bienvenue dans mon shop")
    items = generate_item()
    while True:
        display_items(items, player)
        while True:
            code, u_choix = prompt_player(items)
            if code == "exit":
                break
            elif code == "break":
                break
            elif code == "continue":
                continue
        if code == "exit":
            break
        if player_has_enough(player, items[u_choix]['cost']):
            buy(items[u_choix], player)
            items.pop(u_choix)
        else:
            print("Tu n'as pas assez d'argent")
    print("Au revoir")


def player_has_enough(player, cost):
    if player.argent >= cost:
        return True
    else:
        return False


def generate_item():
    return choices(UPGRADES, k=3)


def display_items(items, player):
    pos = 1
    for item in items:
        print("{} - {} : {} {}".format(pos, item['name'], item['cost'], properties.DEVISE))
        pos += 1
    print("Vous possedez {} {}".format(player.argent, properties.DEVISE))
    return


def prompt_player(items):
    u_choix = input("Choisir un article : ")
    if u_choix.isdigit():
        u_choix = int(u_choix)
    elif u_choix == "quit":
        return "exit", None
    else:
        print("Je n'ai pas cette article")
        return "continue", None
    if 0 <= u_choix < len(items):
        return "break", u_choix
    else:
        print("Je n'ai pas cette article")
        return "continue", None


def buy(upgrade, player):
    player.money -= upgrade['cost']
    print("{} a {} {}".format(player.name, player.money, properties.DEVISE))
    player.apply_upgrade(upgrade)
    return
