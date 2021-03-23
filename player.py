import random


class Player(object):

    def __init__(self):
        self.hand = []

    def player_hand(self):
        hand_p = raw_input('Please choose (R)ock, (P)aper, or (S)cissor: ')
        if hand_p not in 'rpsRPS':
            print 'Invalid selection. Please try again.'
            self.player_hand()
        elif hand_p == 'r' or hand_p == 'R':
            hand_p = 'rock'
            return hand_p
        elif hand_p == 'p' or hand_p == 'P':
            hand_p = 'paper'
            return hand_p
        elif hand_p == 's' or hand_p == 'S':
            hand_p = 'scissor'
            return hand_p

    def computer_hand(self):
        hand_c = random.randint(1,3)
        if hand_c == 1:
            return 'rock'
        elif hand_c == 2:
            return 'paper'
        elif hand_c == 3:
            return 'scissor'
