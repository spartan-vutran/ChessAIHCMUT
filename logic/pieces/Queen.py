import pygame
from logic.attributes import Piece, GameState
from typing import Tuple, List

class Queen(Piece):
  notation = 'Q'
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_queen.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

  def getValidMoves(gs: GameState, pos: Tuple[int]) -> List[Tuple[int]]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"
    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != Queen.notation:
      return []

    output = []
    # Move North
    for x in range(row)[::-1]:
      square = gs.board[x][col]
      if square != "":
        if square[0] != player_color:
          output.append((x,col))
        break
      output.append((x,col))

    # Move SouthEast
    for i in range(1, 8):
      tar_row, tar_col = (row+i, col+i)
      if tar_row > 7 or tar_col > 7:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[0] != player_color:
          output.append((tar_row, tar_col))
        break
      output.append((tar_row, tar_col))

    # Move East
    for x in range(col + 1, 8):
      square = gs.board[row][x]
      if square != "":
        if square[0] != player_color:
          output.append((row,x))
        break
      output.append((row,x))

    # Move NorthEast
    for i in range(1, 8):
      tar_row, tar_col = (row-i, col+i)
      if tar_row < 0 or tar_col > 7:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[0] != player_color:
          output.append((tar_row, tar_col))
        break
      output.append((tar_row, tar_col))

    # Move South
    for x in range(row + 1, 8):
      square = gs.board[x][col]
      if square != "":
        if square[0] != player_color:
          output.append((x,col))
        break
      output.append((x,col))

    # Move NorthWest
    for i in range(1, 8):
      tar_row, tar_col = (row-i, col-i)
      if tar_row < 0 or tar_col < 0:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[0] != player_color:
          output.append((tar_row, tar_col))
        break
      output.append((tar_row, tar_col))

    # Move West
    for y in range(col)[::-1]:
      square = gs.board[row][y]
      if square != "":
        if square[0] != player_color:
          output.append((row,y))
        break
      output.append((row,y))

    # Move SouthWest
    for i in range(1, 8):
      tar_row, tar_col = (row+i, col-i)
      if tar_row > 7 or tar_col < 0:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[0] != player_color:
          output.append((tar_row, tar_col))
        break
      output.append((tar_row, tar_col))

    return output