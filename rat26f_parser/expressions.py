# ====================================================
# CPSC 323 - Assignment 2
# RAT26F Recursive Descent Parser
# Expression-related grammar rules
# ====================================================

class ExpressionRules:


    # R23: <Condition> ::= <Expression> <Relop> <Expression>
    def condition(self):
        self.print_rule("<Condition> -> <Expression> <Relop> <Expression>")
        self.expression()  # R25
        self.relop()       # R24
        self.expression()  # R25


    # R24: <Relop> ::= == | != | > | < | <= | >=
    def relop(self):
        token = self.current_token()

        if token is not None and token[1] in ("==", "!=", ">", "<", "<=", ">="):
            self.print_rule(f"<Relop> -> {token[1]}")
            self.match(token[1])
        else:
            raise SyntaxError(f"Expected relop, but found {token}")


    # R25: <Expression> ::= <Term> <Expression Prime>
    def expression(self):
        self.print_rule("<Expression> -> <Term> <Expression Prime>")
        self.term()              # R26
        self.expression_prime()  # R37


    # R26: <Term> ::= <Factor> <Term Prime>
    def term(self):
        self.print_rule("<Term> -> <Factor> <Term Prime>")
        self.factor()      # R27
        self.term_prime()  # R36


    # R27: <Factor> ::= - <Primary> | <Primary>
    def factor(self):
        if self._lexeme() == "-":
            self.print_rule("<Factor> -> - <Primary>")
            self.match("-")
        else:
            self.print_rule("<Factor> -> <Primary>")

        self.primary()  # R28

    # R28: <Primary> ::= <Identifier> <Primary Prime>
    #                  | <Integer> | <Real>
    #                  | ( <Expression> ) | true | false
    def primary(self):
        token_type = self._type()
        lexeme = self._lexeme()

        if token_type == "identifier":
            self.print_rule("<Primary> -> <Identifier> <Primary Prime>")
            self.match("identifier")
            self.primary_prime()  # R30

        elif token_type == "integer":
            self.print_rule("<Primary> -> <Integer>")
            self.match("integer")

        elif token_type == "real":
            self.print_rule("<Primary> -> <Real>")
            self.match("real")

        elif lexeme == "(":
            self.print_rule("<Primary> -> ( <Expression> )")
            self.match("(")
            self.expression()  # R25
            self.match(")")

        elif lexeme in ("true", "false"):
            self.print_rule(f"<Primary> -> {lexeme}")
            self.match(lexeme)

        else:
            raise SyntaxError(
                f"Expected identifier, integer, real, '(', true or false, "
                f"but found {lexeme}"
            )

    # R30: <Primary Prime> ::= ( <IDs> ) | <Empty>
    def primary_prime(self):
        if self._lexeme() == "(":
            self.print_rule("<Primary Prime> -> ( <IDs> )")
            self.match("(")
            self.ids()  # R13
            self.match(")")
        else:
            self.print_rule("<Primary Prime> -> <Empty>")
            self.empty()  # R29

    # R36: <Term Prime> ::= * <Factor> <Term Prime>
    #                    | / <Factor> <Term Prime> | <Empty>
    def term_prime(self):
        lexeme = self._lexeme()

        if lexeme in ("*", "/"):
            self.print_rule(
                f"<Term Prime> -> {lexeme} <Factor> <Term Prime>"
            )
            self.match(lexeme)
            self.factor()      # R27
            self.term_prime()  # R36

        else:
            self.print_rule("<Term Prime> -> <Empty>")
            self.empty()  # R29

    # R37: <Expression Prime> ::= + <Term> <Expression Prime>
    #                          | - <Term> <Expression Prime> | <Empty>
    def expression_prime(self):
        lexeme = self._lexeme()

        if lexeme in ("+", "-"):
            self.print_rule(
                f"<Expression Prime> -> {lexeme} <Term> <Expression Prime>"
            )
            self.match(lexeme)
            self.term()              # R26
            self.expression_prime()  # R37

        else:
            self.print_rule("<Expression Prime> -> <Empty>")
            self.empty()  # R29
