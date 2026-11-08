
# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# Statement-related grammar rules
# ====================================================

class StatementRules:

    # R14: <Statement List> ::= <Statement> <Statement List Prime>
    def statement_list(self):
        self.print_rule(
            "<Statement List> -> <Statement> <Statement List Prime>"
        )
        self.statement()             # R15
        self.statement_list_prime()  # R35

    # R15: <Statement> ::= <Compound> | <Assign> | <If>
    #                    | <Return> | <Print> | <Scan> | <While>
    def statement(self):
        lexeme = self._lexeme()

        if lexeme == "{":
            self.print_rule("<Statement> -> <Compound>")
            self.compound()  # R16

        elif self._type() == "identifier":
            self.print_rule("<Statement> -> <Assign>")
            self.assign()  # R17

        elif lexeme == "if":
            self.print_rule("<Statement> -> <If>")
            self.if_statement()  # R18

        elif lexeme == "return":
            self.print_rule("<Statement> -> <Return>")
            self.return_statement()  # R19

        elif lexeme == "put":
            self.print_rule("<Statement> -> <Print>")
            self.print_statement()  # R20

        elif lexeme == "get":
            self.print_rule("<Statement> -> <Scan>")
            self.scan_statement()  # R21

        elif lexeme == "while":
            self.print_rule("<Statement> -> <While>")
            self.while_statement()  # R22

        else:
            raise SyntaxError(
                f"Expected statement, but found {self.current_token()}"
            )

    # R16: <Compound> ::= { <Statement List> }
    def compound(self):
        self.print_rule("<Compound> -> { <Statement List> }")
        self.match("{")
        self.statement_list()  # R14
        self.match("}")

    # R17: <Assign> ::= <Identifier> = <Expression> ;
    def assign(self):
        self.print_rule("<Assign> -> <Identifier> = <Expression> ;")
        self.match("identifier")
        self.match("=")
        self.expression()  # R25
        self.match(";")

    # R18: <If> ::= if ( <Condition> ) <Statement> <If Prime>
    def if_statement(self):
        self.print_rule(
            "<If> -> if ( <Condition> ) <Statement> <If Prime>"
        )
        self.match("if")
        self.match("(")
        self.condition()  # R23
        self.match(")")
        self.statement()  # R15
        self.if_prime()   # R39

    # R19: <Return> ::= return <Return Prime>
    def return_statement(self):
        self.print_rule("<Return> -> return <Return Prime>")
        self.match("return")
        self.return_prime()  # R38

    # R20: <Print> ::= put ( <Expression> ) ;
    def print_statement(self):
        self.print_rule("<Print> -> put ( <Expression> ) ;")
        self.match("put")
        self.match("(")
        self.expression()  # R25
        self.match(")")
        self.match(";")

    # R21: <Scan> ::= get ( <IDs> ) ;
    def scan_statement(self):
        self.print_rule("<Scan> -> get ( <IDs> ) ;")
        self.match("get")
        self.match("(")
        self.ids()  # R13
        self.match(")")
        self.match(";")

    # R22: <While> ::= while ( <Condition> ) <Statement>
    def while_statement(self):
        self.print_rule(
            "<While> -> while ( <Condition> ) <Statement>"
        )
        self.match("while")
        self.match("(")
        self.condition()  # R23
        self.match(")")
        self.statement()  # R15

    # R35: <Statement List Prime> ::= <Statement List> | <Empty>
    def statement_list_prime(self):
        lexeme = self._lexeme()

        if self._type() == "identifier" or lexeme in (
            "{", "if", "return", "put", "get", "while"
        ):
            self.print_rule(
                "<Statement List Prime> -> <Statement List>"
            )
            self.statement_list()  # R14

        else:
            self.print_rule("<Statement List Prime> -> <Empty>")
            self.empty()  # R29

    # R38: <Return Prime> ::= ; | <Expression> ;
    def return_prime(self):
        if self._lexeme() == ";":
            self.print_rule("<Return Prime> -> ;")
            self.match(";")

        else:
            self.print_rule("<Return Prime> -> <Expression> ;")
            self.expression()  # R25
            self.match(";")

    # R39: <If Prime> ::= fi | else <Statement> fi
    def if_prime(self):
        lexeme = self._lexeme()

        if lexeme == "fi":
            self.print_rule("<If Prime> -> fi")
            self.match("fi")

        elif lexeme == "else":
            self.print_rule(
                "<If Prime> -> else <Statement> fi"
            )
            self.match("else")
            self.statement()  # R15
            self.match("fi")

        else:
            raise SyntaxError(
                f"Expected fi or else, but found {lexeme}"
            )
