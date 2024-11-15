def find_crowded(cows, k):
    """Find highest breed ID of cows within k positions of each other"""
    if len(cows) < 2:
        return -1

    pos = {}
    crowded = set()

    for i, breed in enumerate(cows):
        if breed in pos:
            if i - pos[breed][-1] <= k:
                crowded.add(breed)
            pos[breed].append(i)
        else:
            pos[breed] = [i]

    return max(crowded) if crowded else -1
