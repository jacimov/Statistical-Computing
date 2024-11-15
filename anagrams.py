# anagrams.py
import sys
import os
from find_anagrams import find_sets


def load_words(path):
    """Load and clean words from file"""
    with open(path, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def main():
    # Use relative paths from script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, 'anagrams-data')

    # Input/output paths
    eng_path = os.path.join(data_dir, 'english-words.txt')
    more_path = os.path.join(data_dir, 'more-english-words.txt')
    out_path = os.path.join(data_dir, 'anagram_sets.txt')

    try:
        # Combine words from both files
        words = load_words(eng_path) + load_words(more_path)

        # Get and write anagram sets
        anagram_sets = find_sets(words)
        with open(out_path, 'w') as file:
            for word_set in anagram_sets:
                if len(word_set) > 1:
                    file.write(str(word_set) + '\n')

        print(f"Anagram sets written to {out_path}")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
