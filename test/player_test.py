from src.player import Player
from unittest.mock import patch

class PlayerTest():
    
    @patch('builtins.input', return_value = 'R')
    def player_hand_test(self):
        
        test_player = Player()
        
        test_player.player_hand()
        
        self.assertTrue(test_player.hand == 'rock')        