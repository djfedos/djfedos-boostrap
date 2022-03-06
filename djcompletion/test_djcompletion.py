import unittest
import djcompletion

class TestDjcompletion(unittest.TestCase):

    def test_completions_ma(self):
        # arrange
        expected_completions = ['marsaba', 'maramba', 'man', 'may']
        token_path = 'tokens.txt'
        prefix = 'ma'
        
        # act
        my_db = djcompletion.load_tokens(token_path)
        actual_completions = djcompletion.get_completions(my_db, prefix)

        # assert            
        self.assertEqual(expected_completions, actual_completions)


if __name__ == "__main__":
    unittest.main()