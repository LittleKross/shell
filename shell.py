# Imports
import sys
import os
import fileinput
import argparse
import fileinput

# Global variables
version = "1.1.2"

def verifyFile(file):
    return os.path.exists(os.path.join(os.getcwd(), file))

def crawlRawDisk(*args):
    if len(args) == 1:
        row = 0
        crawlRawDisk(args[0],row)
    if len(args) == 2:
        currentCluster = args[0][args[1]]
        print(currentCluster)
        nextCluster = args[0][args[1]][1:3]
        print(nextCluster)

def collectRawDisk(data,file):
    count = 0
    for line in file:
            if count > 1:
                data.append(line[3:])
            count += 1
    return data

def printRawDisk(disk):
    for line in disk:
        sys.stdout.write(line)

def evalArgs(argsData):
    try:
        # Predefine vars
        data = []
        fileName = None
        file = None

        # Check for stdin
        if not sys.stdin.isatty():
            file = fileinput.input()

        # Check for file input flag
        if argsData.file != None:
            fileName = argsData.file
            file = open(fileName)

        # Check if either stdin or -f has been passed in
        if file != None:
            data = collectRawDisk(data,file)
            file.close()
            printRawDisk(data)

        # Checks for directory file
        if argsData.directory:
            crawlRawDisk(data)

        # Check if neither stdin or file flag were passed in
        # if :
        #     raise(Exception)

    except:
        # Check if file does not exist
        if (fileName != None) and not(verifyFile(fileName)):
            print("Error: The disk is broken or does not exist, please provide a correct drive file.")
        # Check if dir flag was set and no other args
        elif argsData.directory and fileName == None and file == None:
            print("Error: -dir is useless without a specified disk file")
        else:
            pass
        # Catch all other errors
        # else:
        #     print(Exception + "Error: you broke the thing... good job")

# Methods
def parseInput():
    
    # Create parser
    parser = argparse.ArgumentParser(add_help=False,description='Takes a disk and prints its contents.')
    
    # Add args
    parser.add_argument('-v', '--version', action="version",version="shell.py version --> " + version,help="Display current program version")
    parser.add_argument('-d','-dir','--directory',action="store_true",help="List file contents of the input drive")
    parser.add_argument('-h','-H', '--help','-?', action='help', default=argparse.SUPPRESS,help='Show this help message and exit.')
    parser.add_argument('-f','--file', type=str, help="Specify a formatted drive file")
    
    # Check if no args were passed
    if len(sys.argv)==1 and sys.stdin.isatty():
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    #Return parser with args
    return args


parsed = parseInput()
evalArgs(parsed)