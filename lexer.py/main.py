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
if inputContent: #If data was found, then try to use Lexer
    print("Output:")
    print("-" * 7)
    print(f"{'Token':<25}{'lexeme'}")
    print("-" * 40)
# Run Lexer
    lexer(inputContent)

#This sTATEment is + false 000 #



#Loops until fully checked all tokens