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

    def draw_snake(self, snake):
        for snake_point in snake.body:
            i, j = snake_point
            self.board[i][j] = snake.symbol

    def draw_apple(self, apple):
        if apple.visible:
            i, j = apple.position
            self.board[i][j] = apple.symbol

    def show(self):
        for row in self.board:
            # print(row)
            print(' '.join(row))

    def clear_board(self):
        self.board = self.init_board()


class Snake:
    def __init__(self, symbol='o', position=(1, 1)):
        self.symbol = symbol
        self.body = [position]

    def eat(self, apple):
        # TODO: this method should append new position to snake's body
        self.body.append(apple.position)

    def move(self, position: tuple):

        # TODO: this method should move snake's body by one step forward,
        # by means append to the body next position and
        # pop from the body the position at 0 index at the same time.
        self.body.append(position)
        self.body.pop(0)

    def choices(self, board_width=1, board_height=1):

        # TODO: this method should return set of next possible positions
        # where snake can move based on it's current position.
        # Note: if next possible position is already in snake body, filter it out.
        x, y = self.body[-1]

        allowed_steps = []
        if x < board_width - 1:
            point = (x + 1, y)
            if point not in self.body:
                allowed_steps.append(point)
            # else:
            #     print("Body contains:" + str(x+1) + "," + str(y))

        if x > 0:
            point = (x - 1, y)
            if point not in self.body:
                allowed_steps.append(point)
            # else:
            #     print("Body contains:" + str(x - 1) + "," + str(y))

        if y < board_height - 1:
            point = (x, y + 1)
            if point not in self.body:
                allowed_steps.append(point)
            # else:
            #     print("Body contains:" + str(x) + "," + str(y+1))

        if y > 0:
            point = (x, y-1)
            if point not in self.body:
                allowed_steps.append(point)
            # else:
            #     print("Body contains:" + str(x) + "," + str(y-1))

        return allowed_steps

class Apple:
    def __init__(self, symbol='$', position=(2, 2), visible=True):
        self.position = position
        self.symbol = symbol
        self.visible = visible

    def show(self, position: tuple):
        self.visible = True
        self.position = position

    def hide(self):
        self.visible = False

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(self.width, self.height)
        self.snake = Snake()
        self.apple = Apple()

    def clear(self):
        # TODO: should clear the board to initial state.
        self.board.clear_board()

    def play(self):
        self.apple.show(position=(2, 3))

        self.snake.move(position=(1, 2))
        self.render()

        self.snake.move(position=(2, 2))
        self.render()

        self.snake.eat(self.apple)
        self.apple.hide()
        self.render()

        self.apple.show(position=(4, 6))

        self.snake.move((2, 4))
        self.render()

        self.snake.move((2, 5))
        self.render()

        self.snake.move((2, 6))
        self.render()

        self.snake.move((3, 6))
        self.render()

        self.snake.eat(self.apple)
        self.apple.hide()
        self.render()

        self.apple.show(position=(8, 10))
        self.render()


        #print(self.snake.choices(self.board.width, self.board.height))

    def render(self):

        self.clear()

        self.board.draw_apple(self.apple)

        self.board.draw_snake(self.snake)

        self.board.show()

        sleep(2)


if __name__ == '__main__':
    game = Game()
    game.play()
