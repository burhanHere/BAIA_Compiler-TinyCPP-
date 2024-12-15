from ..enums.TokenType import TokenType

# Token class to represent a token with its type, value, and line number
class Token:
    def __init__(self, tokenType: TokenType, value: str, lineNumber: int):
        # Private variables for token type, value (lexeme), and line number
        self.__currentTokenType = tokenType
        self.__lexeme = value  # Assigning value to the private variable
        self.__lineNumber = lineNumber  # Assigning lineNumber to the private variable

    # Getter methods to access the private variables
    def get_current_token_type(self) -> TokenType:
        return self.__currentTokenType

    def get_lexeme(self) -> str:
        return self.__lexeme

    def get_line_number(self) -> int:
        return self.__lineNumber

    # Override the __str__ method to display token info in a readable format
    def __str__(self) -> str:
        return f"<{self.__currentTokenType.value}, {self.__lexeme}, {self.__lineNumber}>"
