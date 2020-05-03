# Imports
import sys
import fileinput
import argparse
import fileinput

# Global variables
version = "1.0.0"

def parseInput():
    parser = argparse.ArgumentParser(add_help=False)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--version", action="store_true",help="Display current version info")
    group.add_argument("-q", "--quiet", action="store_true",help="Display less information")
    parser.add_argument('-h', '--help',"-?", action='help', default=argparse.SUPPRESS,help='Show this help message and exit.')
    parser.add_argument("-f","--file", type=str, help="The file to output")
    args = parser.parse_args()
    return args

def evalInfo(argsData):
    
    isStdin = True
    for line in fileinput.input():
        if not fileinput.isstdin():
            isStdin = False
            break
        print(line)
    fileinput.close()

    if argsData.file != None:
        datafile = open(argsData.file)
        printFile(datafile)
    if argsData.version:
        print("shell.py version --> " + version)

def printFile(file):
    count = 0
    for line in file:
            count += 1
            if count > 1:
                print(line) # remove 1st two chars later

def printStdIn(stdIn):
    with stdIn as lines:
        for line in lines:
            if lines.lineno() != 1:
                print(lines.lineno(),line)

# def test():
    # args = sys.argv

    # Input processing
    # test = fileinput.input()
    # Flags
    # if args.__len__() == 1 and test:
        # sys.stdout.write("Help documentation...\n")
    # else:
        # Each case represents a flag at any specific element in the args array
        # for i in range(1,args.__len__()):
            # if args.__len__() == 1:
                # printStdIn()
            # if args[i] == "-v" or args[i] == "-V" or args[i] == "--get-version":
                # sys.stdout.write("Version 1.0.0\n")
            #if args[i] == "-h" or args[i] == "-H" or args[i] == "-?" or args[i] == "--Help" or args[i] == "--get-help":
            #    sys.stdout.write("Help documentation...")
            # if args[i] == "-f" or args[i] == "-F" or args[i] == "--input-file" or args[i] == "--Input-File":
                # inputfile = open(args[i + 1])
                # break
            # else:
                # inputfile = open(args[i])

parsed = parseInput()
evalInfo(parsed)
    