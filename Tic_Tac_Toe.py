"""
Monte Carlo Tic-Tac-Toe Player
http://www.codeskulptor.org/#user40_y4TLM2etJM_25.py
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    This function takes a current board and 
    the next player to move. 
    """
    curplayer = player
    winner = None
    #scores = [[0 for dummycol in range(board._dim)] 
    #             for dummyrow in range(board._dim)]
    print board.__str__()
    
    while winner == None:
        # Pick an empty square randomly
        empty = board.get_empty_squares()
        empty_sq = empty[random.randrange(len(empty))]
        row = empty_sq[0]
        col = empty_sq[1]
        
        # Move
        board.move(row, col, curplayer)

        # Update state
        winner = board.check_win()
        curplayer = provided.switch_player(curplayer)

        # Display board
        print board.__str__()

    #mc_update_scores(scores,board,board.check_win())
    #get_best_move(board,scores)
    #print "scores", scores
    #print "curplayer", curplayer
    
def mc_update_scores(scores, board, player): 
    """
    This function takes a grid of scores, a board from a 
    completed game, and which player the machine player is. 
    The function scores the completed board and update 
    the scores grid. 
    """
    winner = board.check_win()
    
    # assign score to earn based on the result
    if winner == player:
        player_score = SCORE_CURRENT
        other_score = -SCORE_OTHER
    elif winner == provided.switch_player(player):
        player_score = -SCORE_CURRENT
        other_score = SCORE_OTHER
    else:
        player_score = 0
        other_score = 0
        
    for dummyrow in range(board.get_dim()):
        for dummycol in range(board.get_dim()):
            if board.square(dummyrow,dummycol) == player:
                scores[dummyrow][dummycol] += player_score
            elif board.square(dummyrow,dummycol) == provided.switch_player(player):
                scores[dummyrow][dummycol] += other_score 
   
    
def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. 
    The function finds all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.
    """
    #get empty squares
    empty = board.get_empty_squares()
    print "empty", empty
    
    temp = []
    for dummy in empty:
        dummyrow = dummy[0]
        dummycol = dummy[1]
        temp += [scores[dummyrow][dummycol]]
    max_score = max(temp)
    print "max_score", max_score
    
    max_empty_sq = []
    for dummy in empty:
        dummyrow = dummy[0]
        dummycol = dummy[1]
        if scores[dummyrow][dummycol] == max_score:
            max_empty_sq += [(dummyrow,dummycol)]
    
    print "max_empty_sq", max_empty_sq
    random_sq = max_empty_sq[random.randrange(len(max_empty_sq))]
    print "random_sq", random_sq
    
    return random_sq

#board = provided.TTTBoard(3)
#player = provided.PLAYERX
#mc_trial(board,player)

    

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine 
    player is, and the number of trials to run. The function should 
    use the Monte Carlo simulation described above to return a move 
    for the machine player in the form of a (row, column) tuple. 
    """
    scores = [[0 for dummycol in range(board.get_dim())] 
                 for dummyrow in range(board.get_dim())]
    
    for dummy in range(trials):
        board_sim = board.clone()
        mc_trial(board_sim, player)
        mc_update_scores(scores, board_sim, player)
    
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

