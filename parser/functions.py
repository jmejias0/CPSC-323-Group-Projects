
# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# Function-related grammar rules
# ====================================================

class FunctionRules:

    # R3: <Function Definitions> ::= <Function> <Function Definitions Prime>
    def function_definitions(self):
        self.print_rule(
            "<Function Definitions> -> <Function> <Function Definitions Prime>"
        )
        self.function_definition()         # R4
        self.function_definitions_prime()  # R31

    # R4: <Function> ::= function <Identifier> ( <Opt Parameter List> )
    #                   <Opt Declaration List> <Body>
    def function_definition(self):
        self.print_rule(
            "<Function> -> function <Identifier> ( <Opt Parameter List> ) "
            "<Opt Declaration List> <Body>"
        )
        self.match("function")
        self.match("identifier")
        self.match("(")
        self.opt_parameter_list()     # R5
        self.match(")")
        self.opt_declaration_list()   # R10
        self.body()                   # R9

    # R5: <Opt Parameter List> ::= <Parameter List> | <Empty>
    def opt_parameter_list(self):
        if self._type() == "identifier":
            self.print_rule("<Opt Parameter List> -> <Parameter List>")
            self.parameter_list()  # R6

        elif self._lexeme() == ")":
            self.print_rule("<Opt Parameter List> -> <Empty>")
            self.empty()  # R29

        else:
            raise SyntaxError("Expected identifier or )")

    # R6: <Parameter List> ::= <Parameter> <Parameter List Prime>
    def parameter_list(self):
        self.print_rule(
            "<Parameter List> -> <Parameter> <Parameter List Prime>"
        )
        self.parameter()             # R7
        self.parameter_list_prime()  # R32

    # R7: <Parameter> ::= <IDs> <Qualifier>
    def parameter(self):
        self.print_rule("<Parameter> -> <IDs> <Qualifier>")
        self.ids()        # R13
        self.qualifier()  # R8

    # R9: <Body> ::= { <Statement List> }
    def body(self):
        self.print_rule("<Body> -> { <Statement List> }")
        self.match("{")
        self.statement_list()  # R14
        self.match("}")

    # R31: <Function Definitions Prime> ::= <Function Definitions> | <Empty>
    def function_definitions_prime(self):
        if self._lexeme() == "function":
            self.print_rule(
                "<Function Definitions Prime> -> <Function Definitions>"
            )
            self.function_definitions()  # R3

        else:
            self.print_rule("<Function Definitions Prime> -> <Empty>")
            self.empty()  # R29

    # R32: <Parameter List Prime> ::= , <Parameter List> | <Empty>
    def parameter_list_prime(self):
        if self._lexeme() == ",":
            self.print_rule(
                "<Parameter List Prime> -> , <Parameter List>"
            )
            self.match(",")
            self.parameter_list()  # R6

        else:
            self.print_rule("<Parameter List Prime> -> <Empty>")
            self.empty()  # R29
