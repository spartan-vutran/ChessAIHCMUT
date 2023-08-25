from enum import Enum
from typing import Optional, List

class Turn(Enum):
   WHITE = 0
   BLACK = 1


class Action:
  def __init__(self, pos, tar) -> None:
    self.pos = pos
    self.tar = tar


class Piece:
  def __init__(self):
    pass


class GameState:
    """
    The state of the game, with
    + board: A 2d table containing ids of pieces at each index
    + turn: 0 or 1, determining the player of the turn
    + white: List of white pieces
    + black: List of black pieces
    """

    def __init__(self, board: Optional[List[List[str]]] = None, turn: Optional[Turn] = Turn.WHITE):
      if board is None:
        self.board = [
          ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
          ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
      else:
        self.board = board
      self.turn = turn