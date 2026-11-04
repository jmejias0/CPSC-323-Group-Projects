# CPSC-323 - Assignment 2
# Function-related grammar rules

import token


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

    # Twelfth Rule #R12 of RAT26F is <Declaration>
    def declaration(self):
        self.qualifier()  # R8
        self.ids()        # R13
       
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
        elif token is not None and token[1] == "print":
            self.print_statement()  #R20
        elif token is not None and token[1] == "get":
            self.scan_statement()   #R21
        elif token is not None and token[1] == "while":
            self.while_statement()  #R22
        else:
            raise SyntaxError("Expected statement, but found {token}")
        
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
    
    #R18 of Rat26 is <If>
    #R18: <If> ::= if ( <Condition> ) <Statement> <If prime>
    def If(self):
        #R21: <Scan> ::= get ( <IDs> );
    #--------------------------------------End of Jonnathan's section


    
    # Thirty-first Rule #R31 of RAT26F is <Function Definitions Prime>
    def function_definitions_prime(self):
        token = self.current_token()

        if token is not None and token[1] == "function":
            self.function_definitions()  # R3
        else:
            self.empty() #R29
