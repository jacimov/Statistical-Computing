# find_anagrams.py

def sort_str(word):
    """Sort letters in word (case-insensitive)"""
    return ''.join(sorted(word.strip().lower()))


def find_sets(words):
    """Group words into anagram sets"""
    groups = {}

    for word in words:
        if not word.strip():
            continue

        key = sort_str(word)
        if key in groups:
            groups[key].add(word)
        else:
            groups[key] = {word}

    return [group for group in groups.values() if len(group) >= 2]
