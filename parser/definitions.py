
# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# Declaration-related grammar rules
# ====================================================

class DefinitionRules:

    # R8: <Qualifier> ::= integer | boolean | real
    def qualifier(self):
        token = self.current_token()

        if token is not None and token[1] == "integer":
            self.print_rule("<Qualifier> -> integer")
            self.match("integer")

        elif token is not None and token[1] == "boolean":
            self.print_rule("<Qualifier> -> boolean")
            self.match("boolean")

        elif token is not None and token[1] == "real":
            self.print_rule("<Qualifier> -> real")
            self.match("real")

        else:
            raise SyntaxError(
                f"Expected integer, boolean, or real, but found {token}"
            )

    # R10: <Opt Declaration List> ::= <Declaration List> | <Empty>
    def opt_declaration_list(self):
        token = self.current_token()

        if token is not None and token[1] in ("integer", "boolean", "real"):
            self.print_rule(
                "<Opt Declaration List> -> <Declaration List>"
            )
            self.declaration_list()  # R11

        else:
            self.print_rule(
                "<Opt Declaration List> -> <Empty>"
            )
            self.empty()  # R29

    # R11: <Declaration List> ::= <Declaration> ; <Declaration List Prime>
    def declaration_list(self):
        self.print_rule(
            "<Declaration List> -> <Declaration> ; <Declaration List Prime>"
        )
        self.declaration()             # R12
        self.match(";")
        self.declaration_list_prime()  # R33

    # R12: <Declaration> ::= <Qualifier> <IDs>
    def declaration(self):
        self.print_rule(
            "<Declaration> -> <Qualifier> <IDs>"
        )
        self.qualifier()  # R8
        self.ids()        # R13

    # R13: <IDs> ::= <Identifier> <IDs Prime>
    def ids(self):
        self.print_rule(
            "<IDs> -> <Identifier> <IDs Prime>"
        )
        self.match("identifier")
        self.ids_prime()  # R34

    # R33: <Declaration List Prime> ::= <Declaration List> | <Empty>
    def declaration_list_prime(self):
        # Another declaration follows only if the next token is a qualifier
        if self._lexeme() in ("integer", "boolean", "real"):
            self.print_rule(
                "<Declaration List Prime> -> <Declaration List>"
            )
            self.declaration_list()  # R11

        else:
            self.print_rule(
                "<Declaration List Prime> -> <Empty>"
            )
            self.empty()  # R29

    # R34: <IDs Prime> ::= , <IDs> | <Empty>
    def ids_prime(self):
        if self._lexeme() == ",":
            self.print_rule("<IDs Prime> -> , <IDs>")
            self.match(",")
            self.ids()  # R13

        else:
            self.print_rule("<IDs Prime> -> <Empty>")
            self.empty()  # R29
