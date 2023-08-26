import argparse
from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState
from logic.heuristic import Heuristic

def main():
  # parser = argparse.ArgumentParser(description='Mode games.')
  # parser.add_argument("-m", '--mode', choices=['personvspersion', 'personvsagent', 'agentvsagent'], default='personvspersion', help='Specify mode game to run')
  # args = parser.parse_args()
  
  # game = GameFrontEnd()
  # game.setUpPlayer(args.mode)
  # game.printInfoBoard()
  # game.play()
  board = [
    ['','','','','','','',''],
    ['', '','','','','wK','',''],
    ['','','','','','','',''],
    ['wB','','bK','wQ','','','',''],
    ['wB','wP','','','','','',''],
    ['','','','wP','','','',''],
    ['', '','','','','','',''],
    ['', '','','','','','',''],
  ]
  turn = Turn.BLACK

  gs = GameState(board, turn)
  eval_value = Heuristic.eval(gs)
  print(eval_value)
  # gc = GameController()

  # gc.actions(gs)

if __name__ == '__main__':
  main()


