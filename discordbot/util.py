import difflib
from .emojis import emojis

def railfence_encode(n_rails: int, plaintext: str) -> str:
    """
    Encodes a plaintext string into crypttext using the railfence cipher. This
    function assumes that n_rails is at least 1.
    
    Parameters
    ----------
    n_rails: int
        Number of rails
    
    plaintext: str
        Original unencoded string
        
    Returns
    -------
    str
        Encrypted version of plaintext (i.e. crypttext)
    """
    # If only 1 rail, then no modification needed
    if n_rails == 1:
        return plaintext
    
    # How many characters there are in each "up-down" cycle.
    #
    # For example, with 5 rails:
    # a.......i
    # .b.....h.j
    # ..c...g...k
    # ...d.f.... and so on ...
    # ....e......
    #
    # A letter's vertical position (a.k.a. rail) goes from top to bottom then
    # top again (a to e to h, i is part of a new cycle).
    # Notice there are 8 letters in the cycle.
    # In fact, if you experiment with different numbers of rails, you'll find
    # that the length of each cycle is 2 * (n_rails - 1)
    cycle_len = 2*(n_rails-1)
    
    # List of rails
    # Each rail stores the characters at each vertical position
    # e.g. The 0th character falls in rails[0], the 1st character in rails[1]
    # and so on
    rails = []
    for _ in range(n_rails):
        rails.append("")
    
    # Go through each character in plaintext
    for index in range(len(plaintext)):
        # Get the character at that index
        character = plaintext[index]
        
        # Figure out position of the character in the "up-down" cycle
        # 
        # In the example above, the letter j (index 9) would be in position 1,
        # while for the letter h (index 7) would be in position 7.
        #
        # Note that `a % b` finds the remainder when `a` is divided by `b`
        position = index % cycle_len
        
        # Find which rail the letter belongs to based on their position in the
        # "up-down" cycle
        #
        # If position is on the downward side of the cycle (0 to 4 in the
        # example), then the rail that character belongs to is simply its
        # position in the cycle.
        #
        # However, for characters on the upward side of the cycle (from 5 to 7),
        # the rail a character belongs to is not simply its position.
        # For example, with the letter h (position 7), it is supposed to be in
        # rail 1, so we must map position 7 to rail 1 like so:
        if position >= n_rails:
            rail = cycle_len - position
        else:
            rail = position
            
        # Add character to that rail
        rails[rail] += character
    
    # Concatenate rails to create the final output
    output = ""
    for rail in rails:
        output += rail
    
    # Send output back to calling function
    return output


def bubble_sort(sequence):
    """
    Sort a sequence in ascending order using the bubble sort algorithm.
    """
    seq_len = len(sequence)
    ordered = False
    
    # Continue sorting until the list is sorted
    while not ordered:
        # Assume sequence is already sorted
        ordered = True
        # Go through each number in the sequence
        for i in range(seq_len-1):
            # If this number is greater than the number after it, then swap
            if sequence[i] > sequence[i+1]:
                # The sequence was not already ordered correctly
                # So we set ordered to False to tell the while loop
                # to go through the list one more time to check
                ordered = False
                temp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = temp
    
    # Technically not necessary as lists are "pass by reference" in Python
    # See https://realpython.com/python-pass-by-reference/ to find out more
    return sequence


def emoji_list():
    return list(emojis.keys())


def best_fit_emoji(word, options):
    possibilities = difflib.get_close_matches(word, options, 1, 0.6)
    if possibilities != []:
        emoji_name = possibilities[0]
        return emojis[emoji_name]
    else:
        return ''