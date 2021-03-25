from labelconstans import LabelConstants

class VictoryChecker(object):
    
    def __init__(self, player_hand, computer_hand, player, computer):
        self.player_hand = LabelConstants.RPS_VALUE[player_hand]
        self.player = player
        self.computer_hand = LabelConstants.RPS_VALUE[computer_hand]
        self.computer = computer
        
    def check_victory(self):
        winner = LabelConstants.RPS_TABLE[self.player_hand][self.computer_hand]        
        if winner == self.player_hand:
            self.display_winner(self.player, self.computer)
        elif winner == self.computer_hand:
            self.display_winner(self.computer, self.player)
        else:
            print ("Tie! Ugh...")
    
    def display_winner(self, winner, loser):
        print ("{} has lost. {} has won. Long live {}!".format(loser, winner, winner))        