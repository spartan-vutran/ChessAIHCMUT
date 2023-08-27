from logic.attributes import Turn, GameState, Action, Move, QueenPromote, EnterTower
from .heuristic import Heuristic
from logic.game import GameController
import copy

class SearchAlgo:
    def __init__():
      pass
    
    def searchMove(gs: GameState) -> Action:
        pass

class AlphaBetaAlgo(SearchAlgo):
    INFINITE = 10000000
    def __init__(self, depth = 2):
       self.game = GameController()
       self.depth = depth

    def searchMove(self, gs: GameState) -> Action:
        best_move = None
        best_score = -MinMaxAlgo.INFINITE
        turn = gs.turn
        
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            if not self.game.checkValidMove(gs, move):
                continue
            eval_value = Heuristic.eval(gs)
            
            print(self.game.board_to_string(gs.board))
            print(eval_value)
            gs = self.game.move(gs, move)
            print(self.game.board_to_string(gs.board))

            if gs.turn == Turn.WHITE:
                score = self.maxValue(gs, self.depth, -MinMaxAlgo.INFINITE, MinMaxAlgo.INFINITE)
                if (score > best_score):
                    best_score = score
                    best_move = move
            else: 
                score = self.minValue(gs, self.depth, -MinMaxAlgo.INFINITE, MinMaxAlgo.INFINITE)
                if (score < best_score):
                    best_score = score
                    best_move = move
            print(score)

        return best_move
    
    def maxValue(self, gs: GameState, depth, alpha, beta):
        if (depth == 0): #or self.game.isTerminal(gs)
            return Heuristic.eval(gs)
        
        best_score = - MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            self.game.move(gs, move)

            score = self.minValue(gs, depth-1, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break  # Beta cutoff

        return best_score
    
    def minValue(self, gs: GameState, depth, alpha, beta):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            self.game.move(gs, move)

            score = self.maxValue(gs, depth-1, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break  # Alpha cutoff

        return best_score
    
class MinMaxAlgo(SearchAlgo):
    INFINITE = 10000000
    def __init__(self, depth = 2):
       self.game = GameController()
       self.depth = depth

    def searchMove(self, gs: GameState) -> Action:
        best_move = None
        best_score = -MinMaxAlgo.INFINITE
        turn = gs.turn
        
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            if not self.game.checkValidMove(gs, move):
                continue
            eval_value = Heuristic.eval(gs)
            
            print(self.game.board_to_string(gs.board))
            print(eval_value)
            gs = self.game.move(gs, move)
            print(self.game.board_to_string(gs.board))

            if gs.turn == Turn.WHITE:
                score = self.maxValue(gs, self.depth)
                if (score > best_score):
                    best_score = score
                    best_move = move
            else: 
                score = self.minValue(gs, self.depth)
                if (score < best_score):
                    best_score = score
                    best_move = move
            print(score)

        return best_move
    
    def maxValue(self, gs: GameState, depth):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = - MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            self.game.move(gs, move)

            score = self.minValue(gs, self.depth-1)
            best_score = max(best_score, score)

        return best_score
    
    def minValue(self, gs: GameState, depth):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            gs = copy.deepcopy(gs)
            self.game.move(gs, move)

            score = self.maxValue(gs, self.depth-1)
            best_score = min(best_score, score)

        return best_score