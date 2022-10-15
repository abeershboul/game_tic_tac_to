import os
import time


class Player:

    def __init__(self, name,mark):
        self.name = name
        self.moves = 0
        self.mark = mark

class Bot:
    def __init__(self) -> None:
        pass

class GameLogic:

    """
    1. After the game starts a welcome message printed on the screen
    2. The users prompted to enter their names
    3. Then the board gets printed on the screen and player one starts
    4. The players must choose a spot between 1 and 9
    5. If the inputs invalid the user will be prompted again
    6. Once the user type their spot, the board will get updated
    7. Then we check if the game is finished or not
    8. If the game didn't finish, we switch turns
    9. We back to point (4)
    10. To exit the game, just type exit in your turn
    
    """

    def __init__(self):
        self.board =[["1",'2','3'],["4",'5','6'],['7','8','9']]
        self.player1 = None
        self.player2 = None
        self.currentPlayer = None
        self.is_Finished = False
        self.selected_spots = []
        self.game_result= None
        self.winner = None

    def welcome_message(self):
        os.system('clear')
        print("\n")
        print("==============================================")
        print("Hello! Welcome to Pam's Tic Tac Toe game!")
        print("\n")
        print("Rules: Player 1 and player 2, represented by X and O, take turns "
            "marking the spaces in a 3*3 grid. The player who succeeds in placing "
            "three of their marks in a horizontal, vertical, or diagonal row wins.")
        print("\n")
        print("To exit the game at any time, type: exit")
        print("==============================================")
        print("\n")
        input("Press enter to continue.")
        print("\n")
            
    def get_players(self):
        player1_name = input('Player 1 name : ')
        self.player1 = Player(player1_name,'x')
        player2_name = input('Player 2 name : ')
        self.player2 = Player(player2_name,'o')
        os.system('clear')
        self.currentPlayer = self.player1
        print(f'Players are : {self.player1.name} and {self.player2.name}')

    def print_baord(self):
        os.system('clear') # clear screen
        time.sleep(0.5) # delay 0.5 sec
        board = f"""
        Please Select an empty spot 

{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}
----------
{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}
----------
{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}

"""
        print(board)

    def get_input(self):
        userInput = input(f'Select your spot {self.currentPlayer.name} -> ')
        while True:

            if userInput.lower() == 'exit':
                self.quit_game()
            
            if self.validate_input(userInput):
                if self.isEmpty_spot(userInput):
                    break
                else:
                    userInput = input(f'Please Enter an open spot {self.currentPlayer.name} -> ') 
            else:
                userInput = input(f'Please Enter a valid spot {self.currentPlayer.name} -> ')
        return userInput

    def validate_input(self,input):

        try: 
            if int(input) > 0 and int(input) <= 9:
                return True
        except:
            return False

    def isEmpty_spot(self,input):
        if input in self.selected_spots:
            return False
        return True

    def update_board(self,user_input):
        """
        This function update 
        """
        board =[["1",'2','3'],["4",'5','6'],['7','8','9']]
        board[2][1]                         # 0   1   2
        # 0 1 2
        # 8
        user_input = int(user_input)
        if user_input > 6: # 7 8 9
            index = user_input - 7
            # 8 => 1
            # 7 => 0
            print(user_input)
            self.board[2][index] = self.currentPlayer.mark

        elif user_input >3: # 4 5 6
            index = user_input - 4
            # input - 4 = >2
            self.board[1][index] = self.currentPlayer.mark

        elif user_input <4: # 1 2 3
            index = user_input - 1
            self.board[0][index] = self.currentPlayer.mark
        self.currentPlayer.moves +=1        
        self.selected_spots.append(str(user_input))

    def check_for_winner(self):
        board = self.board
        self.print_baord()
        count =0
        for w in range(3):                              
            if board[1][1] == board[w][w]:
                count +=1
        if count == 3:
            self.game_result='Winner!'
            self.is_Finished=True
            self.winner = self.currentPlayer
            
        else:
            count =0

        dig= -1
        for y in range(3):
            if board[y][dig] == board[1][1]:
                count +=1
            dig -=1

        if count == 3:
            self.game_result='Winner!'
            self.is_Finished=True
            self.winner = self.currentPlayer
            
        else:
            count =0


        for y in range(3):
            # Check all rows 
            """
            board[?][0]
            baord[?][1]
            board[?][2]

            baord [0][?]
            baord [1][?]
            baord [2][?]

                0   1   2

            0   o | 2 | x
                ----------
            1   4 | x | 6
                ----------
            2   x | 8 | o
            """  
            first_in_row = board[y][0]    
            for x in range(3):
                if board[y][x] == first_in_row:
                    count += 1
            
            if count == 3:
                self.game_result='Winner!'
                self.is_Finished=True
                self.winner = self.currentPlayer
        
                break
            else:
                count =0
            
            # Check all columns 
            first_in_col = board[0][y]
            for j in range(3):
                if board[j][y] == first_in_col:
                    count += 1
            
            if count == 3:
                self.game_result='Winner!'
                self.is_Finished=True
                self.winner = self.currentPlayer
                
                break
            else:
                count =0
            
        if len(self.selected_spots) == 9 and self.winner == None:
                self.game_result='Draw!'
                self.is_Finished=True
                self.winner = None

    def switch_turns(self,player):
        if player == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def print_result(self):
        print(f"The game is finished")
        if self.winner == None:
            print(f'Game ended with draw')
        else:
            print(f'The winner is {self.winner.name} with {self.winner.moves} moves !')
    
    def quit_game(self):
        print(f"{self.currentPlayer.name} has quit the game!!")
        exit()

    def start(self):
        self.welcome_message()
        self.get_players()
        
        while True:
            self.print_baord()
            user_input = self.get_input()
            self.update_board(user_input)
            self.check_for_winner()
            if not self.is_Finished:
                self.switch_turns(self.currentPlayer)
            else:
                self.print_result()
                break

#game = GameLogic()
#game.start()

