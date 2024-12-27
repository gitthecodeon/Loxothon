import errorCatch

# In this module we'll neatly store our error catching for the scanner
class scanErr(Exception):
    def __init__(self, line, message):
        self.line = line
        self.message = message

    # points out where the error happend and what type it is
    def report(self):
        print(f'[line {self.line}] Error: {self.message}')
        errorCatch.hadError = True