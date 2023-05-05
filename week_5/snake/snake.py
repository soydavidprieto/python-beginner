import random
from board import Board
from board import Color
from time import sleep

class Snake:
    def __init__(self, head=(Color.PINK + '%' + Color.ENDC), symbol=(Color.OKGREEN + 'o' + Color.ENDC), tail=(Color.PINK + '~' + Color.ENDC), position=(1, 1)):
        self.symbol = symbol
        self.head = head
        self.tail = tail
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
    def __init__(self, symbol=(Color.FAIL + '@' + Color.ENDC), position=(2, 2)):
        self.position = position
        self.symbol = symbol

class GameOverError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def render(self):
        self.clear()
        i,j = self.snake.body[-1]
        self.board.board[i][j] = self.snake.head

        if len(self.snake.body) > 1:
            i, j = self.snake.body[0]
            self.board.board[i][j] = self.snake.tail

        for i, j in self.snake.body[1:-1]:
            self.board.board[i][j] = self.snake.symbol

        i, j = self.apple.position
        self.board.board[i][j] = self.apple.symbol

        self.board.show()

    def play(self):
        try:
            self.render()  # initial render of board, snake and apple
            while True:  # start our game
                snake_i, snake_j = self.snake.body[-1]  # remember last position of snake's head
                choices = self.snake.choices(snake_i, snake_j)
                # TODO: find next possible position (next_move) for snake to move
                filtered_choices = []
                if choices:
                    for i in choices:
                        if all(j != 0 for j in i) or all(j != self.width for j in i) or all(j != self.height for j in i):
                            filtered_choices.append(i)

                if filtered_choices:
                    distance = self.board.distance(filtered_choices[0], self.apple.position)
                    next_move = filtered_choices[0]
                    for i, tuple in enumerate(filtered_choices):
                        distance1 = self.board.distance(filtered_choices[i], self.apple.position)
                        if distance1 < distance:
                            distance = distance1
                            next_move = filtered_choices[i]
                else:
                    next_move = None

                if next_move is None:  # there is no possible move for snake
                    self.snake.move((snake_i + 1, snake_j + 1))  # just do one move forward for snake
                    self.render()  # render last move
                    raise GameOverError('No moves for snake!')  # end the game (snake does not have next valid move)

                if next_move == self.apple.position:
                    self.snake.eat(next_move)
                    self.render()
                    self.init_apple()
                    self.render()
                    # TODO: eat apple, render this action, init new apple and render it on board
                    continue  # go to next game cycle
                # if game is not over, and snake did not eat the apple in current game cycle, then it means it can simply move on next valid position:
                self.snake.move(next_move)
                self.render()

        except GameOverError:
            print('Game Over!')

    def clear(self):
        self.board = Board(self.width, self.height)

    def init_apple(self):
        last_position = self.apple.position
        new_i = random.randint(1, self.width-2)
        new_j = random.randint(1, self.height-2)
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
