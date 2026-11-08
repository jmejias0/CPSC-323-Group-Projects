
# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# ====================================================

from .definitions import DefinitionRules
from .functions import FunctionRules
from .expressions import ExpressionRules
from .statement import StatementRules


class Parser(FunctionRules, DefinitionRules, ExpressionRules, StatementRules):

    def __init__(self, tokens):
        # List of tokens received from the lexer
        self.tokens = tokens

        # Current position in the token list
        self.position = 0

        # Enable or disable production rule printing
        self.show_rules = True

    def current_token(self):
        # Return None if we reach the end of the tokens
        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]

    def advance(self):
        # Move to the next token in the list
        if self.position < len(self.tokens):
            self.position += 1

    # ---------- Shared helper functions ----------

    def _lexeme(self):
        token = self.current_token()
        return token[1] if token is not None else None

    def _type(self):
        token = self.current_token()
        return token[0].lower() if token is not None else None

    def print_rule(self, rule):
        # Prints the production rule used when enabled
        if self.show_rules:
            print("     " + rule)

    def match(self, expected):
        # Check whether the current token matches
        token = self.current_token()

        if token is None:
            raise SyntaxError(
                f"Expected {expected}, but reached end of input"
            )

        # Tokens are represented as:
        # (token_type, lexeme)
        token_type, lexeme = token

        if lexeme == expected or token_type.lower() == expected.lower():
            self.advance()
        else:
            raise SyntaxError(
                f"Expected {expected}, but found {lexeme}"
            )

    # First Rule #R1 of RAT26F is <Rat26F>
    def parse_rat26f(self):
        self.print_rule(
            "<Rat26F> -> <Opt Function Definitions> @ "
            "<Opt Declaration List> @ <Statement List>"
        )

        self.opt_function_definitions()  # R2
        self.match("@")
        self.opt_declaration_list()      # R10
        self.match("@")
        self.statement_list()            # R14

        # Ensure the entire program has been parsed
        if self.current_token() is not None:
            raise SyntaxError(
                f"Unexpected token after program: {self.current_token()}"
            )

    # Second Rule #R2 of RAT26F is <Opt Function Definitions>
    def opt_function_definitions(self):
        if self._lexeme() == "function":
            self.print_rule(
                "<Opt Function Definitions> -> <Function Definitions>"
            )
            self.function_definitions()  # R3

        else:
            self.print_rule(
                "<Opt Function Definitions> -> <Empty>"
            )
            self.empty()  # R29

    # Twenty-Ninth Rule #R29 of RAT26F is <Empty>
    def empty(self):
        # Empty production: consumes no tokens
        pass
