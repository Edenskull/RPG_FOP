import plugins.GameSystem.properties as properties
import plugins.GameSystem.player as player

from enum import Enum


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


class Dungeon:
    def __init__(self):
        self.DUNGEON_FLOOR = 1
        return

    def get_floor_ennemies(self):
        if 1 < self.DUNGEON_FLOOR < 10:
            return [1, 2]


def game_start():
    global GAMESTATE
    GAMESTATE = GameState()
    print("Good morning traveller, I\'m here to force you to play with me to this RPG.")
    player.create_player()
    GAMESTATE.change_gamestate(EnumState.READY)
    return


def enter_dungeon():
    global GAMESTATE
    GAMESTATE.change_gamestate(EnumState.RUN)
    while GAMESTATE.GAMESTATE == EnumState.READY:
        pass

