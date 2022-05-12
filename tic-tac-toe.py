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
        self.round_counter = 1

    def check_winner(self, player_move):
        '''
            check if there's any winner on the board; check through the rows and columns and diagonals
        '''

        #print("DEBUG: Checking for winner")

        winner = self.check_board_row(player_move=player_move)
        if winner:
            return winner

        winner = self.check_board_column(player_move=player_move)
        if winner:
            return winner

        winner = self.check_board_diagonals()
        if winner:
            return winner

    def is_board_filled(self):
        '''
         Check if board is filled
        '''

        return True if self.round_counter >= self.rows**2 else False

    def check_board_diagonals(self):
        '''
            check for a winner in the board diagonal
            Note: cell index starts at 1 as how it's displayed on the board
        '''
        winner_found = True
        winner = ''

        # getting left bottom cell
        left_buttom_cell_value = self.board[0]

        # DIRECTION left-second-bottom to top-right
        for i in range(self.rows - 2, -1, -1):
            cell_index = (self.rows - i) * self.rows - i

            if self.board[cell_index - 1] != left_buttom_cell_value:
                print("INFO: No winner in diagonal from left-bottom to top-right")
                winner_found = False
                break

        if winner_found:
            winner = left_buttom_cell_value
            print("INFO: Found winner in diagonal from left-bottom to top-right. Winner is ", winner)
            # TODO: uncomment below
            #return winner

        # DIRECTION bottom-right to top-left
        # resetting winner found boolean
        winner_found = True

        # getting right bottom cell
        right_bottom_cell_value = self.board[self.rows - 1]

        for i in range(self.rows - 1, -1, -1):
            cell_index = (i + 1) * self.rows - i

            if self.board[cell_index - 1] != right_bottom_cell_value:
                print("INFO: No winner in diagonal from right-bottom to top-left")
                winner_found = False
                break

        if winner_found:
            winner = right_bottom_cell_value
            print("INFO: Found winner in diagonal from right-bottom to top-left. Winner is ", winner)
            return winner

        return winner

    def check_board_row(self, player_move):
        '''
            checks the row of the move played to see if player is a winner
        '''

        # initialize winner
        winner = ''

        # define player, aka cell played value
        player = self.board[player_move-1]

        # define the cell number being checked
        cell_checked = player_move

        # define a counter that will help transition in the row from the cell checked
        adjacency_counter = 1

        # define a boolean to check if the row edge has been reached
        edge_reached = False

        # check the value of the adjacent cells within bounds of the row being checked
        for cell_counter in range(0, self.rows-1):
            # if cell being checked lies in the last column of the row
            # reset the cell checked to the cell played
            if cell_checked % self.rows == 0:
                edge_reached = True

            if edge_reached:
                adjacency_counter = -1
                cell_checked = player_move
                edge_reached = False

            # check if the cells on the right side of the cell played equals to player (cell played value)
            cell_checked = cell_checked + adjacency_counter
            cell_checked_value = self.board[cell_checked-1]

            if cell_checked_value != player:
                print("INFO: No winner found in row")
                return winner

        winner = player
        print("INFO: Found winner in the row. Winner is", winner)

        return winner

    def check_board_column(self, player_move):
        '''
            checks the column of the move played to see if player is a winner
        '''

        # initialize winner
        winner = ''

        # define player, aka cell played value
        player = self.board[player_move - 1]

        # define the cell number being checked
        cell_checked = player_move

        # define a counter that will help transition in the row from the cell checked
        adjacency_counter = -self.rows

        # define a boolean to check if the row edge has been reached
        edge_reached = False

        # check the value of the adjacent cells within bounds of the row being checked
        for cell_counter in range(0, self.rows - 1):
            # check if cell is in the first row of the column
            if cell_checked <= self.rows:
                edge_reached = True

            # if cell being checked lies in the first row of the column
            # reset the cell checked and flip the sign of adjacency counter to transition to the rows below player move
            if edge_reached:
                adjacency_counter = -1 * adjacency_counter
                cell_checked = player_move
                edge_reached = False

            # check if the value of adjacent cells is equal to player (cell played value)
            cell_checked = cell_checked + adjacency_counter
            cell_checked_value = self.board[cell_checked - 1]

            if cell_checked_value != player:
                print("INFO: No winner found in column")
                return winner

        winner = player
        print("INFO: Found winner in the column. Winner is", winner)

        return winner

    def display_board(self):
        '''
            Display the board appropriately, according to the num key pad
        '''

        # iterate over board and print its values
        # along with side (|) and lower lines (--)
        for cell_index in range(self.rows ** 2, 0, -self.rows):
            for cell_index_flipped in range(cell_index - self.rows + 1, cell_index + 1):
                # if reached the end of the row, don't print a side line
                if cell_index_flipped % self.rows == 0:
                    print('{:^7}'.format(self.board[cell_index_flipped - 1]))

                    # print lower lines as long as it's not last row
                    if not cell_index_flipped == self.rows:
                        for j in range(self.rows):
                            print('--------', end='')

                    print()
                    continue

                print('{:^7}|'.format(self.board[cell_index_flipped - 1]), end='')

    @staticmethod
    def create_board(rows):
        '''
            create board based on number of rows
        '''

        board = [str(i) for i in range(1, 1 + rows ** 2)]

        return board

    @staticmethod
    def get_number_in_range(input_message, max_num, min_num=0):
        '''
            Get a correct number in a specified range from user
        '''

        # get number from user
        while 1:
            try:
                # try to convert rows to an integer
                num = int(input(input_message))

                if num < min_num or num > max_num:
                    print("Error: number should be in range(" + str(min_num) +
                          ", " + str(max_num) + ")")
                    raise ValueError

                return int(num)

            except ValueError:
                # if number is invalid, display an error message
                print("Error: Please enter a valid number", file=sys.stderr)
                continue

    def switch_players(self, current_player):
        '''
            Switch the player turns
        '''
        return self.player2 if current_player == self.player1 else self.player1

    @classmethod
    def start(cls):
        '''
            Call this function to start using the class
        '''

        # display a welcoming message
        print("Welcome to Tic Tac Toe!\n\n" +
              "You can play using any number of rows in the range (" +
              str(TicTacToe.rows_min) + ", " + str(TicTacToe.rows_max) +
              "), inclusive of both.")

        # get number of board rows from player
        board_rows = TicTacToe.get_number_in_range(input_message="Enter the number of rows: ",
                                                   max_num=TicTacToe.rows_max,
                                                   min_num=TicTacToe.rows_min)

        # define a tic-tac-toe instance
        game = cls(rows=board_rows)

        # define the first player
        player = game.player1

        while 1:
            # ask player for their move
            player_move = TicTacToe.get_number_in_range(
                input_message="Player "+player+" - Enter a cell number: ",
                max_num=game.rows**2,
                min_num=1)

            # update board and display it
            game.board[player_move - 1] = player
            game.display_board()

            # once minimum amount of rounds are played, check if there's a winner or it's a tie
            if game.round_counter >= game.rows:
                board_filled = game.is_board_filled()
                if board_filled:
                    print("It's a tie! Good luck next time :p")
                    break

                winner = game.check_winner(player_move)

                # if winner found, declare winner and end game
                if winner:
                    print("CONGRATULATIONS PLAYER {}! You have won!".format(winner))
                    break

            game.round_counter += 1

            player = game.switch_players(current_player=player)

        print("Game Over")


def main():

    TicTacToe.start()

    return 0


# execute the main function when system starts
if __name__ == "__main__":
    main()


