
import  pytest
from Tic_Tac_Toe import GameLogic


def test_input():
    game = GameLogic()
    actual =  game.validate_input('8')
    expected = True
    assert actual == expected
    #      False  ==  True

def test_empty():
    game = GameLogic()
    game.selected_spots =['1']
    actual =  game.isEmpty_spot('1')
    expected = False
    assert actual == expected

def test_winner():
    game = GameLogic()
    game.board = [
    ["x",'o','o'],
    ["x",'x','o'],
    ['o','o','x']]
    game.check_for_winner()
    actual = game.is_Finished 
    expected = True
    assert actual == expected

def test_board():
    game = GameLogic()  
    game.board = [
    ["x",'o','x'],
    ["x",'x','o'],
    ['o','x','o']]
    game.selected_spots = ['1','2','3','4','5','6','7','8','9']
    game.check_for_winner() 
    actual = game.game_result
    expected = "Draw!"
    assert actual == expected