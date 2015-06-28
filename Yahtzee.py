"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
http://www.codeskulptor.org/#user40_8NmUErVnty_22.py
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(60)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    unique = set(hand)
    score_counter = {}
    for dummy in unique:
        score_counter[dummy] = hand.count(dummy)
    
    score_board = []
    for key in score_counter:
        current_score = key * score_counter[key]
        score_board += [current_score]
    
    max_score = max(score_board)
    return max_score



def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = set([x+1 for x in range(num_die_sides)])
    remaining_seq = gen_all_sequences(outcomes, num_free_dice)
    #print remaining_seq
    
    counter = 0
    total = 0.0
    
    for dummy_hand in remaining_seq:
        current_hand = held_dice + dummy_hand
        current_score = score(current_hand)
        #print current_hand, current_score
        total += current_score
        counter += 1
    
    return float(total)/counter

#print expected_value((), 6, 1)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])

    for item in hand:
        temp_set = set()
        for partial_sequence in answer_set:
            #print "partial_sequence", partial_sequence
            new_sequence = list(partial_sequence)
            new_sequence.append(item)
            temp_set.add(tuple(new_sequence))
            #print "temp_set", temp_set
        answer_set.update(temp_set)
        #print "answer_set", answer_set
    return answer_set



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    potential_hands = gen_all_holds(hand)
    
    expected_score = 0.0
    best_hand = ()
    
    for dummy_hand in potential_hands:
        print "dummy_hand", dummy_hand
        num_free_dice = len(hand) - len(dummy_hand)
        print "num_free_dice", num_free_dice
        temp_score = expected_value(dummy_hand, 
                                    num_die_sides, num_free_dice)
        print "temp_score", temp_score
        if temp_score >= expected_score:
            best_hand = dummy_hand
            expected_score = temp_score
    
    return (expected_score, best_hand)

#hand = (1, 1, 1, 5, 6)
#strategy(hand,6)




def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    #hand = (1, 1, 1, 5, 6)
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



