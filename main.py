from frontend.game import GameFrontEnd
from logic.game import GameController
from logic.attributes import Turn, GameState



if __name__ == '__main__':
  # game = GameFrontEnd()
  # game.play()

  board = [
    ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
    ['', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
    ['bP','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['','','','','','','',''],
    ['', 'wQ','','','','','',''],
    ['', '','','','','','',''],
  ]
  turn = Turn.WHITE

  gs = GameState(board, turn)
  gc = GameController()

  gc.actions(gs)

