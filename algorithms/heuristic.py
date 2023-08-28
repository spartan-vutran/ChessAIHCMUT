import numpy
from logic.pieces.Rook import Rook
from logic.pieces.Bishop import Bishop
from logic.pieces.Knight import Knight
from logic.pieces.Queen import Queen
from logic.pieces.King import King
from logic.pieces.Pawn import Pawn
from logic.attributes import GameState, Move, Turn
from logic.game import chessLogic

class Heuristic:
  @staticmethod
  def eval(gs: GameState):
    pass

class MovingMatrixAndMaterialHeuristic(Heuristic):

    # The tables denote the points scored for the position of the chess pieces on the board.

    PAWN_TABLE = numpy.array([
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [ 5,  5, 10, 25, 25, 10,  5,  5],
        [ 0,  0,  0, 20, 20,  0,  0,  0],
        [ 5, -5,-10,  0,  0,-10, -5,  5],
        [ 5, 10, 10,-20,-20, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    KNIGHT_TABLE = numpy.array([
        [-50,-40,-30,-30,-30,-30,-40,-50],
        [-40,-20,  0,  0,  0,  0,-20,-40],
        [-30,  0, 10, 15, 15, 10,  0,-30],
        [-30,  5, 15, 20, 20, 15,  5,-30],
        [-30,  0, 15, 20, 20, 15,  0,-30],
        [-30,  5, 10, 15, 15, 10,  5,-30],
        [-40,-20,  0,  5,  5,  0,-20,-40],
        [-50,-40,-30,-30,-30,-30,-40,-50]
    ])

    BISHOP_TABLE = numpy.array([
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-10,-10,-10,-10,-10,-20]
    ])

    # ROOK_TABLE = numpy.array([
    #     [ 0,  0,  0,  0,  0,  0,  0,  0],
    #     [ 5, 10, 10, 10, 10, 10, 10,  5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [ 0,  0,  0,  5,  5,  0,  0,  0]
    # ])
    ROOK_TABLE = numpy.array([
        [ 0,  0,  0,  5,  5,  0,  0,  0],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [ 5, 10, 10, 10, 10, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    QUEEN_TABLE = numpy.array([
        [-20,-10,-10, -5, -5,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5,  5,  5,  5,  0,-10],
        [ -5,  0,  5,  5,  5,  5,  0, -5],
        [  0,  0,  5,  5,  5,  5,  0, -5],
        [-10,  5,  5,  5,  5,  5,  0,-10],
        [-10,  0,  5,  0,  0,  0,  0,-10],
        [-20,-10,-10, -5, -5,-10,-10,-20]
    ])

    KING_TABLE = numpy.array([
        [ 20, 30, 10,  0,  0, 10, 30, 20],
        [ 20, 20,  0,  0,  0,  0, 20, 20],
        [-10,-20,-20,-20,-20,-20,-20,-10],
        [-20,-30,-30,-40,-40,-30,-30,-20],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30]
    ])

    @staticmethod
    def eval(gs: GameState):
        heuristic = MovingMatrixAndMaterialHeuristic
        material = heuristic.get_material_score(gs, 0.4)
        

        pawns = heuristic.get_piece_position_score(gs, Pawn.NOTATION, heuristic.PAWN_TABLE, 0.1)
        knights = heuristic.get_piece_position_score(gs, Knight.NOTATION, heuristic.KNIGHT_TABLE, 0.1)
        bishops = heuristic.get_piece_position_score(gs, Bishop.NOTATION, heuristic.BISHOP_TABLE,0.1)
        rooks = heuristic.get_piece_position_score(gs, Rook.NOTATION, heuristic.ROOK_TABLE, 0.1)
        queens = heuristic.get_piece_position_score(gs, Queen.NOTATION, heuristic.QUEEN_TABLE, 0.1)
        kings = heuristic.get_piece_position_score(gs, King.NOTATION, heuristic.KING_TABLE, 0.1)

        # pawn_structure_bonus = 0
        # for col in range(8):
        #     white_pawns = sum(1 for row in range(0, 6) if gs.board[row][col] == 'wP')
        #     black_pawns = sum(1 for row in range(2, 8) if gs.board[row][col] == 'bP')
        #     pawn_structure_bonus += (white_pawns - black_pawns) * 5
    
        # mobility_bonus = 0
        # # Calculate mobility bonus for both sides (simple piece count)
        # white_mobility = sum(len(list(gs.board[row])) for row in range(8) if gs.board[row][0].startswith("w"))
        # black_mobility = sum(len(list(gs.board[row])) for row in range(8) if gs.board[row][0].startswith("b"))
        # mobility_bonus += white_mobility - black_mobility
        
        #late game, change heuristic funtion
        # return material + pawns + knights + bishops + rooks + queens + kings + pawn_structure_bonus + mobility_bonus
        return material + pawns + knights + bishops + rooks + queens + kings
    # Returns the score for the position of the given type of piece.
    # A piece type can for example be: pieces.Pawn.PIECE_TYPE.
    # The table is the 2d numpy array used for the scoring. Example: Heuristics.PAWN_TABLE
    @staticmethod
    def get_piece_position_score(gs: GameState, piece_notation, table, weight):
      white = 0
      black = 0
      numberList = []
      for x in range(8):
          for y in range(8):
              numberList.append(table[x][y])
              piece = gs.board[x][y]
              if (piece != ''):
                  if piece.endswith(piece_notation):
                      if (piece.startswith("w")):
                          white += table[x][y]
                      else:
                          black += table[7 - x][y]
      numberList.sort()
      maxWhiteValue = sum(numberList[-20:])
      minBlackValue = numberList[0]
      return ((white - black)/(maxWhiteValue-minBlackValue))*weight

    @staticmethod
    def get_material_score(gs: GameState, weight: float):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                piece = gs.board[x][y]
                score = 0
                if (piece != ''):
                    if piece.endswith(King.NOTATION):
                        score = King.VALUE
                    elif piece.endswith(Queen.NOTATION):
                        score = Queen.VALUE
                    elif piece.endswith(Rook.NOTATION):
                        score = Rook.VALUE
                    elif piece.endswith(Bishop.NOTATION):
                        score = Bishop.VALUE
                    elif piece.endswith(Knight.NOTATION):
                        score = Knight.VALUE
                    elif piece.endswith(Pawn.NOTATION):
                        score = Pawn.VALUE

                    if (piece.startswith("w")):
                        white += score
                    else:
                        black += score
                    score = 0
        highestDiff = (Queen.VALUE + 2*Rook.VALUE + 2*Bishop.VALUE+ 2*Knight.VALUE+ 8*Pawn.VALUE)
        return ((white - black)/highestDiff)*weight
    

class AdvancedHeuristic(Heuristic):

    # The tables denote the points scored for the position of the chess pieces on the board.

    PAWN_TABLE = numpy.array([
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [ 5,  5, 10, 25, 25, 10,  5,  5],
        [ 0,  0,  0, 20, 20,  0,  0,  0],
        [ 5, -5,-10,  0,  0,-10, -5,  5],
        [ 5, 10, 10,-20,-20, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    KNIGHT_TABLE = numpy.array([
        [-50,-40,-30,-30,-30,-30,-40,-50],
        [-40,-20,  0,  0,  0,  0,-20,-40],
        [-30,  0, 10, 15, 15, 10,  0,-30],
        [-30,  5, 15, 20, 20, 15,  5,-30],
        [-30,  0, 15, 20, 20, 15,  0,-30],
        [-30,  5, 10, 15, 15, 10,  5,-30],
        [-40,-20,  0,  5,  5,  0,-20,-40],
        [-50,-40,-30,-30,-30,-30,-40,-50]
    ])

    BISHOP_TABLE = numpy.array([
        [-20,-10,-10,-10,-10,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5, 10, 10,  5,  0,-10],
        [-10,  5,  5, 10, 10,  5,  5,-10],
        [-10,  0, 10, 10, 10, 10,  0,-10],
        [-10, 10, 10, 10, 10, 10, 10,-10],
        [-10,  5,  0,  0,  0,  0,  5,-10],
        [-20,-10,-10,-10,-10,-10,-10,-20]
    ])

    # ROOK_TABLE = numpy.array([
    #     [ 0,  0,  0,  0,  0,  0,  0,  0],
    #     [ 5, 10, 10, 10, 10, 10, 10,  5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [-5,  0,  0,  0,  0,  0,  0, -5],
    #     [ 0,  0,  0,  5,  5,  0,  0,  0]
    # ])
    ROOK_TABLE = numpy.array([
        [ 0,  0,  0,  5,  5,  0,  0,  0],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [ 5, 10, 10, 10, 10, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    QUEEN_TABLE = numpy.array([
        [-20,-10,-10, -5, -5,-10,-10,-20],
        [-10,  0,  0,  0,  0,  0,  0,-10],
        [-10,  0,  5,  5,  5,  5,  0,-10],
        [ -5,  0,  5,  5,  5,  5,  0, -5],
        [  0,  0,  5,  5,  5,  5,  0, -5],
        [-10,  5,  5,  5,  5,  5,  0,-10],
        [-10,  0,  5,  0,  0,  0,  0,-10],
        [-20,-10,-10, -5, -5,-10,-10,-20]
    ])

    KING_TABLE = numpy.array([
        [ 20, 30, 10,  0,  0, 10, 30, 20],
        [ 20, 20,  0,  0,  0,  0, 20, 20],
        [-10,-20,-20,-20,-20,-20,-20,-10],
        [-20,-30,-30,-40,-40,-30,-30,-20],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30],
        [-30,-40,-40,-50,-50,-40,-40,-30]
    ])

        
    def material(gs: GameState, weight):
      white = 0
      black = 0
      for x in range(8):
          for y in range(8):
              piece = gs.board[x][y]
              score = 0
              if (piece != ''):
                  if piece.endswith(King.NOTATION):
                      score = 0
                  elif piece.endswith(Queen.NOTATION):
                      score = 9
                  elif piece.endswith(Rook.NOTATION):
                      score = 5
                  elif piece.endswith(Bishop.NOTATION):
                      score = 3
                  elif piece.endswith(Knight.NOTATION):
                      score = 3
                  elif piece.endswith(Pawn.NOTATION):
                      score = 1

                  if (piece.startswith("w")):
                      white += score
                  else:
                      black += score
                  score = 0
      
      max_diff = 39 #Point when the difference between # pieces is max
      return ((white - black)*weight) / max_diff
        

    def piece_moves(gs: GameState, weight):
      # This heuristic calculates the number of legal moves a player can make. It encourages the AI to develop its pieces to exert more control over the board. 
      white_points = 0
      square_values = {(4,4): 1, (3,4): 1, (4,3): 1, (3,3): 1, (2,2): 0.5, (2,3): 0.5, (4,4): 0.5, (2,5): 0.5, (5,2): 0.5, (5,3):0.5, (5,4): 0.5, (5,5): 0.5, (4,2): 0.5, (3,2): 0.5, (4,5): 0.5, (3,5): 0.5}
      maxPoint = 1
      for action in chessLogic.actions(gs):
        target = action.tar
        if not isinstance(action, Move) or target not in square_values:
          continue
        white_points += square_values[target] if gs.turn == Turn.WHITE else -square_values[target] 
        maxPoint += 1
      pointInPerCen = white_points/maxPoint
      return pointInPerCen*weight


    def in_check(gs: GameState, weight):
      # This heuristic checks if a player is in check or checkmate status. It encourages the AI to make moves that would put the opponent in check while avoiding moves that would put itself in check.
      if chessLogic.isTerminal(gs):
        return 1*weight if gs.turn == Turn.BLACK else -1*weight
      else: return 0


    def pawn_structure(gs: GameState, weight):
      # The pawn structure heuristic gives a score based on the number of pawns supported by other pawns. It encourages the AI to develop its pawns in a way that allows pawns moving forward to be defended by other pawns from behind.

      # determine pawn to search for based on whose turn it is
      vector, color = (-1, "b") if gs.turn == Turn.BLACK else (1,"w")
      point = 0
      for i, row in enumerate(gs.board):
          for j in range(len(row)):
              if gs.board[i][j] == f"{color}P":
                  tl = i-vector, j-vector
                  tr = i-vector, j+vector
                  if tl[0] >= 0 and tl[0] <= 7 and tl[1] >= 0 and tl[1] <= 7:
                      if gs.board[tl[0]][tl[1]] == f"{color}P":
                          point += 1
                  if tr[0] >= 0 and tr[0] <= 7 and tr[1] >= 0 and tr[1] <= 7:
                      if gs.board[tr[0]][tr[1]] == f"{color}P":
                          point += 1
      return (point/16) * weight


    @staticmethod
    def eval(gs: GameState):
      total_points = 0
      # total piece count
      total_points += AdvancedHeuristic.material(gs, 0.3)
      total_points += AdvancedHeuristic.piece_moves(gs, 0.075)
      total_points += AdvancedHeuristic.in_check(gs, 0.05)
      total_points += AdvancedHeuristic.pawn_structure(gs, 0.075)
      

      pawns = AdvancedHeuristic.get_piece_position_score(gs, Pawn.NOTATION, AdvancedHeuristic.PAWN_TABLE, 0.025)
      knights = AdvancedHeuristic.get_piece_position_score(gs, Knight.NOTATION, AdvancedHeuristic.KNIGHT_TABLE, 0.075)
      bishops = AdvancedHeuristic.get_piece_position_score(gs, Bishop.NOTATION, AdvancedHeuristic.BISHOP_TABLE,0.075)
      rooks = AdvancedHeuristic.get_piece_position_score(gs, Rook.NOTATION, AdvancedHeuristic.ROOK_TABLE, 0.1)
      queens = AdvancedHeuristic.get_piece_position_score(gs, Queen.NOTATION, AdvancedHeuristic.QUEEN_TABLE, 0.15)
      kings = AdvancedHeuristic.get_piece_position_score(gs, King.NOTATION, AdvancedHeuristic.KING_TABLE, 0.075)
      
      return pawns + knights + bishops + rooks + queens + kings + total_points
    
    @staticmethod
    def get_piece_position_score(gs: GameState, piece_notation, table, weight):
      white = 0
      black = 0
      numberList = []
      for x in range(8):
          for y in range(8):
              numberList.append(table[x][y])
              piece = gs.board[x][y]
              if (piece != ''):
                  if piece.endswith(piece_notation):
                      if (piece.startswith("w")):
                          white += table[x][y]
                      else:
                          black += table[7 - x][y]
      numberList.sort()
      maxWhiteValue = sum(numberList[-20:])
      minBlackValue = numberList[0]
      return ((white - black)/(maxWhiteValue-minBlackValue))*weight