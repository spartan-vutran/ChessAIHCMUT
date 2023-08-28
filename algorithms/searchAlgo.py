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
        turn = self.game.toMove(gs)
        best_score = MinMaxAlgo.INFINITE if turn == Turn.BLACK else -MinMaxAlgo.INFINITE
        alpha, beta = -MinMaxAlgo.INFINITE, MinMaxAlgo.INFINITE
        count = 1

        print(f"===================Guess for=============================")
        print(f"============================================================")
        eval_value = Heuristic.eval(gs)
        
        print(self.game.board_to_string(gs.board))
        print(f"Its heuristic value:{eval_value}")
        for move in self.game.actions(gs):
            gsCopy = self.game.move(gs, move)

            if turn == Turn.BLACK:
                # print(f"===================Check move {count}========================")
                # print(self.game.board_to_string(gsCopy.board))
                # print(f"Current turn: {'White' if gsCopy.turn == Turn.WHITE else 'Black'}")
                score = self.maxValue(gsCopy, self.depth, alpha, beta)
                # print(f"===================Traceback to========================")
                # print(self.game.board_to_string(gsCopy.board))
                # print(f"Its heuristic value:{eval_value}")
                # print(f"Current best move:{best_move}")
                count += 1
                if (score < best_score): 
                    best_score = score
                    best_move = move
                    beta = min(beta, score)
                    
                    
            else: 
                score = self.minValue(gsCopy, self.depth, alpha, beta)
                if (score > best_score):
                    best_score = score
                    best_move = move
                    alpha = max(alpha, score)
            # print(score)

        return best_move
    

    def maxValue(self, gs: GameState, depth, alpha, beta):
        if (depth == 0): #or self.game.isTerminal(gs)
            return Heuristic.eval(gs)
        
        best_score = - MinMaxAlgo.INFINITE
        count = 1
        for move in self.game.actions(gs):
            newGs = self.game.move(gs, move)
            # print(f"===================Check move {count}========================")
            # print(self.game.board_to_string(newGs.board))
            # print(f"maxValue")
            # print(f"Current turn: {'White' if newGs.turn == Turn.WHITE else 'Black'}")

            score = self.minValue(newGs, depth-1, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            # print(f"===================Traceback to========================")
            # print(self.game.board_to_string(newGs.board))
            # print(f"Its heuristic value:{score}")
            # print(f"Current best score:{best_score}")
            # print(f"Alpha: {alpha} \t Beta: {beta}")
            count += 1
            if beta <= alpha:
                break  # Beta cutoff

        return best_score
    

    def minValue(self, gs: GameState, depth, alpha, beta):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = MinMaxAlgo.INFINITE
        gs = copy.deepcopy(gs)
        count = 1
        for move in self.game.actions(gs):
            newGs = self.game.move(gs, move)
            # print(f"===================Check move {count}========================")
            # print(self.game.board_to_string(newGs.board))
            # print(f"minValue")
            # print(f"Current turn: {'White' if newGs.turn == Turn.WHITE else 'Black'}")
            score = self.maxValue(newGs, depth-1, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, score)
            # print(f"===================Traceback to========================")
            # print(self.game.board_to_string(newGs.board))
            # print(f"Its heuristic value:{score}")
            # print(f"Current best score:{best_score}")
            # print(f"Alpha: {alpha} \t Beta: {beta}")
            count += 1
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
        turn = gs.turn
        best_score = MinMaxAlgo.INFINITE if turn == Turn.BLACK else -MinMaxAlgo.INFINITE
        
        for move in self.game.actions(gs):
            # if not self.game.checkValidMove(gsCopy, move):
            #     continue
            # eval_value = Heuristic.eval(gs)
            
            # print(self.game.board_to_string(gs.board))
            # print(eval_value)
            gsCopy = self.game.move(gs, move)
            # print(self.game.board_to_string(gsCopy.board))

            if turn == Turn.WHITE:
                score = self.minValue(gsCopy, self.depth)
                if (score > best_score):
                    best_score = score
                    best_move = move
            else: 
                score = self.maxValue(gsCopy, self.depth)
                if (score < best_score):
                    best_score = score
                    best_move = move
            # print(score)

        return best_move
    
    
    def maxValue(self, gs: GameState, depth):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = - MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            newGs = self.game.move(gs, move)

            score = self.minValue(newGs, depth-1)
            best_score = max(best_score, score)

        return best_score
    

    def minValue(self, gs: GameState, depth):
        if (depth == 0):
            return Heuristic.eval(gs)
        
        best_score = MinMaxAlgo.INFINITE
        for move in self.game.actions(gs):
            newGs = self.game.move(gs, move)

            score = self.maxValue(newGs, depth-1)
            best_score = min(best_score, score)

        return best_score