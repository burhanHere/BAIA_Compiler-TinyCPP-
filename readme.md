# Lexical Analyzer (Scanner)

This project is a lexical analyzer (scanner) designed to tokenize source code. It reads lines of code from a specified file, uses regular expressions to identify and categorize various tokens such as identifiers, numbers, operators, punctuations, and keywords, and then outputs these tokens for further processing.

## Features

- **Tokenization:** Uses regular expressions to identify and categorize different types of tokens.
- **Token Types:** Supports identifiers, numbers, operators, punctuations, keywords, and unknown tokens.
- **Line-by-Line Processing:** Reads source code line by line for efficient tokenization.
- **Token Class:** Represents individual tokens with their type, value, and line number for easy management and debugging.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/burhanHere/BAIA_Compiler-TinyCPP-.git
```
2. Navigate to the project directory:
    ```bach
    cd your/directory
    ```

## Usage
1. Place your source code file in the project directory.
2. Run the scanner with the source code file as an argument:
```bash
python main.py path/to/your/sourcecodeFileWithExtention
```
3. The scanner will output a list of tokens found in the source code.

## File Structure
```bash
main.py: Driver code to run the scanner.
src/classes/Scanner.py: Contains the Scanner class for reading and tokenizing source code.
src/classes/Token.py: Contains the Token class to represent individual tokens.
src/enums/TokenType.py: Defines the TokenType enum for different token categories.
```

## Author
 Muhammad Burhan - https://github.com/burhanHere
 