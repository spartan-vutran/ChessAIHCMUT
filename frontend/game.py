import pygame
from .pieces import Rook, Queen, Pawn, Knight, King, Bishop
from typing import Tuple
from logic.game import GameState, GameController, Action
from enum import Enum
from frontend import settings

class Square:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.abs_x = x * width
		self.abs_y = y * height
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		self.color = 'light' if (x + y) % 2 == 0 else 'dark'
		self.draw_color = (220, 189, 194) if self.color == 'light' else (53, 53, 53)
		self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
		self.occupying_piece = None
		self.coord = self.get_coord()
		self.highlight = False

		self.rect = pygame.Rect(
			self.abs_x,
			self.abs_y,
			self.width,
			self.height
		)


	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)


	def draw(self, display):
		if self.highlight:
			pygame.draw.rect(display, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(display, self.draw_color, self.rect)

		if self.occupying_piece != None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)
			



class Player():
  pass


class Turn(Enum):
   WHITE = 0
   BLACK = 1

class Agent(Player):
  def __init__(self):
    pass

  def getMove(self, gameState):
    return Action((0,1),(0,2))

class Person(Player):
  def __init__(self):
    pass


# Game state checker
class GameFrontEnd:
  # option = {
  #    "cVsp": {
  #       "hard": "HardAgent",
  #       "medium": "MediumAgent",
  #       "easy": "EasyAgent",
  #    }
     
  # }

  def initGame(self):
    pygame.init()
    self.screen = pygame.display.set_mode(settings.WINDOW_SIZE)
    
  def __init__(self):
    self.width = settings.WINDOW_SIZE[0]
    self.height = settings.WINDOW_SIZE[1]
    self.tile_width = self.width // 8
    self.tile_height = self.height // 8
    self.selected_piece = None

    self.gameState =  GameState()
    self.squares = self.generate_squares()
    self.setup_board()
    
    # TODO: Add options to choose which agent to run
    self.setUpPlayer()
    self.initGame()
  

  def setUpPlayer(self):
    #  TODO: Mock choosing agents
    self.player1 = Agent()
    self.player2 = Person()
    self.players = [self.player1, self.player2]


  def play(self):
    """
      Control turn between agents or between agent and player
    """
    running = True
    while running:
      turn = self.gameState.turn
      curPlayer = self.players[turn.value]
      if isinstance(curPlayer, Agent):
        action = curPlayer.getMove(self.gameState)
        if not self.move(action):
          print("Invalid move")
      else:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
          # Quit the game if the user presses the close button
          if event.type == pygame.QUIT:
            running = False
          elif event.type == pygame.MOUSEBUTTONDOWN: 
            # If the mouse is clicked
            if event.button == 1:
              print("clicked: \n")
              print(mx, my)
              self.handle_click(mx,my)

        # if self.is_in_checkmate(Turn.BLACK): # If black is in checkmate
        #   print('White wins!')
        #   running = False
        # elif board.is_in_checkmate('white'): # If white is in checkmate
        #   print('Black wins!')
        #   running = False
        # # Draw the board
        self.draw()


  def move(self, action:Action):
    pos_square =  self.get_square_from_pos(action.pos)
    tar_square = self.get_square_from_pos(action.tar)

    piece =  pos_square.occupying_piece
    if not piece:
      return False

    # TODO: Check if piece run valid move
    is_valid_move = GameController.checkValidMove(self.gameState, Action)
    if not is_valid_move:
      return False
    
    pos_square.occupying_piece = None
    tar_square.occupying_piece = piece
    self.gameState = GameController.move(self.gameState, Action)
    return True
      

  def generate_squares(self):
    output = []
    for y in range(8):
      for x in range(8):
        output.append(
          Square(x,  y, self.tile_width, self.tile_height)
        )
    return output


  def get_square_from_pos(self, pos):
    for square in self.squares:
      if (square.x, square.y) == (pos[0], pos[1]):
        return square


  def get_piece_from_pos(self, pos):
    return self.get_square_from_pos(pos).occupying_piece


  def setup_board(self):
    # iterating 2d list
    for y, row in enumerate(self.gameState.board):
      for x, piece in enumerate(row):
        if piece != '':
          print(x,y,piece)
          square = self.get_square_from_pos((x, y))

          # looking inside contents, what piece does it have
          if piece[1] == 'R':
            square.occupying_piece = Rook(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )
          # as you notice above, we put `self` as argument, or means our class Board

          elif piece[1] == 'N':
            square.occupying_piece = Knight(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )

          elif piece[1] == 'B':
            square.occupying_piece = Bishop(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )

          elif piece[1] == 'Q':
            square.occupying_piece = Queen(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )

          elif piece[1] == 'K':
            square.occupying_piece = King(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )

          elif piece[1] == 'P':
            square.occupying_piece = Pawn(
              (x, y), Turn.WHITE if piece[0] == 'w' else Turn.BLACK, self
            )


  def handle_click(self, mx, my):
    x = mx // self.tile_width
    y = my // self.tile_height
    print(x, y)
    # clicked_square = self.get_square_from_pos((x, y))

    # if self.selected_piece is None:
    #   if clicked_square.occupying_piece is not None:
    #     if clicked_square.occupying_piece.side == self.gameState.turn:
    #       self.selected_piece = clicked_square.occupying_piece

    # elif self.selected_piece.move(self, clicked_square):
    #   self.turn = Turn.WHITE if self.turn == Turn.BLACK else Turn.BLACK

    # elif clicked_square.occupying_piece is not None:
    #   if clicked_square.occupying_piece.color == self.turn:
    #     self.selected_piece = clicked_square.occupying_piece


  def is_in_check(self, color, board_change=None): # board_change = [(x1, y1), (x2, y2)]
    output = False
    king_pos = None

    changing_piece = None
    old_square = None
    new_square = None
    new_square_old_piece = None

    if board_change is not None:
      for square in self.squares:
        if square.pos == board_change[0]:
          changing_piece = square.occupying_piece
          old_square = square
          old_square.occupying_piece = None
      for square in self.squares:
        if square.pos == board_change[1]:
          new_square = square
          new_square_old_piece = new_square.occupying_piece
          new_square.occupying_piece = changing_piece

    pieces = [
      i.occupying_piece for i in self.squares if i.occupying_piece is not None
    ]

    if changing_piece is not None:
      if changing_piece.notation == 'K':
        king_pos = new_square.pos
    if king_pos == None:
      for piece in pieces:
        if piece.notation == 'K' and piece.color == color:
            king_pos = piece.pos
    for piece in pieces:
      if piece.color != color:
        for square in piece.attacking_squares(self):
          if square.pos == king_pos:
            output = True

    if board_change is not None:
      old_square.occupying_piece = changing_piece
      new_square.occupying_piece = new_square_old_piece
            
    return output


  def is_in_checkmate(self, color):
    output = False

    for piece in [i.occupying_piece for i in self.squares]:
      if piece != None:
        if piece.notation == 'K' and piece.color == color:
          king = piece

    if king.get_valid_moves(self) == []:
      if self.is_in_check(color):
        output = True

    return output


  def draw(self):
    self.screen.fill('white')
    if self.selected_piece is not None:
      self.get_square_from_pos(self.selected_piece.pos).highlight = True
      for square in self.selected_piece.get_valid_moves(self):
        square.highlight = True
    for square in self.squares:
      square.draw(self.screen)
    pygame.display.update()