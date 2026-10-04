#===================================================================
# Programmers:Jose Mejias, Giovanni Arredondo, Jonnathan Quijada
# Assignment Number: 1
# Class:CPSC-323
#===================================================================
#   GetInput from inFile
#   Print Template
#   Use Lexer to check data
#   Print results
#===================================================================
# TEMPORARY COMMENT, REMOVE LATER: "C:\Users\Mama Karen\Desktop\College\Fullerton\Fall 2026\compilers\a1inFile1.txt"


# MAIN
# Variables
from lexer import lexer
# Ask the user for an input file directory
inFile = input("Enter Input File directory: ")
try:    #Attempt to open input file
    file = open(inFile, "r")
    inputContent = file.read()
    file.close()
except FileNotFoundError:
    print("ERR, no valid input file at this directory.")
# Print Template
if inputContent: #If data was found, then print template to prep for lexer
    print("Output:")
    print("-" * 7)
    print(f"{'Token':<25}{'lexeme'}")
    print("-" * 40)


#Parsing into the Lexer EXPLAINED

# Begin parsing characters into Lexer
    #If the current character is a space, then skip lexer and move to next character
        # if the previous token is blank, set it to the current token value
        # else, Lexer tells you what kind of token it currently is
        # Check if the token changed from when you last checked it
          #if it did, check if the current character is a '.'
             # If it isn't, check if you currently have a REAL
               # If you dont, then its a invalid digit (0.), so remove the . to print correct
               # Print the current token and its associated value
               # reset the buffers so they can be reused for the next token
        # add next token to Token Val
    # Check 1 more time for token type
    # Print last token since it missed the loop's window to be printed



tokenVal = ""   # The value of the token that is remembered through the loop, printed after done
tokenPrev = ""  # the previous token type to be compared to the current token type
for char in inputContent:
    if char != " ":
        if tokenPrev == "":
            tokenPrev = lexer(char)                         # Set the initial Token Value
        else:
            tokenType = lexer(tokenVal + char)              # Check what type of token returns from prev char + current char
            if tokenType != tokenPrev:                      # Check if the new token isnt the same type as previous
                if char != '.':                             # Check for special cases involving digits
                    if tokenType != "Real":                 # Check for special cases involving real numbers
                        if tokenVal[-1] == '.':             # Check if a . is at the end
                             tokenVal = tokenVal[:-1]       # Remove dot so digit value is valid to print
                        print(f"{tokenPrev:<25}{tokenVal}") # Print token and value
                        tokenVal = ""                       # Empty value to make room for next
                        tokenPrev = ""                      # Empty type since whats next could be anything
        tokenVal += char
tokenPrev = lexer(tokenVal)                                 # Check for type one more time
print(f"{tokenPrev:<25}{tokenVal}")                         # File is done, print last token and its value and were done
# End of Main()

#testcase 1, if it passes this properly then we are close to being done
#This sTATEment is + false 000 #