# ====================================================
# CPSC 323 - Assignemnt 2
# RAT26F REcursive Descent Parser
# ====================================================

class Parser:

    def __init__(self, tokens):
        # List of tokens received from the lexer
        self.tokens = tokens

        #current po sition in the token list
        self.position = 0

    def current_token(self):
        # Return None if we reach the end of the tokens
        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]

    def advance(self):
        # Move to the next token in the list
        if self.position < len(self.tokens):
            self.position += 1

    def match(self, expected):
        # Check whether the current token matches
        token = self.current_token()

        if token is None:
            raise SyntaxError(
                f"Expected {expected}, but reached end of input"
            )

        # For now, tokens are represented as:
        # (token_type, lexeme)
        token_type, lexeme = token

        if lexeme == expected or token_type == expected:
            self.advance()
        else:
            raise SyntaxError(
                f"Expected {expected}, but found {lexeme}"
            )

     # First RAT26F rule <Rat26F>
        def parse_rat26f(self):
            self.opt_function_definitions() #R2
            self.match("@") 
            self.opt_declaration_list()     #R10
            self.match("@")
            self.statement_list()           #R14