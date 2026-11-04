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

    # Eighth Rule #R8 of RAT26F is <Qualifier>
    def qualifier(self):
        token = self.current_token()

        if token is not None and token[1] == "integer":
            self.match("integer")  # R11

        elif token is not None and token[1] == "boolean":
            self.match("boolean")  # R12

        elif token is not None and token[1] == "real":
            self.match("real")  # R33

        else:
            raise SyntaxError("Expected integer, boolean, or real")

    # Ninth Rule #R9 of RAT26F is <Body>
    def body(self):
        self.match("{")          # Opening brace
        self.statement_list()    # R14
        self.match("}")          # Closing brace

    # Tenth Rule #R10 of RAT26F is <Opt Declaration List>
    def opt_declaration_list(self):
        token = self.current_token()

        if token is not None and token[1] in ["integer", "boolean", "real"]:
            self.declaration_list()  # R11

        else:
            self.empty()  # R29
            
    #R11 of Rat26 is <declaration_list>
    def declaration_list(self):
        self.declaration()
        self.declaraction_list_prime()
    #2nd part of R11
    def declaraction_list_prime(self):
        token = self.current_token()
        if token in ["int", "float", "char"]:
            declaration_list()
        else:
            return
       
    #R12 of Rat26 is <declaration>
    def declaration(self):
        self.qualifier()
        self.ids()

#Jonnathan's Incomplete Section
    #R13 of Rat26 is <ids>
    def ids(self):
        token = self.current_token()
#R14 of Rat26 is <statement_list>
def statement_list(self):
#R15 of Rat26 is <statement>
def statement(self):
#R16 of Rat26 is <compound>
def compound(self):
#R17 of Rat26 is <assign>
def assign(self):
#R18 of Rat26 is <If>
def If(self):
#End of Jonnathan's incomplete section


    
    # Thirty-first Rule #R31 of RAT26F is <Function Definitions Prime>
    def function_definitions_prime(self):
        token = self.current_token()

        if token is not None and token[1] == "function":
            self.function_definitions()  # R3
        else:
            self.empty() #R29
