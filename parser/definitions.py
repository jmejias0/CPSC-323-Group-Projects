# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# Declaration-related grammar rules
# ====================================================

class DefinitionRules:

    # Eighth Rule #R8 of RAT26F is <Qualifier>
    def qualifier(self):
        token = self.current_token()

        if token is not None and token[1] == "integer":
            self.match("integer")  # Integer qualifier

        elif token is not None and token[1] == "boolean":
            self.match("boolean")  # Boolean qualifier

        elif token is not None and token[1] == "real":
            self.match("real")  # Real qualifier

        else:
            raise SyntaxError("Expected integer, boolean, or real")

    # Tenth Rule #R10 of RAT26F is <Opt Declaration List>
    def opt_declaration_list(self):
        token = self.current_token()

        if token is not None and token[1] in ["integer", "boolean", "real"]:
            self.declaration_list()  # R11

        else:
            self.empty()  # R29

    # Eleventh Rule #R11 of RAT26F is <Declaration List>
    def declaration_list(self):
        self.declaration()             # R12
        self.match(";")                # Semicolon
        self.declaration_list_prime()  # R33

    # Twelfth Rule #R12 of RAT26F is <declaration>
    def declaration(self):
        self.qualifier()
        self.ids()

    # Thirteenth Rule #R13 of RAT26F is <Ids>
    def ids(self):
        self.match("identifier")  # identifier
        self.ids_prime()          # R34

     # R33: <Declaration List Prime> ::= <Declaration List> | <Empty>
    def declaration_list_prime(self):
        # Another declaration follows only if the next token is a qualifier
        if self._lexeme() in ("integer", "boolean", "real"):
            self.print_rule("<Declaration List Prime> -> <Declaration List>")
            self.declaration_list() #R11
        else:
            self.print_rule("<Declaration List Prime> -> <Empty>")
            self.empty()            #R29

    # R34: <IDs Prime> ::= , <IDs> | <Empty>
    def ids_prime(self):
        if self._lexeme() == ",":
            self.print_rule("<IDs Prime> -> , <IDs>")
            self.match(",")
            self.ids()              #R13
        else:
            self.print_rule("<IDs Prime> -> <Empty>")
            self.empty()            #R29