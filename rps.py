from player import Player
from victorychecker import VictoryChecker

class Rps(object):

    def __init__(self):
        self.player = self.create_player()
        self.computer = 'Khaox'
        self.game_over = None

    def create_player(self):
        print("Please enter your name: ")
        return str(input())

    def play_game(self):
        self.pause()
        while self.game_over is None:
            plyr = Player()
            hand_p = plyr.player_hand()
            hand_c = plyr.computer_hand()
            self.display_play(hand_p, hand_c)
            victory = VictoryChecker(hand_p,hand_c,self.player,self.computer)
            victory.check_victory()
            self.pause()

    def display_play(self, hand_p, hand_c):
        print ("{} plays {}.".format(self.player, hand_p))
        print ("{} plays {}.".format(self.computer, hand_c))

    def pause(self):
        print("Press 'enter' when you're ready to play against {} (the computer). Type 'exit' otherwise".format(self.computer))
        if str(input()).lower() == 'exit':
            self.game_over=True

if __name__ == "__main__":
    game = Rps()
    game.play_game()
