from src.victorychecker import VictoryChecker
from unittest.mock import patch

class PlayerTest():
    
    def check_victory_test(self):
        
        with patch.object('builtins', 'print') as test_mock:
            test = VictoryChecker('rock', 'paper', 'A', 'B')
        
        test_mock.assertTrue ('B has lost. A has won. Long live A!')