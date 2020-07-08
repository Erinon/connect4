from enum import Enum


class Board:
    PLAYER_1 = 1
    PLAYER_2 = -1
    EMPTY = 0
    
    PLAYER_1_STR = 'X'
    PLAYER_2_STR = 'O'
    EMPTY_STR = '_'
    
    WINNER_1 = 1
    WINNER_2 = -1
    DRAW = 0
    PROGRESS = 2

    def __init__(self, width, height, target=4):
        if target < 2:
            raise Exception('target < 2')
        
        if width < target or height < target:
            raise Exception('width or height < target')
        
        self.target = target
        
        self.width = width
        self.height = height
        
        self.max_moves = width * height
        self.moves = 0

        self.board = [[Board.EMPTY for _ in range(self.width)] for _ in range(self.height)]
        self.heights = [0 for _ in range(self.width)]

        self.turn = self.PLAYER_1
        
        self.status = self.PROGRESS
    
    def make_move(self, column):
        column -= 1
        
        if self.status != Board.PROGRESS or column < 0 or column >= self.width or self.heights[column] >= self.height:
            return False

        self.heights[column] += 1

        self.board[-self.heights[column]][column] = self.turn

        self.change_turn()
        
        self.moves += 1
        
        self.check_status()

        return True

    def change_turn(self):
        if self.turn == Board.PLAYER_1:
            self.turn = Board.PLAYER_2
        else:
            self.turn = Board.PLAYER_1
    
    def check_status(self):
        if self.status != Board.PROGRESS:
            return
        
        # check rows
        for i in range(self.height):
            for j in range(self.width - self.target + 1):
                target = self.board[i][j]
                
                if target == Board.EMPTY:
                    continue
                
                found = True
                for k in range(j+1, j+self.target):
                    if self.board[i][k] != target:
                        found = False
                        break
                
                if found:
                    self.status = Board.player_to_winner(target)
                    return
        
        # check columns
        for j in range(self.width):
            for i in range(self.height - self.target + 1):
                target = self.board[i][j]
                
                if target == Board.EMPTY:
                    continue
                
                found = True
                for k in range(i+1, i+self.target):
                    if self.board[k][j] != target:
                        found = False
                        break
                
                if found:
                    self.status = Board.player_to_winner(target)
                    return
        
        # check diagonal rising to the right
        for i in range(self.height - self.target + 1):
            for j in range(self.target - 1, self.width - 1):
                target = self.board[i][j]
                
                if target == Board.EMPTY:
                    continue
                
                found = True
                for k in range(1, self.target):
                    if self.board[i+k][j-k] != target:
                        found = False
                        break
                
                if found:
                    self.status = Board.player_to_winner(target)
                    return
        
        # check diagonal rising to the left
        for i in range(self.height - self.target + 1):
            for j in range(self.width - self.target + 1):
                target = self.board[i][j]
                
                if target == Board.EMPTY:
                    continue
                
                found = True
                for k in range(1, self.target):
                    if self.board[i+k][j+k] != target:
                        found = False
                        break
                
                if found:
                    self.status = Board.player_to_winner(target)
                    return
        
        # check draw
        if self.moves == self.max_moves:
            self.status = self.DRAW
    
    def get_status(self):
        return self.status
    
    def player_to_winner(player):
        if player == Board.PLAYER_1:
            return Board.WINNER_1
        else:
            return Board.WINNER_2
    
    def cell_to_string(cell):
        if cell == Board.PLAYER_1:
            return Board.PLAYER_1_STR
        elif cell == Board.PLAYER_2:
            return Board.PLAYER_2_STR
        else:
            return Board.EMPTY_STR

    def __str__(self):
        return '\n'.join([' '.join([Board.cell_to_string(c) for c in r]) for r in self.board])

    def __repr__(self):
        return self.__str__()

