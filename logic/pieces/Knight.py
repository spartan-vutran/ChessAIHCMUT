import pygame
from typing import Tuple, List
from logic.attributes import Piece, GameState

class Knight(Piece):
  notation = 'N'
  def __init__(self, pos, color, board):
    super().__init__(pos, color, board)

    img_path = 'data/imgs/' + color[0] + '_knight.png'
    self.img = pygame.image.load(img_path)
    self.img = pygame.transform.scale(self.img, (board.tile_width - 20, board.tile_height - 20))


  def getValidMoves(gs: GameState, pos:Tuple[int]) -> List[Tuple[int]]:
    row, col = pos
    player_color = "w" if gs.turn.value == 0 else "b"

    # Check if the piece is valid
    if gs.board[row][col][0] != player_color or  gs.board[row][col][1] != Knight.notation:
      return []
    
    # Get moves of Knight
    ele_1 = [[1,-1], [2,-2]] 
    ele_2 = [[2,-2], [1,-1]]
    # First try unit 1 for col
    validMoves = []
    index = 0
    while index < 2:
      yele, xele = ele_1[index], ele_2[index]
      for y in yele:
        for x in xele:
          tarRow, tarCol = row + x, col + y
          if tarRow > 7 or tarRow < 0 or tarCol > 7 or tarCol < 0:
            continue
          tarSquare = gs.board[tarRow][tarCol]
          if tarSquare != '' and tarSquare[0] == player_color:
            continue
          validMoves.append((tarRow, tarCol))
      index = index + 1
    
    return validMoves
    

    


	# def get_possible_moves(self, board):
	# 	output = []
	# 	moves = [
	# 		(1, -2),
	# 		(2, -1),
	# 		(2, 1),
	# 		(1, 2),
	# 		(-1, 2),
	# 		(-2, 1),
	# 		(-2, -1),
	# 		(-1, -2)
	# 	]

	# 	for move in moves:
	# 		new_pos = (self.x + move[0], self.y + move[1])
	# 		if (
	# 			new_pos[0] < 8 and
	# 			new_pos[0] >= 0 and 
	# 			new_pos[1] < 8 and 
	# 			new_pos[1] >= 0
	# 		):
	# 			output.append([
	# 				board.get_square_from_pos(
	# 					new_pos
	# 				)
	# 			])

	# 	return output