from function.PyLogger.pylogger import pylogger
from function.GameSystem.shop import trigger_shop
from function.GameSystem.player import create_player


def run():
    player = create_player()
    trigger_shop(player)


if __name__ == "__main__":
    # pylogger.info("Starting RPG_FOP Game")
    run()
