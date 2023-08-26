import pygame
from typing import Tuple, List
from logic.attributes import Piece, GameState, Turn, Action, Move, EnterTower
import copy 
class King(Piece):
  NOTATION = 'K'
  VALUE = 20000
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_king.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))


  def getValidMoves(gs: GameState, pos:Tuple[int]) -> List[Tuple[int]]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"
    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != King.notation:
      return []
    
    # Get possible moves without legitimate
    possibleMoves = []
    for i in range(-1,2):
      for j in range(-1,2):
        if i == 0 and j == 0:
          continue
        tarRow, tarCol = row+i, col+j
        if tarRow > 7 or tarRow < 0 or tarCol > 7 or tarCol <0:
          continue
        square = gs.board[tarRow][tarCol]
        if square != "" and square[0] == player_color:
          continue
        possibleMoves.append(Move((row,col),(tarRow, tarCol)))

    # Enter tower move
    sideValue = gs.turn.value
    
    isEnterMoveImpossible = gs.isEnterTower[sideValue] or gs.isKingMove[sideValue] or gs.isLeftRockMove[sideValue] or gs.isRightRockMove[sideValue]

    return possibleMoves

