# DFA table for identifiers
identifier_table = {
    1: {'L': 2, 'D' : 6, '_': 6},
    2: {'L': 3, 'D' : 4, '_': 5},
    3: {'L': 3, 'D' : 4, '_': 5},
    4: {'L': 3, 'D' : 4, '_': 5},
    5: {'L': 3, 'D' : 4, '_': 5},
    6: {'L': 6, 'D' : 6, '_': 6}
}

start_state = 1
accepting_states = {2, 3, 4, 5}
dead_state = 6

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

    if current_state in accepting_states:
        return True
    else:
        return False

# TEST OUTPUT
print("Output:")
print("-" * 7)
print(f"{'Token':<25}{'lexeme'}")
print("-" * 40)

lexeme = "fahr"

if identifier_dfa(lexeme):
    print(f"{'identifier':<25}{lexeme}")

print(identifier_dfa("abc"))
print(identifier_dfa("abc123"))
print(identifier_dfa("abc_123"))
print(identifier_dfa("123abc"))
print(identifier_dfa("_abc"))
print(identifier_dfa("abc$"))
print(identifier_dfa("abc def"))