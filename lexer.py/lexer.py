# DFA table for identifiers
identifier_table = {
    1: {'L': 2, 'D' : 6, '_': 6},
    2: {'L': 3, 'D' : 4, '_': 5},
    3: {'L': 3, 'D' : 4, '_': 5},
    4: {'L': 3, 'D' : 4, '_': 5},
    5: {'L': 3, 'D' : 4, '_': 5},
    6: {'L': 6, 'D' : 6, '_': 6}
}
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
    current_state = 1
    for char in lexeme:
        char_type = character_type(char)
        if char_type == "Unknown token":
            return False
        current_state = identifier_table[current_state][char_type]
    