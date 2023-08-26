import pygame
from typing import Tuple, List
from logic.attributes import Piece, GameState, Move, Action


class Rook(Piece):
  NOTATION = 'R'
  VALUE = 500
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_rook.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
    self.notation = 'R'


  def getValidMoves(gs: GameState, pos:Tuple[int]) -> List[Action]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"
    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != Rook.NOTATION:
      return []

    validMoves = []
    # Upper move checking
    for uI in range(row+1,8):
      target_square = gs.board[uI][col]
      if target_square != '':
        if target_square[0] != player_color:
          validMoves.append(Move((row,col), (uI,col)))
        break
      validMoves.append(Move((row,col), (uI,col)))
    
    # Lower move checking
    for lI in list(reversed(range(0, row))):
      target_square = gs.board[lI][col]
      if target_square != '':
        if target_square[0] != player_color:
          validMoves.append(Move((row,col),(lI,col)))
        break
      validMoves.append(Move((row,col),(lI,col)))
    
    # Right move checking
    for rI in range(col+1, 8):
      target_square = gs.board[row][rI]
      if target_square != '':
        if target_square[0] != player_color:
          validMoves.append(Move((row,col),(row,rI)))
        break
      validMoves.append(Move((row,col),(row,rI)))
    
    # Left move checking
    for lI in list(reversed(range(0,col))):
      target_square = gs.board[row][lI]
      if target_square != '':
        if target_square[0] != player_color:
          validMoves.append(Move((row,col),(row,lI)))
        break
      validMoves.append(Move((row,col),(row,lI)))

    return validMoves