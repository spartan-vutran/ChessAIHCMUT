
from typing import List
from logic.pieces.Rook import Rook
from logic.pieces.Bishop import Bishop
from logic.pieces.Knight import Knight
from logic.pieces.Queen import Queen
from logic.pieces.King import King
from logic.pieces.Pawn import Pawn
from logic.attributes import Turn, Action, GameState


class GameController:
  """
  All logic of the chess game has to communicate to this class
  """
  pieceDict = {
    "R": Rook,
    "B": Bishop,
    "K": Knight,
    "Q": Queen,
    "K": King,
    "P": Pawn,
  }
  def __init__(self):
    pass
  

  def toMove(self, gs: GameState) -> Turn:
    """
    Return player of the state
    """
    return gs.turn
  

  def findPiecesofPlayer(self, gs: GameState) -> List[int]:
    """
    Find all pieces on board of player in turn
    """
    player_color = "w" if gs.turn == Turn.WHITE else "b"
    player_pieces = []
    for i, row in enumerate(gs.board):
      for j, piece in enumerate(row):
        if piece.startswith(player_color):
          player_pieces.append((i,j))
      
    return player_pieces


  def actions(self, gs: GameState) -> List[Action]:
    """
    Find all actions from given states
    """
    playerPieceIndexes = self.findPiecesofPlayer(gs)
    actions = []
    for posRow, posCol  in playerPieceIndexes:
      piece = gs.board[posRow][posCol]
      pieceClass = self.pieceDict[piece[1]]
      validMoves = pieceClass.getValidMoves(gs, (posRow,posCol))
      for tarRow, tarCol in validMoves:
        actions.append(Action((posRow, posCol),(tarRow, tarCol)))
    
    return actions


  def checkValidMove(gs: GameState, action: Action) -> bool:
    return True

  def move(gs: GameState, action: Action) -> GameState:
    board = [
          ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
          ['', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
          ['bP','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['','','','','','','',''],
          ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
          ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
    return GameState(board, Turn.BLACK)



