
from TokenType import TokenType
from Token import Token
from scanErr import scanErr

# right now all the happens is the the tokens from the source file get scanned and spat out in the terminal
# of course, it will get fleshed out as the interpreter gets built
class Scanner:
    def __init__ (self, source: str):
        self.source = source
        self.tokens = []

        self.start = 0

        # aware of the code smell (maybe this is a future me problem)
        self.current = 0
        self.line = 1

     
    def scanTokens(self):
        while (not self.isAtEnd()):
            self.start = self.current
            self.scanToken()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens
    
    # a helper function to tell us if the scanner has reached 
    # the end (all the characters have been consumed)
    def isAtEnd(self) -> bool:
        return self.current >= len(self.source)
    
    # now we add the tokens that the scanner will recognize
    def scanToken(self):
        c = self.advance()
        # this is a switch statement for Pytyhon that goes through an asortment
        # of important characters 
        match c:
            case '(': 
                return self.addToken(TokenType.LEFT_PAREN)
            case ')':
                return self.addToken(TokenType.RIGHT_PAREN)
            case '{': 
                return self.addToken(TokenType.LEFT_BRACE)
            case '}': 
                return self.addToken(TokenType.RIGHT_BRACE)
            case ',': 
                return self.addToken(TokenType.COMMA)
            case '.': 
                return self.addToken(TokenType.DOT)
            case '-': 
                return self.addToken(TokenType.MINUS)
            case '+': 
                return self.addToken(TokenType.PLUS)
            case ';': 
                return self.addToken(TokenType.SEMICOLON)
            case '*': 
                return self.addToken(TokenType.STAR)
            
            case '!':
                return self.addToken(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG) 
            case '=':
                return self.addToken(TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL) 
            case '<':
                return self.addToken(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS_EQUAL) 
            case '>':
                return self.addToken(TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER_EQUAL) 
            
            case '/':
                if (self.match('/')):
                    while self.peek() != '\n' and not self.isAtEnd(): 
                        self.advance()
                    else:
                        self.addToken(TokenType.SLASH)

            case ' ':
                return
            case '\r':
                return
            case '\t':
                return
            case '\n':
                self.line += 1
            
            case '"':
                return self.string()
            
            
            case 'o':
                if (self.match('r')):
                    return self.addToken(TokenType.OR)

            # our default case 
            case _:
                if (self.isDigit(c)):
                    self.number()
                elif (self.isAlpha(c)):
                    self.identifier()
                else:
                    return self.error(self, "invalid character")
            
    # returns the next character after consuming it        
    def advance(self) -> str:
        # updating the current position (yes I know this is a code smell... Maybe I'll fix it later)
        self.current += 1
        return self.source[self.current - 1]
    
    # Only one addToken function since function overloading is not supported in Python
    def addToken(self, type:TokenType, literal: object = None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    # check if the given tokens match what the scanner has in its list
    def match(self, expected) -> bool:
        # makes sure it stops when it reaches the end
        if (self.isAtEnd()):
            return False
        if (self.source[self.current] != expected):
            return False
        
        # update the current position even though this isn't the best way to do that
        self.current += 1
        return True
    
    # looks at the token in the current position
    def peek(self):
        if (self.isAtEnd()):
            return '\0'
        return self.source[self.current]
    

    def string(self):
        while (self.peek() != '"' and not self.isAtEnd()):
            if (self.peek() == '\n'):
                self.line += 1
            self.advance()
        
        if (self.isAtEnd()):
            self.error(self.line, "Unterminated string.")
            return
        
        self.advance()

        value = self.source[self.start + 1: self.current - 1]
        self.addToken(TokenType.STRING, value)

    def isDigit(self, c):
        return c >= '0' and c <= '9'
    
    
    def number(self):
        while (self.isDigit(self.peek())):
            self.advance()
        if (self.peek() == '.' and self.isDigit(self.peekNext())):
            self.advance
            while (self.isDigit(self.peek())):
                self.advance()

        self.addToken(TokenType.NUMBER, float(self.source[self.start: self.current]))

    # takes a look at the next token
    def peekNext(self):
        if (self.current + 1 >= len(self.source)):
            return '\0'
        return self.source[self.current + 1]
    

    def identifier(self):
        while (self.isAlphaNumeric(self.peek())):
            self.advance()
        text = self.source[self.start: self.current]
        token_type = keywords.get(text)
        if token_type is None: 
            token_type = TokenType.IDENTIFIER
        self.addToken(token_type)


    def isAlpha(self, c):
        return (c >= 'a' and c <= 'z' or (c >= 'A' and c <= 'Z') or c == '_')
    
    def isAlphaNumeric(self, c):
        return self.isAlpha(c) or self.isDigit(c)
    
    def error(self, token, message):
        err = scanErr(self.line, message)
        err.report() 


# our library of keywords
    
keywords = {
    "and": TokenType.AND,
    "class": TokenType.CLASS,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "fun": TokenType.FUN,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "var": TokenType.VAR,
    "while": TokenType.WHILE,
    }
    
