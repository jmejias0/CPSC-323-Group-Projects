#Gio's part 

SEPARATORS = {'(', ')', '{', '}', ';', ',', '@'} 
SIMPLE_OPS = {'=', '<', '>', '+', '-', '*', '/'}
DOUBLE_OPS = {'==', '!=', '<=', '>='} #operators that use 2 characters are defined here


def match_op_or_sep(src, i):
    """Try to match an operator or separator at src[i].
    Returns (token_type, lexeme, new_index) or None if no match."""
    two = src[i:i+2]
    ch = src[i]

    # Longest match first so this checks 2-char operators before 1-char ones
    if two in DOUBLE_OPS:
        return ('operator', two, i + 2)
    if ch in SEPARATORS:
        return ('separator', ch, i + 1)
    if ch in SIMPLE_OPS:
        return ('operator', ch, i + 1)
    return None