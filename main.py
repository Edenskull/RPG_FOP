import plugins.GameSystem.game as gm
import plugins.GameSystem.player as player

from plugins.GameSystem.shop import trigger_shop


def run():
    gm.game_start()
    print(gm.GAMESTATE.GAMESTATE)


if __name__ == "__main__":
    run()
