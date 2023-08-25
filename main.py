import argparse
from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState

def main():
  # parser = argparse.ArgumentParser(description='Mode games.')
  # parser.add_argument("-m", '--mode', choices=['personvspersion', 'personvsagent', 'agentvsagent'], default='personvsagent', help='Specify mode game to run')
  # args = parser.parse_args()
  
  # game = GameFrontEnd()
  # game.setUpPlayer(args.mode)
  # game.play()
  board = [
    ['','','','','','','',''],
    ['', 'bP','','','','','',''],
    ['','wR','wR','','','','',''],
    ['','','','','','','',''],
    ['','wP','','bP','wP','','',''],
    ['','','wB','','','','',''],
    ['', '','','wB','bP','','',''],
    ['bP', '','','','','','',''],
  ]
  turn = Turn.WHITE

  gs = GameState(board, turn)
  gc = GameController()

  gc.actions(gs)

if __name__ == '__main__':
  main()


