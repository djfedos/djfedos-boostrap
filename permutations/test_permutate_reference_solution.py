# this test is made according to this video tutorial: https://youtu.be/6tNS--WetLI

import unittest
import permutate_reference_solution

class TestPermutate(unittest.TestCase):
    
    
    def test_permutate(self):
        anagrams = permutate_reference_solution.permutate([1, 2, 3])
        anagrams.sort()
        expected_anagrams = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(anagrams, expected_anagrams)


if __name__ == "__main__":
    unittest.main()