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
from lexer import lexer, SEPARATORS, SIMPLE_OPS, DOUBLE_OPS, keywords
# Ask the user for an input file directory
inFile = input("Enter Input File directory: ")
try:    #Attempt to open input file
    file = open(inFile, "r")
    outputFile = open("output.txt", "w")
    inputContent = file.read()
    file.close()
except FileNotFoundError:
    print("ERR, no valid input file at this directory.")
# Print Template
if inputContent: #If data was found, then print template to prep for lexer
    outputFile.write("Output:\n")
    outputFile.write("-" * 7 + "\n")
    outputFile.write(f"{'Token':<25}{'lexeme'}\n")
    outputFile.write("-" * 40 + "\n")

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
tokenType = ""  # Current type of the token
inComment = False  # Flag to check if we are in a comment, so we can skip the lexer and move to next character

i = 0

while i < len(inputContent):
    char = inputContent[i]

    # Handle operators
    two_chars = inputContent[i:i+2]
    
    if two_chars in DOUBLE_OPS:
        if tokenVal != "":
            outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")
    
        tokenVal = ""
        tokenPrev = ""
        tokenType = ""
    
        outputFile.write(f"{'operator':<25}{two_chars}\n")
        i += 2
        continue

    # start/end comment
    if char == '!':
        # If we are entering a comment and there is a token waiting,
        # print that token before ignoring the comment
        if not inComment and tokenVal != "":
            outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")
            tokenVal = ""
            tokenPrev = ""
            tokenType = ""

        inComment = not inComment
        i += 1
        continue

    #ignore characters in comment
    if inComment:
        i += 1
        continue

     # Handle spaces, tabs, and newlines
    if char.isspace():
        if tokenVal != "":
            outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")
            tokenVal = ""
            tokenPrev = ""
            tokenType = ""
        i += 1
        continue    

    # Handle separators 
    if char in SEPARATORS:
        if tokenVal != "":
            outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")

        tokenVal = ""
        tokenPrev = ""
        tokenType = ""

        outputFile.write(f"{'separator':<25}{char}\n")
        i += 1
        continue

    if char in SIMPLE_OPS:
        if tokenVal != "":
            outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")

        tokenVal = ""
        tokenPrev = ""
        tokenType = ""

        outputFile.write(f"{'operator':<25}{char}\n")
        i += 1
        continue

    if tokenPrev == "":
        tokenPrev = lexer(char)                         # Set the initial Token Value
        tokenType = tokenPrev
        #print("Initial token found! "+ tokenPrev)
    else:
        #print("Running Lexer for " + tokenVal + char)
        tokenType = lexer(tokenVal + char)              # Check what type of token returns from prev char + current char
        #print(f"{tokenType:<25}{tokenVal + char}")
        if tokenType != tokenPrev and tokenType != "keyword":                      # Check if the new token isnt the same type as previous
            #if char != '.':     # Check for special cases involving digits
            if char != '.' and tokenType != "Real":  
                
                #if tokenVal[-1] == '.':                 # Check if '.' is at the end
                    #tokenVal = tokenVal[:-1]            # Remove dot so digit value is valid to print
                outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")     # Print token and value
                tokenVal = ""                           # Empty value to make room for next
                tokenPrev = ""  
    if not char.isspace():                    # Empty type since whats next could be anything
        #print("Added " + char + ", token type: " + tokenType + ", previous type: " + tokenPrev)
        tokenVal += char
        tokenPrev = tokenType
    i += 1
if tokenVal != "":
    tokenPrev = lexer(tokenVal)                                 # Check for type one more time
    outputFile.write(f"{tokenPrev:<25}{tokenVal}\n")          # Print last token since it missed the loop's window to be printed

outputFile.close()
#testcase 1, if it passes this properly then we are close to being done
#This sTATEment is + false 000 #