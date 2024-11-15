# test_find_anagrams.py
import unittest
from find_anagrams import sort_str, find_sets
import os


class TestAnagramFinder(unittest.TestCase):
    def setUp(self):
        """Set up test paths"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(script_dir, 'anagrams-data')
        self.eng_path = os.path.join(data_dir, 'english-words.txt')
        self.more_path = os.path.join(data_dir, 'more-english-words.txt')

    def test_sort_str(self):
        """Test string sorting helper function"""
        # Basic sorting
        self.assertEqual(sort_str("cat"), "act")
        self.assertEqual(sort_str("dog"), "dgo")

        # Case handling
        self.assertEqual(sort_str("Cat"), "act")
        self.assertEqual(sort_str("CAT"), "act")

        # Special cases
        self.assertEqual(sort_str("ca t"), " act")
        self.assertEqual(sort_str("cat2"), "2act")
        self.assertEqual(sort_str("c@t"), "@ct")
        self.assertEqual(sort_str(""), "")

    def test_basic(self):
        """Test basic anagram detection"""
        words = ['listen', 'silent', 'enlist']
        result = find_sets(words)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {'listen', 'silent', 'enlist'})

        # Non-anagrams
        words = ['cat', 'dog', 'bird']
        self.assertEqual(len(find_sets(words)), 0)

        # Duplicates
        words = ['cat', 'cat', 'tac']
        self.assertEqual(find_sets(words)[0], {'cat', 'tac'})

    def test_case(self):
        """Test case sensitivity"""
        words = ['Listen', 'Silent', 'ENLIST', 'inLest']
        result = find_sets(words)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {'Listen', 'Silent', 'ENLIST', 'inLest'})

    def test_edge(self):
        """Test edge cases"""
        # Empty input
        self.assertEqual(find_sets([]), [])

        # Single word
        self.assertEqual(find_sets(['cat']), [])

        # Spaces
        words = ['new york', 'work yen']
        self.assertEqual(find_sets(words)[0], {'new york', 'work yen'})

        # Special chars
        words = ['cat!', '!cat', 'act!']
        self.assertEqual(find_sets(words)[0], {'cat!', '!cat', 'act!'})

    def test_groups(self):
        """Test multiple anagram groups"""
        words = ['cat', 'tac', 'act', 'dog', 'god', 'bird']
        result = find_sets(words)
        self.assertEqual(len(result), 2)
        expected = [{'cat', 'tac', 'act'}, {'dog', 'god'}]
        for group in result:
            self.assertIn(group, expected)

    def test_nums(self):
        """Test numbers in words"""
        words = ['cat2', '2cat', 'act2']
        result = find_sets(words)
        self.assertEqual(result[0], {'cat2', '2cat', 'act2'})

    def test_unicode(self):
        """Test unicode characters"""
        words = ['café', 'éfac', 'facé']
        result = find_sets(words)
        self.assertEqual(result[0], {'café', 'éfac', 'facé'})

    def test_file(self):
        """Test with file data"""
        try:
            with open(self.eng_path, 'r') as file:
                words = [next(file).strip() for _ in range(100)]

            result = find_sets(words)

            for anagram_set in result:
                self.assertGreaterEqual(len(anagram_set), 2)
                first_sorted = sort_str(list(anagram_set)[0])
                for word in anagram_set:
                    self.assertEqual(sort_str(word), first_sorted)

        except FileNotFoundError:
            self.skipTest("Test file not found")

    def test_perf(self):
        """Test performance"""
        words = ['word' + str(i) for i in range(1000)]
        words.extend(['cat', 'tac', 'act'] * 100)

        import time
        start = time.time()
        result = find_sets(words)
        duration = time.time() - start

        self.assertLess(duration, 1.0)
        self.assertTrue(any({'cat', 'tac', 'act'} == s for s in result))

    def test_empty(self):
        """Test empty strings and whitespace"""
        # Test empty strings and whitespace-only strings
        words = ['', ' ', '  ', '\t', '\n']
        self.assertEqual(find_sets(words), [])
        # Test words with varying whitespace
        words = ['cat', 'tac', 'act', ' cat', 'cat ', ' cat ']
        result = find_sets(words)
        self.assertEqual(len(result), 1)  # Should only have one group
        expected_set = {'cat', 'tac', 'act', ' cat', 'cat ', ' cat '}
        self.assertEqual(result[0], expected_set)


if __name__ == '__main__':
    unittest.main(verbosity=2)
