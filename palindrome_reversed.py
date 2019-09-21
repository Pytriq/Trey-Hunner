def palindromic(sequence):
    """Return True if the sequence is the same thing in reverse."""
    for m, n in zip(sequence, reversed(sequence)):
        if m != n:
            return False
    return True
