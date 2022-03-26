# this test is made according to this video tutorial: https://youtu.be/6tNS--WetLI

import json
import unittest
import permutate_heaps

class TestPermutate(unittest.TestCase):
    
    
    def test_permutate(self):
        # arrange
        expected_anagrams = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        
        # act
        permutate_heaps.permutate([1, 2, 3])
        with open('./perm_out.json', 'r') as perm_out:
            anagrams = json.load(perm_out)

        # assert            
            self.assertTrue(len(expected_anagrams) == len(anagrams))

            for ex_an in expected_anagrams:
                self.assertTrue(ex_an in anagrams)


if __name__ == "__main__":
    unittest.main()