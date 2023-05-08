from time import sleep
import random
import math


class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.border = border
        self.board = self.init_board()

    def init_board(self):
        board = []

        # for i in range(self.height):
        #     row = [''] * self.width
        #     board.append(row)

        # ['', '', '', '']
        # ['', ' ', ' ', '']
        # ['', ' ', ' ', '']
        # ['', '', '', '']

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.border] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.border)
                    else:
                        row.append(' ')
                board.append(row)
        return board

    def show(self):
        for row in self.board:
            # print(row)
            print(' '.join(row))

    def clear_board(self):
        self.board = self.init_board()

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return math.sqrt(math.pow(p2_i - p1_i, 2) +
                         math.pow(p2_j - p1_j, 2) * 1.0)  # `TODO: place formula here`


class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        # by means append to the body next position and
        # pop from the body the position at 0 index at the same time.
        self.body.append(position)
        self.body.pop(0)

    def choices(self):
        # TODO: this method should return set of next possible positions
        # where snake can move based on it's current position.
        # Note: if next possible position is already in snake body, filter it out.
        i, j = self.body[-1]
        choice = []
        if ((i + 1), j) not in self.body and i < (game.width - 2):
            choice.append((i + 1, j))
        if (i, (j + 1)) not in self.body and j < (game.height - 2):
            choice.append((i, j + 1))
        if ((i - 1), j) not in self.body and i > 1:
            choice.append((i - 1, j))
        if (i, (j - 1)) not in self.body and j > 1:
            choice.append((i, j - 1))
        return choice


class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol

    def show(self, position: tuple):
        self.position = position


class GameOverError(Exception):
    pass


class Game:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def init_apple(self):
        last_position = self.apple.position
        possible_positions = []
        for new_i in range(1, (self.width - 1)):
            for new_j in range(1, (self.height - 1)):
                new_position = (new_i, new_j)
                if new_position == last_position or new_position in self.snake.body:
                    continue
                else:
                    possible_positions.append(new_position)
        if len(possible_positions) == 0:
            raise GameOverError('No places for apple!')
        else:
            position = random.choice(possible_positions)
            self.apple = Apple(position=position)
            self.board.show()
        # TODO:
        # if we can find new place where we can set new apple on the board (new_i, new_j), re-create an apple on that position
        # self.apple = Apple(position=(new_i, new_j))
        # Notes:
        # 1. this new position should not overlap with snake body
        # 2. this new position should not overlap with the last position of an apple
        # 3. if we can't find new position for an apple it means our game is over, so raise custom exception in that case (just place it as is in the code):
        #  raise GameOverError('No places for apple!')

    def play(self):
        game_cycles = 30
        try:
            self.render()  # initial render of board, snake and apple
            while game_cycles > 0:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head

                # TODO: find next possible position (next_move) for snake to move
                possible_positions = self.snake.choices()
                if len(possible_positions) == 0:
                    next_position = None
                else:
                    # next_move = random.choice(possible_positions)
                    actual_distance = Board.distance(self.apple.position, self.snake.body[-1])
                    for x in range(len(possible_positions)):
                        next_distance = Board.distance(self.apple.position, possible_positions[x])
                        if next_distance < actual_distance and possible_positions[x] not in self.snake.body:
                            next_position = possible_positions[x]

                next_move = next_position

                if next_move is None:  # there is no possible move for snake
                    self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                if next_move == self.apple.position:
                    # TODO: eat apple, render this action, init new apple and render it on board
                    self.snake.eat(self.apple.position)
                    # self.render()
                    self.init_apple()
                    self.render()
                    continue  # go to next game cycle
                # if game is not over, and snake did not eat the apple in current game cycle, then it means it can simply move on next valid position:
                self.snake.move(next_move)
                self.render()
                game_cycles -= 1
        except GameOverError:
            print('Game Over!')

    def clear(self):
        self.board.clear_board()

    def render(self):
        self.clear()
        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol
        for (x, y) in self.snake.body:
            self.board.board[x][y] = self.snake.symbol
        self.board.show()
        sleep(1)


if __name__ == '__main__':
    game = Game()
    game.play()