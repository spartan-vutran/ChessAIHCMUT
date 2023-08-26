import pygame
from typing import Tuple, List
from logic.attributes import Piece, GameState

class Bishop(Piece):
  NOTATION = 'B'
  VALUE = 330
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_bishop.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))
    self.notation = 'B'


  def getValidMoves(gs: GameState, pos: Tuple[int]) -> List[Tuple[int]]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"
    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != Bishop.NOTATION:
      return []

    output = []
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
	# def get_possible_moves(self, board):
	# 	output = []

	# 	moves_ne = []
	# 	for i in range(1, 8):
	# 		if self.x + i > 7 or self.y - i < 0:
	# 			break
	# 		moves_ne.append(board.get_square_from_pos(
	# 			(self.x + i, self.y - i)
	# 		))
	# 	output.append(moves_ne)

	# 	moves_se = []
	# 	for i in range(1, 8):
	# 		if self.x + i > 7 or self.y + i > 7:
	# 			break
	# 		moves_se.append(board.get_square_from_pos(
	# 			(self.x + i, self.y + i)
	# 		))
	# 	output.append(moves_se)

	# 	moves_sw = []
	# 	for i in range(1, 8):
	# 		if self.x - i < 0 or self.y + i > 7:
	# 			break
	# 		moves_sw.append(board.get_square_from_pos(
	# 			(self.x - i, self.y + i)
	# 		))
	# 	output.append(moves_sw)

	# 	moves_nw = []
	# 	for i in range(1, 8):
	# 		if self.x - i < 0 or self.y - i < 0:
	# 			break
	# 		moves_nw.append(board.get_square_from_pos(
	# 			(self.x - i, self.y - i)
	# 		))
	# 	output.append(moves_nw)

	# 	return output