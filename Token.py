import TokenType

# this is where we set up the token class that contains information 
# about the token that will be helpful for error handling
class Token:
    def __init__(self, type: TokenType, lexeme: str, literal: object, line: int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self):
        return '%s %s %s' %(self.type, self.lexeme, self.literal)
        