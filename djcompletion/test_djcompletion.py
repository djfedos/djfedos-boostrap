import djcompletion
from pathlib import Path


_me_parent = Path(__file__).absolute().parent

def test_completions_ma():
    # arrange
    expected_completions = ['marsaba', 'maramba', 'man', 'may']
    token_path = f'{_me_parent}/tokens.txt'
    prefix = 'ma'
    
    # act
    my_db = djcompletion.load_tokens(token_path)
    actual_completions = djcompletion.get_completions(my_db, prefix)

    # assert            
    assert expected_completions == actual_completions

def test_completions_ba():
    # arrange
    expected_completions = ['bar', 'baron', 'banya']
    token_path = f'{_me_parent}/tokens.txt'
    prefix = 'ba'
    
    # act
    my_db = djcompletion.load_tokens(token_path)
    actual_completions = djcompletion.get_completions(my_db, prefix)

    # assert            
    assert expected_completions == actual_completions