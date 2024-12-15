from enum import Enum


# TokenType Enum to categorize different types of tokens
class TokenType(Enum):
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    PUNCTUATION = "PUNCTUATION"
    KEYWORD = "KEYWORD"
    UNKNOWN = "UNKNOWN"
