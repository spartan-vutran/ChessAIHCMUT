import argparse
from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState, QueenPromote, EnterTower, Move
from logic.heuristic import Heuristic

def main():
  parser = argparse.ArgumentParser(description='Mode games.')
  parser.add_argument("-m", '--mode', choices=['personvspersion', 'personvsagent', 'agentvsagent'], default='personvspersion', help='Specify mode game to run')
  args = parser.parse_args()
  
  game = GameFrontEnd()
  game.setUpPlayer(args.mode)
  game.printInfoBoard()
  game.play()
  # board = [
  #   ['','','','','','','',''],
  #   ['', '','','','','','',''],
  #   ['','','','','','','',''],
  #   ['','','','','','','',''],
  #   ['','','bR','','','','',''],
  #   ['','','','','','','',''],
  #   ['', '','wQ','','','bK','',''],
  #   ['', '','wK','','','','',''],
  # ]
  # turn = Turn.BLACK

  # gs = GameState(board, turn)
  # # eval_value = Heuristic.eval(gs)
  # # print(eval_value)
  # gc = GameController()
  # # for action in gc.actions(gs):
  # #   print(f"{action.pos}\t{action.tar}")

  # # # print("Hello")
  # # # hello = gc.isTerminal(gs)
  # gc.checkValidMove(gs, Move((6,5), (2,3)))
  # print(hello)  

if __name__ == '__main__':
  main()


