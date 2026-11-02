# ====================================================
# CPSC 323 - Assignemnt 2
# RAT26F REcursive Descent Parser
# ====================================================

from .functions import FunctionRules

class Parser(FunctionRules):

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

    # First Rule #R1 of RAT26F is <Rat26F>
    def parse_rat26f(self):
            self.opt_function_definitions() #R2
            self.match("@") 
            self.opt_declaration_list()     #R10
            self.match("@")
            self.statement_list()           #R14

    #Second Rule #R2 of RAT26F is <Opt Function Definitions>
    def opt_function_definitions(self):
        token = self.current_token()

        if token is not None and token[1] == "function":
            self.function_definitions() #R3
        else:
            self.empty() #R29

    # Twenty-Ninth Rule #R29 of RAT26F is <Empty>
    def empty(self):
        # This rule does nothing, as it represents an empty production
        pass

    