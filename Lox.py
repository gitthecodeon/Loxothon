

# a couple basic imports 
from Scanner import Scanner 
import sys

# used for the error flag (isn't technically necessary but when I made it a local
# variable python wasn't reading it)
import errorCatch

errorCatch.hadError = False 

def main():
    if len(sys.argv) > 2:
        print ("Usage: loxothon [script]")
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        runPrompt()


# this will print the tokens in the tokens list
def run(source: str):
    scanner = Scanner(source)
    tokens = [] 
    tokens.append(scanner.scanTokens())

    for token in tokens:
        print(token)

# runs the provided source file
def runFile( path: str):
    run(open(path, "r", encoding = 'utf-8').read())
    if errorCatch.hadError: 
        sys.exit(65)

# runs REPL prompt 
def runPrompt():
    angleb = ">"
    line = []
    while True:
        line.append(input(f"{angleb} "))
        if line[-1].endswith("\\"):
            line[-1] = line[-1].rstrip("\\")
            angleb= ":"
        else:
            run(" ".join(line))
            errorCatch.hadError = False
            line = []
            angleb = ">"      

if __name__ == '__main__':
    main()


