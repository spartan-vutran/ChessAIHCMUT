import pygame
from logic.attributes import Piece, GameState
from typing import Tuple

class Queen(Piece):
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_queen.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))

    self.notation = 'Q'

  def getValidMoves(gs: GameState, pos: Tuple[int]) -> Tuple[int]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"
    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != "Q":
      return []

    output = []
    # Move North
    moves_north = []
    for x in range(row)[::-1]:
      square = gs.board[x][col]
      if square != "":
        if square[1] != player_color:
          moves_north.append((x,col))
        break
      moves_north.append((x,col))
    output.append(moves_north)

    # Move SouthEast
    moves_se = []
    for i in range(1, 8):
      tar_row, tar_col = (row+i, col+i)
      if tar_row > 7 or tar_col > 7:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[1] != player_color:
          moves_se.append((tar_row, tar_col))
        break
      moves_se.append((tar_row, tar_col))
    output.append(moves_se)

    # Move East
    moves_east = []
    for x in range(col + 1, 8):
      square = gs.board[row][x]
      if square != "":
        if square[1] != player_color:
          moves_east.append((row,x))
        break
      moves_east.append((row,x))
    output.append(moves_east)

    # Move NorthEast
    moves_ne = []
    for i in range(1, 8):
      tar_row, tar_col = (row-i, col+i)
      if tar_row < 0 or tar_col > 7:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[1] != player_color:
          moves_ne.append((tar_row, tar_col))
        break
      moves_ne.append((tar_row, tar_col))
    output.append(moves_ne)

    # Move South
    moves_south = []
    for x in range(row + 1, 8):
      square = gs.board[x][col]
      if square != "":
        if square[1] != player_color:
          moves_south.append((x,col))
        break
      moves_south.append((x,col))
    output.append(moves_south)

    # Move NorthWest
    moves_nw = []
    for i in range(1, 8):
      tar_row, tar_col = (row-i, col-i)
      if tar_row < 0 or tar_col < 0:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[1] != player_color:
          moves_nw.append((tar_row, tar_col))
        break
      moves_nw.append((tar_row, tar_col))
    output.append(moves_nw)

    # Move West
    moves_west = []
    for y in range(col)[::-1]:
      square = gs.board[row][y]
      if square != "":
        if square[1] != player_color:
          moves_west.append((row,y))
        break
      moves_west.append((row,y))
    output.append(moves_west)

    # Move SouthWest
    moves_sw = []
    for i in range(1, 8):
      tar_row, tar_col = (row+i, col-i)
      if tar_row > 7 or tar_col < 0:
        break
      square = gs.board[tar_row][tar_col]
      if square != "":
        if square[1] != player_color:
          moves_sw.append((tar_row, tar_col))
        break
      moves_sw.append((tar_row, tar_col))
    output.append(moves_sw)

    return output