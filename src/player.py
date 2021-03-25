import random
from labelconstans import LabelConstants

class Player(object):
    
    def __init__(self):
        self.hand = []

    def player_hand(self):
        print('Please choose (R)ock, (P)aper, or (S)cissor: ')
        hand_p = str(input()).upper()
        if hand_p in LabelConstants.LABELS.keys():
            return LabelConstants.LABELS[hand_p]
        else:
            print ('Invalid selection. Please try again.')
            self.player_hand()

    def computer_hand(self):
        hand_c = random.randint(1,3)
        if hand_c == 1:
            return LabelConstants.LABELS["R"]
        elif hand_c == 2:
            return LabelConstants.LABELS["P"]
        elif hand_c == 3:
            return LabelConstants.LABELS["S"]