# ====================================================
# CPSC 323 - Assignemnt 2
# RAT26F REcursive Descent Parser
# ====================================================

class Parser:

    def__init__(self, tokens):
        # List of tokens received from the lexer
        self.tokens = tokens

        #current po sition in the token list
        self.position = 0

    def current_token(self):
        # Return None if we reach the end of the tokens
        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]