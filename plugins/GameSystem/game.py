import plugins.GameSystem.properties as properties

from enum import Enum
from plugins.GameSystem.player import create_player


class EnumState(Enum):
    WAIT = 'Wait'
    READY = 'Ready'
    RUN = 'Run'
    END = 'End'


class GameState:
    def __init__(self):
        self.GAMESTATE = EnumState.WAIT
        return

    def change_gamestate(self, state):
        if isinstance(state, EnumState):
            self.GAMESTATE = state
        return


def game_start():
    global GAMESTATE
    GAMESTATE = GameState()
    print("Good morning traveller, I\'m here to force you to play with me to this RPG.")
    create_player()
    GAMESTATE.change_gamestate(EnumState.READY)
    return
