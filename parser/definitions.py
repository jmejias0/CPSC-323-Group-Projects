


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

