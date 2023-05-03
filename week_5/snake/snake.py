import random
from time import sleep

class Board:
    def __init__(self, width, height, border='*'):
        self.width = width
        self.height = height
        self.boarder = border
        self.board = self.init_board()

    def init_board(self):
        board = []

        # for i in range(self.height):
        #     row = [''] * self.width
        #     board.append(row)

        # ['*', '*', '*', '*']
        # ['*', ' ', ' ', '*']
        # ['*', ' ', ' ', '*']
        # ['*', '*', '*', '*']

        for i in range(self.height):
            if i in {0, self.height - 1}:
                row = [self.boarder] * self.width
                board.append(row)
            else:
                row = []
                for j in range(self.width):
                    if j in {0, self.width - 1}:
                        row.append(self.boarder)
                    else:
                        row.append(' ')
                board.append(row)
        return board

    def show(self):
        for row in self.board:
            # print(row)
            print(' '.join(row))

    @staticmethod
    def distance(p1: tuple, p2: tuple):
        p1_i, p1_j = p1
        p2_i, p2_j = p2
        return ((p1_i - p2_i)**2+(p1_j - p2_j)**2)

class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]


    def eat(self, position: tuple):
        self.body.append(position)

    def move(self, position: tuple):
        del(self.body[0])
        self.body.append(position)

    def choices(self, i, j):
        self.i=i
        self.j=j
        choice = []
#        self.i, self.j = self.body[-1]
        if (self.i, (self.j+1)) not in self.body:
            choice.append((self.i, self.j+1))
        if ((self.j+1), self.j) not in self.body:
            choice.append((self.i+1, self.j))
        if ((self.j-1), self.j) not in self.body:
            choice.append((self.i-1, self.j))
        if (self.i, (self.j-1)) not in self.body:
            choice.append((self.i, self.j-1))
        return choice

class Apple:
    def __init__(self, symbol='$', position=(2, 2)):
        self.position = position
        self.symbol = symbol

class GameOverError(Exception):
    print

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        self.clear()
        # the easiest way to place snake's body on the board
        i, j = self.snake.body[0]
        self.board.board[i][j] = self.snake.symbol

        for i, j in self.snake.body:
            self.board.board[i][j] = self.snake.symbol

        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        self.board.show()

    def play(self):
        game_cycles = 5
        try:
            self.render()  # initial render of board, snake and apple
            while game_cycles > 0:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head
                next_move = None
                # TODO: find next possible position (next_move) for snake to move

                if self.snake.choices(snake_i, snake_j)[0]:
                    distance = self.board.distance(self.snake.choices(snake_i, snake_j)[0], self.apple.position)
                    next_move = self.snake.choices(snake_i, snake_j)[0]
                else:
                    next_move = None

                if self.snake.choices(snake_i, snake_j)[1]:
                    distance1 = self.board.distance(self.snake.choices(snake_i, snake_j)[1], self.apple.position)
                    if distance1 < distance:
                        distance = distance1
                        next_move = self.snake.choices(snake_i, snake_j)[1]
                    else:
                        next_move = self.snake.choices(snake_i, snake_j)[0]

                if self.snake.choices(snake_i, snake_j)[2]:
                    distance1 = self.board.distance(self.snake.choices(snake_i, snake_j)[2], self.apple.position)
                    if distance1 < distance:
                        distance = distance1
                        next_move = self.snake.choices(snake_i, snake_j)[2]
                    else:
                        next_move = self.snake.choices(snake_i, snake_j)[1]

                # if self.snake.choices(snake_i, snake_j)[3]:
                #     distance1 = self.board.distance(self.snake.choices(snake_i, snake_j)[3], self.apple.position)
                #     if distance1 < distance:
                #         next_move = self.snake.choices(snake_i, snake_j)[3]
                #     else:
                #         next_move = self.snake.choices(snake_i, snake_j)[2]


                if next_move is None:  # there is no possible move for snake
                    self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)
                if next_move == self.apple.position:
                    self.snake.eat(next_move)
                    self.render()
                    self.init_apple()
                    # TODO: eat apple, render this action, init new apple and render it on board
                    continue  # go to next game cycle
                # if game is not over, and snake did not eat the apple in current game cycle, then it means it can simply move on next valid position:
                self.snake.move(next_move)
                self.render()
                game_cycles -= 1
        except GameOverError:
            print('Game Over!')

    def clear(self):
        self.board = Board(self.width, self.height)

    def init_apple(self):
        last_position = self.apple.position
        new_i = random.randint(1, self.width)
        new_j = random.randint(1, self.height)
        try:
            if (new_i, new_j) not in self.snake.body:
                if (new_i, new_j) not in last_position:
                    self.apple = Apple(position=(new_i, new_j))
                    self.board.board[new_i][new_j] = self.apple.symbol
                    self.board.show()
        except GameOverError:
            print("No places for apple!")


if __name__ == '__main__':
    game = Game()
    game.play()
    # s=Snake()
    # print(s.choices(5,5))