class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.turn_count = 0
        self.marks = ['x', 'o']
        self.emptyMark = '-'
        self.table = [[self.emptyMark,self.emptyMark,self.emptyMark],
                      [self.emptyMark,self.emptyMark,self.emptyMark],
                      [self.emptyMark,self.emptyMark,self.emptyMark]]
        self.player = 0

    def encode(self):
        table = self.table
        s = ""
        for i in range(3):
            for j in range(3):
                s += table[i][j]
        return s 
    
    def string(self):
        table = self.table
        s = ""
        for i in range(3):
            for j in range(3):
                s += table[i][j]
            s+= '\n'
        return s 
    
    def isEmpty(self, posX, posY):
        return self.table[posY][posX] == self.emptyMark

    def mark(self, posX, posY):
        if self.isEmpty(posX, posY):
            self.table[posY][posX] = self.marks[self.player]
            self.player = 1 if self.player == 0 else 0
            self.turn_count += 1
            return True
        else:
            return False

    def winner(self):
        table = self.table

        # ___
        # ___
        # ___
        if table[0][0] == table[0][1] == table[0][2] != self.emptyMark:
            return table[0][0]
        if table[1][0] == table[1][1] == table[1][2] != self.emptyMark:
            return table[1][0]
        if table[2][0] == table[2][1] == table[2][2] != self.emptyMark:
            return table[2][0]
        
        # |||
        # |||
        # |||
        if table[0][0] == table[1][0] == table [2][0] != self.emptyMark:
            return table[0][0]
        if table[0][1] == table[1][1] == table [2][1] != self.emptyMark:
            return table[0][1]
        if table[0][2] == table[1][2] == table [2][2] != self.emptyMark:
            return table[0][2]

        # \-- 
        # -\-
        # --\
        if table[0][0] == table[1][1] == table[2][2] != self.emptyMark:
            return table[0][0]
        if table[0][2] == table[1][1] == table[2][0] != self.emptyMark:
            return table[0][2]
        
        # no win
        return self.emptyMark

    def notFinished(self):
        return self.turn_count < 9 and self.winner() == '-'

    def Render(encode):
        game = TicTacToe()
        for i in range(3):
            for j in range(3):
                game.table[i][j] = encode[i*3+j:i*3+j+1]
        return game