# Imports
import sys
import fileinput
import argparse
import fileinput

# Global variables
version = "1.1.0"

# Methods
def parseInput():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_mutually_exclusive_group()
    parser.add_argument('-v', '--version', action="version",version="shell.py version --> " + version,help="Display current version info")
    parser.add_argument('-d','-dir','--directory',action="store_true",help="List file contents of the input drive")
    parser.add_argument('-h','-H', '--help','-?', action='help', default=argparse.SUPPRESS,help='Show this help message and exit.')
    parser.add_argument('-f','--file', type=str, help="Specify a formatted drive file")
    args = parser.parse_args()
    return args

def evalInfo(argsData):
    if not sys.stdin.isatty():
        data = fileinput.input()
        printStdIn(data)
        data.close()
        

    if argsData.file != None:
        datafile = open(argsData.file)
        printFile(datafile)
    #if argsData.version:
    #    print("shell.py version --> " + version)
    #    sys.exit(1)
    if argsData.directory:
        print("dir here")

def printFile(file):
    count = 0
    for line in file:
            if count > 1:
                sys.stdout.write(line[3:])
            count += 1

def printStdIn(stdIn):
    for line in stdIn:
            if stdIn.lineno() > 2:
                sys.stdout.write(line[3:])

# Main

parsed = parseInput()
evalInfo(parsed)
    