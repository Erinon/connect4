class Board:
    PLAYER_1 = 1
    PLAYER_2 = 2

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise Exception('Invalid width or height.')

        self.width = width
        self.height = height

        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.heights = [0 for _ in range(self.width)]

        self.turn = self.PLAYER_1

        self.winner = None

    def make_move(self, column):
        column -= 1
        
        if self.winner or column < 0 or column >= self.width or self.heights[column] >= self.height:
            return False

        self.heights[column] += 1

        self.board[-self.heights[column]][column] = self.turn

        self.change_turn()

        return True

    def change_turn(self):
        if self.turn == self.PLAYER_1:
            self.turn = self.PLAYER_2
        else:
            self.turn = self.PLAYER_1

    def __str__(self):
        return '\n'.join([' '.join([str(c) for c in r]) for r in self.board])

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    board = Board(7, 6)
    
    while True:
        print(board)
        board.make_move(int(input()))
