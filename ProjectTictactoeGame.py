import random
print("       Welcome to Tic Tac Toe made by Ahmad/Roll number 44")
print()
print("            Numbering of the boxes is as follows: ")
print()
print("                         ","1|2|3 \n                          4|5|6 \n                          7|8|9")
print()
continuegame = "m"
while continuegame == "m":
  game_type = input("1. If you want to play Player vs Player(Multiplayer), enter 'p'.\n2. If you want to play Player vs Computer, enter 'c'.\n3. Enter any other button to exit.\nEnter your choice: ")
  print()
  if game_type == "p" or game_type == "P":
    continuepvp = "y"
    while continuepvp == "y":
      mode = input("If you want to play only 1 game, enter 's'.\nIf you want to play a tournament, enter 't'.\nEnter your choice: ")
      print()
      p = 0
      p1 = 0
      p2 = 0
      
      def pvp():
            
            board = ["-","-","-",
                     "-","-","-",
                     "-","-","-"]

            def display_board():
              print("                         ",board[0] + "|" + board[1] +  "|" + board[2])
              print("                         ",board[3] + "|" + board[4] +  "|" + board[5])
              print("                         ",board[6] + "|" + board[7] +  "|" + board[8])
            #main function
            def main():

            #display initial board
              display_board()
            #while game is still being played
              while game_still_playing:
              #handling the ongoing on turn
                play_turn(current_player)
                
              #change the turn
                change_player()
            
              #check if game is over i.e someone has won or game has tied.
                winner_check()


              #game ended
              if winner == "X":
                global p1
                print()
                print("                  ",player1,"has won the game.")
                print()
                p1 += 1
              if winner == "O":
                global p2
                print()
                print("                  ",player2,"has won the game.")
                print()
                p2 += 1
              elif winner == None:
                global p
                print()
                print("                   This game is a Tie.")
                print()
                p += 1
            #handle a single turn
            def play_turn(player):
              print()
              print("                      ",player,"'s turn.")
              print()
              position = input("               Choose a position from 1-9: ")
              print()

              valid = False
              while not valid:
                #if someone enters a number other than 1-9 or enters any string
                while position not in ["1","2","3","4","5","6","7","8","9"]:
                  position = input("Invalid position. Choose another position: ")
                position = int(position) - 1

                if board[position] == "-":
                  valid = True
                else:
                  #if someone enters an already occupied number/position
                  print("Position is already occupied. Try again!")


              board[position] = player


              display_board()
              

            def winner_check():
              global game_still_playing
              
              global winner
              
              if (board[0] == "X" and board[1] == "X" and board[2] == "X" or # across the top
                  board[3] == "X" and board[4] == "X" and board[5] == "X" or # across the middle
                  board[6] == "X" and board[7] == "X" and board[8] == "X" or # across the bottom
                  board[0] == "X" and board[3] == "X" and board[6] == "X" or # down the left side
                  board[1] == "X" and board[4] == "X" and board[7] == "X" or # down the middle
                  board[2] == "X" and board[5] == "X" and board[8] == "X" or # down the right side
                  board[0] == "X" and board[4] == "X" and board[8] == "X" or # diagonal
                  board[2] == "X" and board[4] == "X" and board[6] == "X"):  # diagonal
                    winner = "X"
                    game_still_playing = False
              elif (board[0] == "O" and board[1] == "O" and board[2] == "O" or # across the top
                  board[3] == "O" and board[4] == "O" and board[5] == "O" or # across the middle
                  board[6] == "O" and board[7] == "O" and board[8] == "O" or # across the bottom
                  board[0] == "O" and board[3] == "O" and board[6] == "O" or # down the left side
                  board[1] == "O" and board[4] == "O" and board[7] == "O" or # down the middle
                  board[2] == "O" and board[5] == "O" and board[8] == "O" or # down the right side
                  board[0] == "O" and board[4] == "O" and board[8] == "O" or # diagonal
                  board[2] == "O" and board[4] == "O" and board[6] == "O"):  # diagonal
                    winner = "O"
                    game_still_playing = False

              else:
                  check_tie()


            
            def check_tie():
              global game_still_playing
              if "-" not in board:
                game_still_playing = False

              return
            #to change the the turn to next player
            def change_player():
              global current_player
              if current_player == "X":
                current_player = "O"
              elif current_player == "O":
                current_player = "X"
              return

            main()
            
      if mode == "t":
        
        no_of_games = eval(input("Enter the number of games you want to play in tournament: "))
        print()
        i = 0
        player1 = input("Enter the name of first player: ")
        player2 = input("Enter the name of second player: ")
        while i != no_of_games:
          
          game_still_playing = True
          winner = None
          print()
          print("           ","This is game no.",i+1,"of the tournament!")
          print()
          toss = random.randint(0,10)
          # current player in latter code changes according to this toss.
          if toss%2 == 0:
            current_player = "X"
            print()
            print("       ",player1,"has won the toss and has been assigned 'X'.")
            print()
          else:
            current_player = "O"
            print()
            print("       ",player2,"has won the toss and has been assigned 'O'.")
            print()

          #game board
          
          pvp()
          i += 1
          if p1+p2+p == no_of_games:
            if p1>p2:
              print("             ",player1," has won the tournament with",p1,"wins!")
              print()
            elif p2>p1:
              print("             ",player2," has won the tournament with",p2,"wins!")
              print()
            else:
              print("                  Tournament is a draw!")
              print()

            
          elif p1+p2 == no_of_games:
            if p1>p2:
              print("             ",player1," has won the tournament with",p1,"wins!")
              print()
            elif p2>p1:
              print("             ",player2," has won the tournament with",p2,"wins!")
              print()
            else:
              print("                  Tournament is a draw!")
              print()


      elif mode == "s":
        
        
          game_still_playing = True
          winner = None
          print()
          player1 = input("Enter the name of first player: ")
          player2 = input("Enter the name of second player: ")
          print()
          toss = random.randint(0,10)
          # current player in latter code changes according to this toss.
          if toss%2 == 0:
            current_player = "X"
            print()
            print("       ",player1,"has won the toss and has been assigned 'X'.")
            print()
          else:
            current_player = "O"
            print()
            print("       ",player2,"has won the toss and has been assigned 'O'.")
            print()
            
          pvp()

      else:
        print("You did not choose the correct mode.")
      print()
      continuepvp = input("If you want to play this mode again, enter 'y' \nEnter any other button to select between main menu and exit: ")
      print()

    

          
  #player vs player code ends here and player vs computer code starts after the else.   
  elif game_type == "c" or game_type == "C":
    continuegamepvc = "y"
    while continuegamepvc == "y":
    
      board = [" ","-","-","-",
                   "-","-","-",
                   "-","-","-"]
      
      #to insert O and X into the desired positions on the board
      def letter_insert(letter, pos):
          board[pos] = letter
      #to define any free space remaining in the board
      def freespace(pos):
          return board[pos] == '-'
      #to display the board
      def display_board(board):
        print("                         ",board[1] + "|" + board[2] +  "|" + board[3])
        print("                         ",board[4] + "|" + board[5] +  "|" + board[6])
        print("                         ",board[7] + "|" + board[8] +  "|" + board[9])
        print()
        
      #to check win conditions     
      def winner_check(bd, lt):
        
        return ((bd[1] == lt and bd[2] == lt and bd[3] == lt) or # across the top
        (bd[4] == lt and bd[5] == lt and bd[6] == lt) or # across the middle
        (bd[7] == lt and bd[8] == lt and bd[9] == lt) or # across the bottom
        (bd[1] == lt and bd[4] == lt and bd[7] == lt) or # down the left side
        (bd[2] == lt and bd[5] == lt and bd[8] == lt) or # down the middle
        (bd[3] == lt and bd[6] == lt and bd[9] == lt) or # down the right side
        (bd[1] == lt and bd[5] == lt and bd[9] == lt) or # diagonal
        (bd[3] == lt and bd[5] == lt and bd[7] == lt)) # diagonal

      #move of the player playing the game
      def move_player():
          run = True
          while run:
            move = eval(input("     Please select a position to place an 'X' (1-9): "))
            print()
            try:  
              if move > 0 and move < 10:    
                if freespace(move):
                  run = False
                  letter_insert('X', move)
                else:
                  #to prevent the insertion of O and X on already filled box
                  print("              Sorry, this space is occupied!")
                  print()
              else:
                #if player enters a number other than 1-9
                print("              Please type a number within the range!")
                print()
            except:
              #if player enters a string
              print("              Please type a number!")
              print()
                  
      #move of the computer
      def move_comp():
          possibleMoves = [x for x, letter in enumerate(board) if letter == '-' and x != 0]
          move = 0

          for let in ['O', 'X']:
              for i in possibleMoves:
                  boardCopy = board[:]
                  boardCopy[i] = let
                  if winner_check(boardCopy, let):
                      move = i
                      return move
          #computer selects 5 as its first move if it isnt already taken
          if 5 in possibleMoves:
            move = 5
            return move

          #computer afterwards moves to corners
          cornersOpen = []
          for i in possibleMoves:
              if i in [1,3,7,9]:
                  cornersOpen.append(i)
                  
          if len(cornersOpen) > 0:
              move = random_pos_select(cornersOpen)
              return move

          #it then moves to edges
          edgesOpen = []
          for i in possibleMoves:
              if i in [2,4,6,8]:
                  edgesOpen.append(i)
                  
          if len(edgesOpen) > 0:
              move = random_pos_select(edgesOpen)
              
          return move

      #scomputer selects random position in respond to block the win of player
      def random_pos_select(li):
          import random
          ln = len(li)
          r = random.randrange(0,ln)
          return li[r]
          
      #to check if the board has been filled or only 1 position is left i.e game tie
      def board_full_check(board):
          if board.count('-') > 0:
              return False
          else:
              return True

      #main function
      def main():
          print('                    Player vs Computer')
          print()
          display_board(board)

          while not(board_full_check(board)):
              if not(winner_check(board, 'O')):
                  #allowing player to play next turn if game is not already won/lost
                  move_player()
                  display_board(board)
              else:
                  #to declare computer as a winner
                  print("                   Computer/O has won!")
                  print()
                  break

              if not(winner_check(board, 'X')):
                  #allowing computer to play next turn if game is not already won/lost
                  move = move_comp()
                  
                  #to check tie
                  if move == 0:
                      print('Tie Game!')
                  else:
                      #to make computer place O if no other condition is fulfilled
                      letter_insert('O', move)
                      print("             Computer placed an 'O' in position", move ,":")
                      print()
                      display_board(board)
              else:
                  #to declare player as a winner
                  print("            Player/X has won.")
                  print()
                  break
                
              #to declare that the game is a tie
              if board_full_check(board):
                print("                   This Game is a Tie.")
                print()
      main()
      print()
      continuegamepvc = input("If you want to play this mode again, enter 'y' \nEnter any other button to select between main menu and exit: ")
      print()

      
  else:
    break
  
  continuegame = input("Enter 'm' to go back to main menu \nEnter any other button to exit\nEnter your choice: ")
      
  print()
