from enum import Enum
from typing import Optional, List

class Side(Enum):
   WHITE = 0
   BLACK = 1


class GameState:
    """
    The state of the game, with
    + board: A 2d table containing ids of pieces at each index
    + turn: 0 or 1, determining the player of the turn
    + white: List of white pieces
    + black: List of black pieces
    """

    def __init__(board: Optional(List[List[str]]) = None, turn: Optional[Side] = Side.WHITE):
      if board is None:
         


class GameController:
    """
    This class deals with the transition of game states and related
    game features
    """
    pieceDict = {
        "WP":   
    }
