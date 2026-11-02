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
        self.parameter_list()    #R5          
        self.match(")")                    
        self.opt_declaration_list() #R10       
        self.body()       #R9

    # Thirty-first Rule #R31 of RAT26F is <Function Definitions Prime>
    def function_definitions_prime(self):
        token = self.current_token()

        if token is not None and token[1] == "function":
            self.function_definitions()  # R3
        else:
            self.empty() #R29