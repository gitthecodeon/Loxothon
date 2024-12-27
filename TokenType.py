
from enum import Enum, auto

# this is where we store all of the different types of Tokens
class TokenType(Enum):
    # Single character tokens
    LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE = [auto() for i in range(4)]
    COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR = [auto() for i in range(7)]

    # One or two character tokens here
    BANG, BANG_EQUAL = [auto() for i in range(2)]
    EQUAL, EQUAL_EQUAL = [auto() for i in range(2)]
    GREATER, GREATER_EQUAL = [auto() for i in range(2)]
    LESS, LESS_EQUAL = [auto() for i in range(2)]

    # Literals
    IDENTIFIER, STRING, NUMBER = [auto() for i in range(3)]

    # Keywords
    AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR = [auto() for i in range(9)]
    PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE = [auto() for i in range(7)]

    # end of file
    EOF = auto()