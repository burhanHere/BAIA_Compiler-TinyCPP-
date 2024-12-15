import sys
import os

from src.classes.Scanner import Scanner
from src.classes.Token import Token

# Driver code to run the scanner
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise "Code file not specified"

    # Create an instance of the Scanner class
    scanner: Scanner = Scanner()

    # Read lines of code from a file
    LsOC: list[str] = scanner.readLineOfCode(
        file_path=sys.argv[1])
    # file_path='targetCodeFiles\\InitialTesting\\MyCodeFile4.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\BasicVariableDeclarations.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\CommentsAndStrings.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\ComplexExpressions.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\ConditionalStatements.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\EdgeCasesWithSpecialCharacters.BAIA') # exception in test case
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\FunctionCallsWithArguments.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\FunctionDefinition.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\LoopingStatements.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\NestedLoopsAndConditions.BAIA')
    # file_path='targetCodeFiles\\DIfferentTypeOfCodes\\UsingCustomOperators.BAIA')

    tokens: list[Token] = None  # List to store all tokens
    lineNumber: int = 1  # Line number counter

    # Process each line in the file
    for i in LsOC:
        # Tokenize each line and get a list of tokens for that line
        newTokens: list[Token] = scanner.Tokenize(LOC=i, lineNumber=lineNumber)

        # If tokens is None (first iteration), initialize it with newTokens
        if tokens == None:
            tokens = newTokens
        else:
            tokens += newTokens  # Add new tokens to the existing list

        lineNumber += 1  # Increment line number for the next iteration

    # Print all the tokens found in the code
    for token in tokens:
        print(token)
