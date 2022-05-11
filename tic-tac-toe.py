import sys

class TicTacToe:
    rows_min = 3
    rows_max = 10
    
    def __init__(self, rows=rows_min):
        self.rows = rows
        self.board = TicTacToe.create_board(rows)
        self.display_board()

        self.player1 = 'X'
        self.player2 = 'O'

    def check_winner(self):
        print("DEBUG: Checking for winner")

        self.check_board_diagonals()

        return True
        self.check_rows()

    def check_board_diagonals(self):
        '''
            check for a winner in the board diagonal
            Note: cell index starts at 1 as how it's displayed on the board
        '''
        winner_found = True
        winner = ''

        # getting left bottom cell
        left_bottom_cell_index = self.rows * self.rows - (self.rows - 1)
        left_buttom_cell_value = self.board[left_bottom_cell_index - 1]

        # direction left bottom+1 -> top right
        for i in range(self.rows-2, -1, -1):
            cell_index = (i+1) * self.rows - i

            if self.board[cell_index - 1] != left_buttom_cell_value:
                print("INFO: No winner in diagonal from left-bottom till top-right")
                winner_found = False
                break

        if winner_found:
            winner = left_buttom_cell_value
            print("INFO: Found winner in diagonal from left-bottom till top-right. Winner is ", winner)
        # direction

    def check_rows(self):
        # initialize first cell move in the row
        first_cell_move = self.board.get(str(1))

        row_counter = 1

        for cell_num in range(2, self.rows**2):
            # if first_move != self.board.get(str(cell_num))

            if cell_num % self.rows == 0:
                print("DEBUG: No winner found in cell number ", cell_num)
                row_counter += 1
                return False

    def display_board(self):
        # iterate over board and print its values
        # along with side (|) and lower lines (--)
        for i in range(1, 1+self.rows**2):
            # if reached the end of the row, don't print a side line
            if i % self.rows == 0:
                print('{:^7}'.format(self.board[i-1]))

                # print lower lines as long as it's not last row
                if not i == self.rows**2:
                    for j in range(self.rows):
                        print('--------', end='')

                print()
                continue
            
            print('{:^7}|'.format(self.board[i-1]), end='')

    def display_initial_board(self):
        # iterate over board dict and print cell numbers
        # along with side (|) and lower lines (--)
        for i in range(1, 1+self.rows**2):
            # if reached the end of the row, don't print a side line
            if i % self.rows == 0:
                print('{:^7}\t'.format(i))

                # print lower lines as long as it's not last row
                if not i == self.rows**2:
                    for j in range(self.rows):
                        print('--------', end='')

                print()
                continue
            
            print('{:^7}|'.format(i), end='')
    
    # create board based on number of rows
    @staticmethod
    def create_board(rows):
        board = [str(i) for i in range(1, 1+rows**2)]

        return board

    @staticmethod
    def get_number_in_range(input_message, max_num, min_num=0):
        # get number from user
        while 1:
            try:
                # try to convert rows to an integer
                num = int(input(input_message))

                if num < min_num or num > max_num:
                    print("Error: number should be in range("+ str(min_num)+
                          ", "+ str(max_num)+ ")")
                    raise ValueError

                return int(num)

            except ValueError:
                # if number is invalid, display an error message
                print("Error: Please enter a valid number", file=sys.stderr)
                continue

    @classmethod
    def start(cls):
        # call this function to start using the class

        # display a welcoming message
        print("Welcome to Tic Tac Toe!\n\n"+
              "You can play using any number of rows in the range ("+
              str(TicTacToe.rows_min)+ ", "+ str(TicTacToe.rows_max)+
              "), inclusive of both.")

        # get number of board rows from user
        board_rows = TicTacToe.get_number_in_range(input_message="Enter the number of rows: ",
                                                   max_num=TicTacToe.rows_max,
                                                   min_num=TicTacToe.rows_min)

        # initialize tic-tac-toe instance
        game = cls(rows=board_rows)

        # initialize first player
        player = game.player1

        # initialize round_counter
        round_counter = 1

        while 1:
            # ask player for move
            player_move = TicTacToe.get_number_in_range(input_message="Enter the cell number: ",
                                                        max_num=TicTacToe.rows_max,
                                                        min_num=1)
            # update board and display it
            game.board[player_move-1] = player
            game.display_board()

            # if round counter > minimum board row number, check for a winner
            if round_counter >= game.rows:
                winner_found = game.check_winner()

                # if winner found, declare winner and exit function

            round_counter += 1


TicTacToe.start()

'''
TODO:
- 

'''
            
            
    
