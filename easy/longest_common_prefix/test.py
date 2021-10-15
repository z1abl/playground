import unittest
from .solution import Solution

class TestLongestCommonPrefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        solution = Solution()
        longestCommonPrefixOne = solution.longestCommonPrefixOne
        self.assertEqual(longestCommonPrefixOne(['','a','a']), '')
        self.assertEqual(longestCommonPrefixOne(['a','abc','a']), 'a')
        self.assertEqual(longestCommonPrefixOne(['test','test','test']), 'test')
        self.assertEqual(longestCommonPrefixOne(['flower','flow','flight']), 'fl')
        self.assertEqual(longestCommonPrefixOne(['','flow','flight']), '')
        self.assertEqual(longestCommonPrefixOne(['matching','matchi','match']), 'match')
        self.assertEqual(longestCommonPrefixOne(['matcing','matchi','match']), 'matc')

        longestCommonPrefixTwo = solution.longestCommonPrefixTwo
        self.assertEqual(longestCommonPrefixTwo(['','a','a']), '')
        self.assertEqual(longestCommonPrefixTwo(['a','abc','a']), 'a')
        self.assertEqual(longestCommonPrefixTwo(['test','test','test']), 'test')
        self.assertEqual(longestCommonPrefixTwo(['flower','flow','flight']), 'fl')
        self.assertEqual(longestCommonPrefixTwo(['','flow','flight']), '')
        self.assertEqual(longestCommonPrefixTwo(['matching','matchi','match']), 'match')
        self.assertEqual(longestCommonPrefixTwo(['matcing','matchi','match']), 'matc')

        longestCommonPrefixThree = solution.longestCommonPrefixThree
        self.assertEqual(longestCommonPrefixThree(['','a','a']), '')
        self.assertEqual(longestCommonPrefixThree(['a','abc','a']), 'a')
        self.assertEqual(longestCommonPrefixThree(['test','test','test']), 'test')
        self.assertEqual(longestCommonPrefixThree(['flower','flow','flight']), 'fl')
        self.assertEqual(longestCommonPrefixThree(['','flow','flight']), '')
        self.assertEqual(longestCommonPrefixThree(['matching','matchi','match']), 'match')
        self.assertEqual(longestCommonPrefixThree(['matcing','matchi','match']), 'matc')


if __name__ == '__main__':
    unittest.main()