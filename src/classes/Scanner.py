import re
import os

from ..enums.TokenType import TokenType
from .Token import Token


class Scanner:
    def __init__(self) -> None:
        # Regular expressions for matching token types
        # Identifier pattern: matches valid variable or function names (e.g., myVar, x123)
        self.__identifier_regex = r'^[_a-zA-Z][_a-zA-Z0-9]*$'

        # Number pattern: matches integers, floating point numbers, and scientific notation
        self.__number_regex = r'^[-+]?\d+(\.\d+)?([eE][-+]?\d+)?$'

        # Operators: Set of multi-character operators and assignment operators
        self.__operators = {"=:=", "!=", "<>", "=:", "==", ">>",
                            "<<", "++", "&&", "||", ">=", "<=", '+=', "-=", "::", "--", "*", "+", "/", "-", "%", ":", "=","&"}

        # Punctuations: List of symbols used as punctuation in the language
        self.__punctuations = {
            '[', '{', ';', ',', '<', '>', '}', ']', '(', ')'}

        # Keywords: List of reserved words in the language
        self.__keywords = {
            "loop", "agar", "magar", "asm", "else", "new", "this", "auto", "enum", "operator", "throw",
            "bool", "explicit", "private", "true", "break", "export", "protected", "try", "case", "extern",
            "public", "typedef", "catch", "false", "register", "typeid", "char", "float", "typename", "class",
            "for", "return", "union", "const", "friend", "short", "unsigned", "goto", "signed", "using",
            "continue", "if", "sizeof", "virtual", "default", "inline", "static", "void", "delete", "int",
            "volatile", "do", "long", "struct", "double", "mutable", "switch", "while", "namespace"
        }

    # Function to read a line of code from a file
    def readLineOfCode(self, file_path: str) -> list[str]:
        code_lines: list[str] = [] # To store code lines from the file|

        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            return list[str]

        try:
            # Read all lines from the file and add them to code_lines
            with open(file_path, 'r') as file:
                lines: list[str] = file.readlines()
                code_lines.extend(lines)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        # Remove any empty or whitespace-only lines
        code_lines = [line.strip() for line in code_lines if line.strip()]

        return code_lines

    # Function to tokenize a line of code and create Token objects
    def Tokenize(self, LOC: str, lineNumber: int):
        tokens: list[Token] = []

        # Regex pattern to match identifiers, numbers, operators, and punctuation
        pattern = r'(\b[_a-zA-Z][_a-zA-Z0-9]*\b|' + \
            r'\b\d+(\.\d+)?([eE][-+]?\d+)?\b|' + \
            r'==|!=|>=|<=|>>|<<|::|\+\+|--|\+=|-=|=:=|' + \
            r'[\+\-\*/%<>&=|!]=?|[\(\)\[\]{};,<>])'

        # Use regex to find all matches in the line of code (LOC)
        words: list[str] = re.findall(pattern, LOC)

        # Iterate through all the matched words and categorize them into tokens
        for match in words:
            word = match[0] # The matched token is the first element of the tuple

            # Check the word and classify it as operator, punctuation, keyword, number, or identifier
            if word in self.__operators:
                tokens.append(Token(tokenType=TokenType.OPERATOR,
                              value=word, lineNumber=lineNumber))
            elif word in self.__punctuations:
                tokens.append(Token(tokenType=TokenType.PUNCTUATION,
                              value=word, lineNumber=lineNumber))
            elif word in self.__keywords:
                tokens.append(Token(tokenType=TokenType.KEYWORD,
                              value=word, lineNumber=lineNumber))
            elif re.match(self.__number_regex, word):
                tokens.append(Token(tokenType=TokenType.NUMBER,
                              value=word, lineNumber=lineNumber))
            elif re.match(self.__identifier_regex, word):
                tokens.append(Token(tokenType=TokenType.IDENTIFIER,
                              value=word, lineNumber=lineNumber))
            else:
                tokens.append(Token(tokenType=TokenType.UNKNOWN,
                              value=word, lineNumber=lineNumber))

        return tokens
