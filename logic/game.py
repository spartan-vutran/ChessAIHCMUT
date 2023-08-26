from typing import List, Tuple
from logic.attributes import Turn, Action, GameState
from logic.pieces.Rook import Rook
from logic.pieces.Bishop import Bishop
from logic.pieces.Knight import Knight
from logic.pieces.Queen import Queen
from logic.pieces.King import King
from logic.pieces.Pawn import Pawn
from logic.attributes import Action, Move, QueenPromote, EnterTower
import copy


class GameController:
  """
  All logic of the chess game has to communicate to this class
  """

  pieceDict = {
    "R": Rook,
    "B": Bishop,
    "N": Knight,
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
  

  def findPiecesofPlayer(self, gs: GameState, turn: Turn) -> List[Tuple[int]]:
    """
    Find all pieces on board of player in turn
    Return: A tuple with:
      + First ele: An array containing indice of all position of pieces of the player
      + Second ele: A position tuple for the King piece (Used to conveniently check checkmate)
    """
    player_color = "w" if turn == Turn.WHITE else "b"
    player_pieces = []
    king_pos = (None,None)
    for i, row in enumerate(gs.board):
      for j, piece in enumerate(row):
        if piece != "" and piece[0] == player_color:
          if piece[1]=="K":
            king_pos = (i,j)
            continue
          player_pieces.append((i,j))
      
    return (player_pieces, king_pos)


  def getPiecesFromOpponent(self, gs:GameState) -> List[Tuple[int]]:
    opponentColor = "b" if gs.turn.value == 0 else "w"
    pieces = []
    for i, row in enumerate(gs.board):
      for j, piece in enumerate(row):
        if piece != '' and piece[0] == opponentColor:
          pieces.append((i,j))
    return pieces
  

  # def getAllEndangeredMoves(self, gs:GameState) -> List[Tuple[int]]:
  #   opponentPieces = self.getPiecesFromOpponent(gs)
  #   endangredMoves = set()
  #   fakeGs = copy.deepcopy(gs)  #If it is your turn, what square will be in danger ?
  #   fakeGs.turn = Turn.WHITE if gs.turn.value == 1 else Turn.BLACK
  #   for row, col in opponentPieces:
  #     piece = gs.board[row][col]
  #     pieceClass = self.pieceDict[piece[1]]
  #     endangredMoves.update(pieceClass.getValidMoves(fakeGs, (row, col)))

  #   return list(endangredMoves)


  def _isEndangered(self, gs:GameState, pos: Tuple, opponentTurn: Turn) -> bool:
    """
    The function checks if the current position is endangred by "opponentTurn"
    """
    opponentPiecesExceptKing, opponentKing = self.findPiecesofPlayer(gs, opponentTurn)
    opponentPieces = opponentPiecesExceptKing + [opponentKing]
    if opponentKing[0] == None: #Opponent does not have a King
      return False
    endangredSquares = set()
    gs.turn = opponentTurn #If it is your turn, Am I endangered ?
    for posRow, posCol  in opponentPieces:
      piece = gs.board[posRow][posCol]
      pieceClass = self.pieceDict[piece[1]]
      if pieceClass == King:
        validMoves = pieceClass.getNormalMoves(gs, (posRow,posCol)) # TOFIX: It is a bit odd here 
      else:
        validMoves = pieceClass.getValidMoves(gs, (posRow,posCol))

      # Filter only capturing actions
      capturingMoves = [move.tar for move in validMoves if isinstance(move, Move)]
      endangredSquares.update(capturingMoves)

    gs.turn = Turn.WHITE if opponentTurn== Turn.BLACK else Turn.BLACK #Return back to its original turn before return
    return pos in endangredSquares
    

  # def _kingSignalForCheckmate(self, gs:GameState, pos:Tuple[int]) -> Tuple:
  #   """
  #   Params:
  #   + pos: the position where the King is
  #   This function returns (s, information), where:
  #   + s is:
  #       + None: for invalid parameter
  #       + 0: If the King is not endangerd
  #       + 1: If the King is endangered and return target positions in "information" to avoid being captured.
  #       + 2: Checkmated.

  #   NOTICE: that the piece must be in the same side of game state
  #   """
  #   kRow, kCol = pos
  #   kSquare = gs.board[kRow][kCol]
  #   kSide, opponentSide = (Turn.WHITE, Turn.BLACK) if kSquare[0] == "w" else (Turn.BLACK, Turn.WHITE) 

  #   if kSquare == "" or kSquare[1] != "K" or gs.turn != kSide:
  #     return (None, None)
    
  #   isEndangered = self._isEndangered(gs, pos, opponentSide)
    
  
  def getValidMovesOfAllPiecesWith(self, gs:GameState, isEndangered: bool = False) -> List[Action]:
    """
    This function returns all moves of pieces, in case "kPos" is given, that means kPos is in danger, only return moves that avoid being captured
    """
    # if kPos:
    #   kRow, kCol
    #   kingClass = self.pieceDict[kSquare[1]]
    # possibleMoves = kingClass.getValidMoves(self, gs, pos)
    playerPieceIndexes, kingIndex = self.findPiecesofPlayer(gs, gs.turn)
    pieces = playerPieceIndexes + [kingIndex]
    kActions = []
    actions = []
    for posRow, posCol  in pieces:
      piece = gs.board[posRow][posCol]
      pieceClass = self.pieceDict[piece[1]]
      if pieceClass == King:
        kActions += pieceClass.getValidMoves(self, gs, (posRow,posCol))
      else:
        actions += pieceClass.getValidMoves(gs, (posRow,posCol))

    if not isEndangered:
      return kActions + actions
    # Keep only those actions would make the King avoid being captured
    opponentTurn = Turn.WHITE if gs.turn == Turn.BLACK else Turn.WHITE
    eligibleActions = []
    for action in actions:
      newGs = self.move(gs, action)
      if not self._isEndangered(newGs, kingIndex, opponentTurn):
        eligibleActions.append(action)

    for action in kActions:
      newGs = self.move(gs, action)
      if not self._isEndangered(newGs, action.tar, opponentTurn):
        eligibleActions.append(action)

    return eligibleActions
    # Remaining not endangered moves
    # remainningMoves = []
    # for move in possibleMoves:
    #   # Check what happend if I move to that state
    #   # We check only normal moves because enter tower moves are prechecked 
    #   if isinstance(move, Move):
    #     tarRow, tarCol = move.tar
    #     tarPiece = gs.board[tarRow][tarCol]
    #     gs.board[kRow][kCol] =""
    #     gs.board[tarRow][tarCol]= kSquare
    #     if not self._isEndangered(gs, move.tar, opponentSide): 
    #       remainningMoves.append(move)
    #     # Return back to origin state
    #     gs.board[tarRow][tarCol] = tarPiece
    #     gs.board[kRow][kCol] = kSquare
    #   else:
    #     remainningMoves.append(move)
    #     #TOFIX: It seems a bit odd because we have to do this to get all valid moves
    # if remainningMoves and not isEndangered:
    #   return (0, remainningMoves)
    # elif remainningMoves and isEndangered:
    #   return (1, remainningMoves)
    # return (2, [])

  def actions(self, gs: GameState) -> List[Action]:
    """
    Find all actions from given states
    """
    opponentTurn = Turn.WHITE if gs.turn == Turn.BLACK else Turn.WHITE
    sideColor = "w" if gs.turn == Turn.WHITE else "b"
    kingIndex = self.findPiecesById(gs, f"{sideColor}K")[0]
    # Check if the king is endangred or checkMate
    # TODO: Check if the king is endangered
    isEndangered = self._isEndangered(gs, kingIndex, opponentTurn)
    
    return self.getValidMovesOfAllPiecesWith(gs, isEndangered)

    # if kingIndex[0] == None: #The state does not have a King
    #   return []
    # signal, info = self._kingSignalForCheckmate(gs, kingIndex)
    # if signal == 1:
    #   # The king is endangred but there is still a move
    #   return info
    # if signal == 2:
    #   # You are checkmated 
    #   return []
    # actions = []
    # actions += info #Add possible moves for the Kings
    # for posRow, posCol  in playerPieceIndexes:
    #   piece = gs.board[posRow][posCol]
    #   pieceClass = self.pieceDict[piece[1]]
    #   actions += pieceClass.getValidMoves(gs, (posRow,posCol))
    # return actions


  def checkValidMove(self, gs: GameState, action: Action) -> bool:
    row, col = action.pos
    square = gs.board[row][col]
    if square == '':
      return False
    pieceClass = self.pieceDict[square[1]]
    if pieceClass == King:
      validActions = pieceClass.getValidMoves(self, gs, (row,col))
    else:
      validActions = pieceClass.getValidMoves(gs, (row,col))
    return action in validActions

  
  def move(self, gs: GameState, action: Action) -> GameState:
    turn = Turn.WHITE if gs.turn.value == Turn.BLACK.value else Turn.BLACK
    # TODO: 
    #Action Move:
    # + move
    #Action Queen promote
    # + promote pawn to queen
    #Action EnterTower
    # + move King
    # + move Rook

    gs = copy.deepcopy(gs)
    pos = action.pos
    tar = action.tar
    board = gs.board
    player_color = "w" if gs.turn.value == 0 else "b"

    piece = board[pos[0]][pos[1]]
    board[pos[0]][pos[1]] = ''
    board[tar[0]][tar[1]] = piece

    # TODO: update value for 
    # self.isEnterTower = [False, False]
    # self.isKingMove = [False,False]
    # self.isRightRockMove = [False, False]
    # self.isLeftRockMove = [False, False]
    if piece.endswith(Rook.NOTATION):
      if pos[1] == 0:
        if player_color == "w":
          gs.isLeftRockMove[0] = True
        else: gs.isLeftRockMove[1] = True
      elif pos[1] == 7:
        if player_color == "w":
          gs.isRightRockMove[0] = True
        else: gs.isRightRockMove[1] = True
    elif piece.endswith(King.NOTATION):
      if isinstance(action, EnterTower):
        if player_color == "w":
          gs.isEnterTower[0] = True
        else: gs.isEnterTower[1] = True
      if player_color == "w":
          gs.isKingMove[0] = True
      else: gs.isKingMove[1] = True

    if isinstance(action, QueenPromote):
      board[tar[0]][tar[1]] = player_color + 'Q'
    elif isinstance(action, EnterTower):
      rPos = action.rPos
      rTar = action.rTar
      rPiece = piece = board[rPos[0]][rPos[1]]
      board[rPos[0]][rPos[1]] = ''
      board[rTar[0]][rTar[1]] = rPiece

    gameState = GameState(board, turn)
    gameState.isEnterTower = gs.isEnterTower
    gameState.isKingMove = gs.isKingMove
    gameState.isLeftRockMove = gs.isLeftRockMove
    gameState.isRightRockMove = gs.isRightRockMove
    
    return gameState
  

  def isTerminal(self, gs:GameState) -> bool:
    """
    Check if the function is terminal
    """  
    # Find the Kings and their positions
    return not self.actions(gs)
  

  def utility(self, gs:GameState, p:Turn) -> float:
    pass

  # def isCutOff(self, gs) -> float:



  def findPiecesById(self, gs:GameState, id: str) -> List[Tuple[int]]:
    """
    + id: "wQ"
    """
    pieces = []
    for i, row in enumerate(gs.board):
      for j, square in enumerate(row):
        if  square == id:
          pieces.append((i,j))
    return pieces

  def getValidMoves(self, gs: GameState, pos:Tuple[int]) -> List[Action]:
    row, col = pos
    board = gs.board
    piece = board[row][col]

    # First check if King is in endanger
    pieceSide, opponentTurn = (Turn.WHITE, Turn.BLACK) if piece[0] == "w" else (Turn.BLACK, Turn.WHITE)
    if piece == '' or gs.turn != pieceSide:
      return []
    kPos = self.findPiecesById(gs, f"{piece[0]}K")[0]
    isEndangered = self._isEndangered(gs, kPos, opponentTurn)
    if isEndangered:
      return self.getValidMovesOfAllPiecesWith(gs, isEndangered)

    pieceClass = self.pieceDict[piece[1]]
    if pieceClass == King:
      return pieceClass.getValidMoves(self, gs, pos)
    else:
      return pieceClass.getValidMoves(gs, pos)


