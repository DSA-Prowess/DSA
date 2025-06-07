"""
Problem You have a collection of baby blocks (cubes with single upper-case letters of the alphabet on each side).
Each block could have up to six different letters on it (or even more if we're in a universe with more than 3 dimensions), but for the sake of simplicity, we'll assume for now that each block only has two distinct letters.
The problem is to write a function that takes a collection of blocks and a target word and returns true or false depending on whether or not you can spell the target word with the collection of blocks.
Example:
 (B,A),(A,B),(X,Y),(A,B): "BABY" => true 
 (B,A),(A,B),(L,E),(A,B): "ABLE" => false (since L and E are on the same block).
"""

def can_spell_word(blocks, target_word):
    """
    Determine if a target word can be spelled using a collection of letter blocks.
    
    Args:
        blocks: List of tuples, where each tuple contains the letters on a block
        target_word: The word we're trying to spell
    
    Returns:
        Boolean indicating whether the word can be spelled
    """
    # Create a copy of blocks we can modify
    #Since we are popping available block by default it is a stack ??
    available_blocks = blocks.copy()
    
    # Try to spell each letter in the target word
    for letter in target_word:
        found_block = False
        
        # Look through available blocks for this letter
        for i, block in enumerate(available_blocks):
            if letter in block:
                # Found a block with this letter, remove it from available blocks
                found_block = True
                available_blocks.pop(i)
                break
        
        # If we couldn't find a block with this letter, return False
        if not found_block:
            return False
    
    # If we made it through all letters, return True
    return True

# Test cases
print(can_spell_word([('B','A'),('A','B'),('X','Y'),('A','B')], "BABY"))  # True
print(can_spell_word([('B','A'),('A','B'),('L','E'),('A','B')], "ABLE"))  # False