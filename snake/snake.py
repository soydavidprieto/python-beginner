import os
from time import sleep


class Board:
    def __init__(self, width: int = 40, height: int = 20, border: str = '*') -> None:
        self.board = self.init_board(width, height, border)

    @staticmethod
    def init_board(width: int, height: int, border: str):
        board = []
        for i in range(height):
            if i in {0, height - 1}:
                board.append([border] * width)
            else:
                board.append([])
                for j in range(width):
                    if j in {0, width - 1}:
                        board[i].append(border)
                    else:
                        board[i].append(' ')
        return board

    def show(self):
        for row in self.board:
            print(' '.join(row))

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return abs(pow((p2_i - p1_i) ** 2 + (p2_j - p1_j) ** 2, 0.5))


class Snake:
    def __init__(self, symbol: str = 'o', position: tuple = (1, 1)) -> None:
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        assert position, f'Snake needs something to eat!'
        self.body.append(position)

    def move(self, position: tuple):
        assert position, f'Snake needs somewhere to move!'
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        # next possible positions
        i, j = self.body[-1]
        options = {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}
        positions = {p for p in options if p not in self.body}
        if not positions:
            raise GameOverError('Snake can\'t move further!')
        return positions


class Apple:
    def __init__(self, symbol: str = '$', position: tuple = (2, 2)):
        self.position = position
        self.symbol = symbol


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width: int = 10, height: int = 10) -> None:
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        self.clear()

        # render apple
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        # render snake
        for position in self.snake.body:
            i, j = position
            self.board.board[i][j] = self.snake.symbol

        self.board.show()
        sleep(2)

    def clear(self):
        self.board = Board(self.width, self.height)
        # clear console
        if os.name == 'nt':
            # windows
            os.system('cls')
        else:
            os.system('clear')

    def init_apple(self):
        last_position = self.apple.position if self.apple else None
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if (i, j) not in self.snake.body:
                    self.apple = Apple(position=(i, j))
                    break
        if last_position is None:
            return
        if last_position == self.apple.position:
            raise GameOverError('No places for apple!')

    def play(self):
        game_cycles = 150
        try:
            self.render()
            while game_cycles > 0:
                snake_i, snake_j = self.snake.body[-1]

                next_move = None
                for possible_move in self.snake.choices():
                    if possible_move == self.apple.position:
                        next_move = self.apple.position
                        break

                    i, j = possible_move
                    if i in {0, self.height - 1} or j in {0, self.width - 1}:
                        # border
                        continue

                    if next_move is None:
                        next_move = possible_move
                        continue

                    d1 = self.board.distance(next_move, self.apple.position)
                    d2 = self.board.distance(possible_move, self.apple.position)
                    if d2 < d1:
                        next_move = possible_move

                if next_move is None:
                    self.snake.move((snake_i + 1, snake_j + 1))
                    self.render()
                    raise GameOverError('No moves for snake!')

                if next_move == self.apple.position:
                    self.snake.eat(self.apple.position)
                    self.render()
                    self.init_apple()
                    self.render()
                    continue

                self.snake.move(next_move)
                self.render()
                game_cycles -= 1

        except GameOverError as e:
            print('Game Over!')
            print(e)


if __name__ == '__main__':
    # TODO: run via terminal for proper rendering
    game = Game()
    game.play()
