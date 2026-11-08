#===================================================================
# Programmers: Jose Mejias, Giovanni Arredondo, Jonnathan Quijada
# Assignment Number: 2
# Class: CPSC-323
#===================================================================
#   Syntax Analyzer main program
#   1. Ask for the input file
#   2. Split the source into tokens using the Assignment 1 lexer()
#   3. Run the recursive descent parser on the tokens
#   4. Write every token, lexeme and production rule used to the
#      output file (output_<input name>.txt)
#   5. On a syntax error, write the token, lexeme, line number
#      and error type
#===================================================================

import os
from lexer.lexer import lexer, SEPARATORS, SIMPLE_OPS, DOUBLE_OPS
from rat26f_parser import Parser

# Switch to turn production rule printing on or off
SHOW_RULES = True

# lexer() calls an integer a "Digit"; the parser expects "integer"
TYPE_NAMES = {"Digit": "integer", "Real": "real"}


#===================================================================
# TOKENIZER
#===================================================================
def tokenize(source):
    """Split the source code into tokens.
    Returns two lists: tokens as (token_type, lexeme) and the line
    number each token is on."""
    tokens = []
    lines = []
    line = 1
    i = 0

    while i < len(source):
        char = source[i]

        # Newlines: count them for error messages
        if char == "\n":
            line += 1
            i += 1
            continue

        # Other white space is ignored
        if char.isspace():
            i += 1
            continue

        two_chars = source[i:i + 2]

        # != is an operator, not the start of a comment
        if two_chars == "!=":
            tokens.append(("operator", "!="))
            lines.append(line)
            i += 2
            continue

        # Comments: everything between ! and ! is skipped
        if char == "!":
            end = source.find("!", i + 1)
            if end == -1:          # comment never closed: skip to the end
                end = len(source) - 1
            line += source.count("\n", i, end + 1)
            i = end + 1
            continue

        # Two-character operators (==, <=, >=)
        if two_chars in DOUBLE_OPS:
            tokens.append((lexer(two_chars), two_chars))
            lines.append(line)
            i += 2
            continue

        # Separators and one-character operators
        if char in SEPARATORS or char in SIMPLE_OPS:
            tokens.append((lexer(char), char))
            lines.append(line)
            i += 1
            continue

        # Identifiers and keywords: a letter followed by letters, digits or _
        if char.isalpha():
            j = i
            while j < len(source) and (source[j].isalnum() or source[j] == "_"):
                j += 1
            word = source[i:j]
            tokens.append((lexer(word), word))
            lines.append(line)
            i = j
            continue

        # Integers and reals (123, 123.00, .001)
        if char.isdigit() or (char == "." and source[i + 1:i + 2].isdigit()):
            j = i
            while j < len(source) and source[j].isdigit():
                j += 1
            # Only a "." followed by a digit makes a real ("123." is not one)
            if j < len(source) and source[j] == "." and source[j + 1:j + 2].isdigit():
                j += 1
                while j < len(source) and source[j].isdigit():
                    j += 1
            number = source[i:j]
            token_type = lexer(number)
            tokens.append((TYPE_NAMES.get(token_type, token_type), number))
            lines.append(line)
            i = j
            continue

        # Anything else is an unknown character
        tokens.append(("Unknown", char))
        lines.append(line)
        i += 1

    return tokens, lines


#===================================================================
# PARSER THAT WRITES TO THE OUTPUT FILE
#===================================================================
class OutputParser(Parser):
    """The group Parser, but every token and production rule is
    written to the output file in the order they are used."""

    def __init__(self, tokens, lines, output_file):
        super().__init__(tokens)
        self.lines = lines
        self.out = output_file
        self.show_rules = SHOW_RULES
        self.write_current_token()        # print the first token

    def write_current_token(self):
        token = self.current_token()
        if token is not None:
            token_type, lexeme = token
            self.out.write(f"Token: {token_type.capitalize():<15}Lexeme: {lexeme}\n")

    def advance(self):
        # Move to the next token and print it, like calling lexer()
        super().advance()
        self.write_current_token()

    def print_rule(self, rule):
        if self.show_rules:
            self.out.write("     " + rule + "\n")

    def current_line(self):
        if self.position < len(self.lines):
            return self.lines[self.position]
        return self.lines[-1] if self.lines else 1


#===================================================================
# MAIN
#===================================================================
def main():
    in_file = input("Enter Input File directory: ").strip().strip('"')

    try:
        with open(in_file, "r") as file:
            source = file.read()
    except FileNotFoundError:
        print("ERR, no valid input file at this directory.")
        return

    # Name the output after the input (test1.txt -> output_test1.txt)
    folder = os.path.dirname(in_file)
    name = os.path.splitext(os.path.basename(in_file))[0]
    out_name = os.path.join(folder, "output_" + name + ".txt")

    tokens, lines = tokenize(source)

    with open(out_name, "w") as output_file:
        parser = OutputParser(tokens, lines, output_file)
        try:
            parser.parse_rat26f()
            output_file.write("\nParsing complete: the program is syntactically correct.\n")
            print("Parsing complete: no syntax errors.")
        except SyntaxError as error:
            token = parser.current_token()
            message = (
                "\nSYNTAX ERROR\n"
                f"  Line number: {parser.current_line()}\n"
                f"  Token:       {token[0] if token else 'end of file'}\n"
                f"  Lexeme:      {token[1] if token else 'end of file'}\n"
                f"  Error type:  {error}\n"
            )
            output_file.write(message)
            print(message)

    print("Results written to " + out_name)
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()