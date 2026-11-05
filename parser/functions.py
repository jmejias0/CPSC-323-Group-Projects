# CPSC-323 - Assignment 2
# Function-related grammar rules

class FunctionRules:

    # Third Rule #R3 of RAT26F is <Function Definitions>
    def function_definitions(self):
        self.function_definition()         # R4
        self.function_definitions_prime()  # R31

    # Fourth Rule #R4 of RAT26F is <Function>
    def function_definition(self):
        self.match("function")             
        self.match("identifier")           
        self.match("(")                    
        self.opt_parameter_list()    #R5          
        self.match(")")                    
        self.opt_declaration_list() #R10       
        self.body()       #R9

    # Fifth Rule #R5 of RAT26F is <Opt Parameter List>
    def opt_parameter_list(self):
        token = self.current_token()

        if token is not None and token[0] == "identifier":
            self.parameter_list()  # R6

        elif token is not None and token[1] == ")":
            self.empty()  # R29

        else:
            raise SyntaxError("Expected identifier or )")

     # Sixth Rule #R6 of RAT26F is <Parameter List>
    def parameter_list(self):
        self.parameter()             # R7
        self.parameter_list_prime()  # R32

    # Seventh Rule #R7 of RAT26F is <Parameter>
    def parameter(self):
        self.ids()        # R13
        self.qualifier()  # R8

    # Ninth Rule #R9 of RAT26F is <Body>
    def body(self):
        self.match("{")          # Opening brace
        self.statement_list()    # R14
        self.match("}")          # Closing brace

#*******************************************************************************

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

    #R12 of Rat26 is <declaration>
    def declaration(self):
        self.qualifier()
        self.ids()

    # Thirteenth Rule #R13 of RAT26F is <Ids>
    def ids(self):
        self.match("identifier")  # identifier
        self.ids_prime()          # R34

    #-------------------------------------Jonnathan Section 14-26
    #R14 of Rat26 is <statement_list>
    def statement_list(self):
        self.statement()
        self.statement_list_prime()

    #R15 of Rat26 is <statement>
    def statement(self):
        token = self.current_token()

        if token is not None and token[1] == "{":
            self.compound()         #R16: Compound
        elif token is not None and token[0] == "identifier":
            self.assign()           #R17: Assign
        elif token is not None and token[1] == "if":
            self.if_statement()     #R18
        elif token is not None and token[1] == "return":
            self.return_statement() #R19
        elif token is not None and token[1] == "put":    # FIXED: keyword is put, not print
            self.print_statement()  #R20
        elif token is not None and token[1] == "get":
            self.scan_statement()   #R21
        elif token is not None and token[1] == "while":
            self.while_statement()  #R22
        else:
            raise SyntaxError(f"Expected statement, but found {token}")  # FIXED: added f
        
    # R16: <Compound> ::= { <Statement List> }
    def compound(self):
        self.match("{") 
        self.statement_list()   #R14
        self.match("}")
    
    #R17: <Assign> ::= <Identifier> = <Expression> ;
    def assign(self):
        self.match("identifier")
        self.match("=")
        self.expression()   #R25
        self.match(";")
    
    #R18: <If> ::= if ( <Condition> ) <Statement> <If prime>
    def if_statement(self):
        self.match("if")
        self.match("(")
        self.condition()    #R23
        self.match(")")
        self.statement()    #R15
        self.if_prime()     #R39

    #R19: <Return> ::= return <Return Prime>
    def return_statement(self):
        self.match("return")
        self.return_prime()     #R38

    #R20: <Print> ::= put ( <Expression> );
    def print_statement(self):
        self.match("put")
        self.match("(")         # FIXED: was missing
        self.expression()       #R25
        self.match(")")         # FIXED: was missing
        self.match(";")

    #R21: <Scan> ::= get ( <IDs> );
    def scan_statement(self):
        self.match("get")
        self.match("(")
        self.ids()          #R13
        self.match(")")
        self.match(";")

    #R22: <While> ::= while ( <Condition> ) <Statement>
    def while_statement(self):
        self.match("while")
        self.match("(")
        self.condition()    #R23
        self.match(")")
        self.statement()    #R15

    #R23: <Condition> ::= <Expression> <Relop> <Expression>
    def condition(self):
        self.expression()   #R25
        self.relop()        #R24
        self.expression()   #R25

    #R24: <Relop> ::= == | != | > | < | <= | >=
    def relop(self):
        token = self.current_token()

        # FIXED: the lexer gives "==", "!=", "<=", ">=" as one lexeme,
        # and ">=" was never checked before
        if token is not None and token[1] in ("==", "!=", ">", "<", "<=", ">="):
            self.match(token[1])
        else:
            raise SyntaxError(f"Expected relop, but found {token}")

    #R25: <Expression> ::= <Term> <Expression Prime>
    def expression(self):
        self.term()     #R26
        self.expression_prime() #R37

    #R26: <Term> ::= <Factor> <Term Prime> 
    def term(self):
        self.factor()       #R27
        self.term_prime()   #R36
    #--------------------------------------End of Jonnathan's section

    #-------------------------------------Gio's 27-39 (except R29, R31)

    # ---------- helpers used by the rules below ----------
    def _lexeme(self):
        token = self.current_token()
        return token[1] if token is not None else None

    def _type(self):
        token = self.current_token()
        return token[0].lower() if token is not None else None

    def print_rule(self, rule):
        # Prints the production rule used (turn off with self.show_rules = False)
        if getattr(self, "show_rules", True):
            print("     " + rule)

    # R27: <Factor> ::= - <Primary> | <Primary>
    def factor(self):
        if self._lexeme() == "-":
            self.print_rule("<Factor> -> - <Primary>")
            self.advance()
        else:
            self.print_rule("<Factor> -> <Primary>")
        self.primary()          #R28

    # R28: <Primary> ::= <Identifier> <Primary Prime> | <Integer> | <Real>
    #                    | ( <Expression> ) | true | false
    def primary(self):
        token_type = self._type()
        lexeme = self._lexeme()

        if token_type == "identifier":
            self.print_rule("<Primary> -> <Identifier> <Primary Prime>")
            self.advance()
            self.primary_prime()    #R30
        elif token_type == "integer":
            self.print_rule("<Primary> -> <Integer>")
            self.advance()
        elif token_type == "real":
            self.print_rule("<Primary> -> <Real>")
            self.advance()
        elif lexeme == "(":
            self.print_rule("<Primary> -> ( <Expression> )")
            self.advance()
            self.expression()       #R25
            self.match(")")
        elif lexeme in ("true", "false"):
            self.print_rule(f"<Primary> -> {lexeme}")
            self.advance()
        else:
            raise SyntaxError(
                f"Expected identifier, integer, real, '(', true or false, but found {lexeme}"
            )

    # R30: <Primary Prime> ::= ( <IDs> ) | <Empty>
    def primary_prime(self):
        if self._lexeme() == "(":
            self.print_rule("<Primary Prime> -> ( <IDs> )")
            self.advance()
            self.ids()              #R13
            self.match(")")
        else:
            self.print_rule("<Primary Prime> -> <Empty>")
            self.empty()            #R29

    # R32: <Parameter List Prime> ::= , <Parameter List> | <Empty>
    def parameter_list_prime(self):
        if self._lexeme() == ",":
            self.print_rule("<Parameter List Prime> -> , <Parameter List>")
            self.advance()
            self.parameter_list()   #R6
        else:
            self.print_rule("<Parameter List Prime> -> <Empty>")
            self.empty()            #R29

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
            self.advance()
            self.ids()              #R13
        else:
            self.print_rule("<IDs Prime> -> <Empty>")
            self.empty()            #R29

    # R35: <Statement List Prime> ::= <Statement List> | <Empty>
    def statement_list_prime(self):
        # Another statement follows only if the next token can start one
        if self._type() == "identifier" or self._lexeme() in ("{", "if", "return", "put", "get", "while"):
            self.print_rule("<Statement List Prime> -> <Statement List>")
            self.statement_list()   #R14
        else:
            self.print_rule("<Statement List Prime> -> <Empty>")
            self.empty()            #R29

    # R36: <Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>
    def term_prime(self):
        lexeme = self._lexeme()
        if lexeme in ("*", "/"):
            self.print_rule(f"<Term Prime> -> {lexeme} <Factor> <Term Prime>")
            self.advance()
            self.factor()           #R27
            self.term_prime()       #R36
        else:
            self.print_rule("<Term Prime> -> <Empty>")
            self.empty()            #R29

    # R37: <Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>
    def expression_prime(self):
        lexeme = self._lexeme()
        if lexeme in ("+", "-"):
            self.print_rule(f"<Expression Prime> -> {lexeme} <Term> <Expression Prime>")
            self.advance()
            self.term()             #R26
            self.expression_prime() #R37
        else:
            self.print_rule("<Expression Prime> -> <Empty>")
            self.empty()            #R29

    # R38: <Return Prime> ::= ; | <Expression> ;
    def return_prime(self):
        if self._lexeme() == ";":
            self.print_rule("<Return Prime> -> ;")
            self.advance()
        else:
            self.print_rule("<Return Prime> -> <Expression> ;")
            self.expression()       #R25
            self.match(";")

    # R39: <If Prime> ::= fi | else <Statement> fi
    def if_prime(self):
        lexeme = self._lexeme()
        if lexeme == "fi":
            self.print_rule("<If Prime> -> fi")
            self.advance()
        elif lexeme == "else":
            self.print_rule("<If Prime> -> else <Statement> fi")
            self.advance()
            self.statement()        #R15
            self.match("fi")
        else:
            raise SyntaxError(f"Expected fi or else, but found {lexeme}")
    #--------------------------------------End of Giovani's section


    
    # Thirty-first Rule #R31 of RAT26F is <Function Definitions Prime>
    def function_definitions_prime(self):
        token = self.current_token()

        if token is not None and token[1] == "function":
            self.function_definitions()  # R3
        else:
            self.empty() #R29