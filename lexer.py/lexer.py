#===================================================================
# Programmers:Jose Mejias, Giovanni Arredondo, Jonnathan Quijada
# Assignment Number: 1
# Class:CPSC-323
#===================================================================
#  Lexer Pseudocode
#   Check for Identifyers
#   Check for Keywords
#   Check for Digits
#   Check for Operators/Separators
#   Check for Comments
#   Print result
#====================================================================
# Tables
identifier_table = {
    1: {'L': 2, 'D' : 6, '_': 6},
    2: {'L': 3, 'D' : 4, '_': 5},
    3: {'L': 3, 'D' : 4, '_': 5},
    4: {'L': 3, 'D' : 4, '_': 5},
    5: {'L': 3, 'D' : 4, '_': 5},
    6: {'L': 6, 'D' : 6, '_': 6}
}
digit_table = {
    1: {'D': 2, '.': 5},
    2: {'D': 2, '.': 3},
    3: {'D': 4, '.': 5},
    4: {'D': 4, '.': 5},
    5: {'D': 5, '.': 5}
}
SEPARATORS = {'(', ')', '{', '}', ';', ',', '@'} 
SIMPLE_OPS = {'=', '<', '>', '+', '-', '*', '/'}
DOUBLE_OPS = {'==', '!=', '<=', '>='} #operators that use 2 characters are defined here
# States
start_state = 1

identifier_accepting_states = {2, 3, 4, 5}
digit_accept_states = {4}
#dead_state = 6
#accepting_states = {2, 3, 4, 5}


#===================================================================
# FUNCTIONS
#===================================================================
def character_type(char):
    if char.isalpha():
        return "L"
    elif char.isdigit():
        return "D"
    elif char == '_':
        return "_"
    else:
        return "Unknown token"
def identifier_dfa(lexeme):
    current_state = start_state

    for char in lexeme:
        char_type = character_type(char)

        if char_type == "Unknown token":
            return False

        #previos_state = current_state
        current_state = identifier_table[current_state][char_type]

        # print(previos_state, "--", char, char_type, "->", current_state)

    if current_state in identifier_accepting_states:
        return True
    else:
        return False
def digit_type(char):
    if char.isdigit():
        return "D"
    elif char == '.':
        return "."
    else:
        return "Unknown token"
def digit_check(lexeme):
    current_state = start_state

    for char in lexeme:
        char_type = digit_type(char)
        if char_type == "Unknown token":
                return False
        current_state = digit_table[current_state][char_type]
    if current_state in digit_accept_states:
        return True
    else:
         return False
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
#===================================================================
# Lexer MAIN
#===================================================================
#apple)

# (apple)
def lexer(lexeme):
    # Check for identifyers
    if identifier_dfa(lexeme):
        print(f"{'identifier':<25}{lexeme}")
    # Check for Keywords
    # Check for Digits
    if digit_check(lexeme):
       print(f"{'Digit':<25}{lexeme}")
    # Check for Operator/Separator
    match_op_or_sep(lexeme,1)
    # Check for Comments



    # End of File
    #print(identifier_dfa("abc"))
    #print(identifier_dfa("abc123"))
    #print(identifier_dfa("abc_123"))
    #print(identifier_dfa("123abc"))
    #print(identifier_dfa("_abc"))
    #print(identifier_dfa("abc$"))
    #print(identifier_dfa("abc def"))