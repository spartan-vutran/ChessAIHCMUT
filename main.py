import argparse
from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState, QueenPromote, EnterTower
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
    ['','wR','','','bK','bP','',''],
    ['', '','','','bP','bP','',''],
    ['','','wB','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['', '','','','','','',''],
    ['', '','','','wK','','',''],
  ]
  turn = Turn.BLACK

  gs = GameState(board, turn)
  # eval_value = Heuristic.eval(gs)
  # print(eval_value)
  gc = GameController()

  gc.actions(gs)

  # gc.checkValidMove(gs, EnterTower((0,4),(0,2),(0,0),(0,3)))

if __name__ == '__main__':
  main()


