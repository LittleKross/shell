# Imports
import sys
import os
import fileinput
import argparse
import fileinput

# Global variables
version = "1.1.1"

# Methods
def parseInput():
    parser = argparse.ArgumentParser(add_help=False,description='Takes a disk and prints its contents.')
    parser.add_argument('-v', '--version', action="version",version="shell.py version --> " + version,help="Display current program version")
    parser.add_argument('-d','-dir','--directory',action="store_true",help="List file contents of the input drive")
    parser.add_argument('-h','-H', '--help','-?', action='help', default=argparse.SUPPRESS,help='Show this help message and exit.')
    parser.add_argument('-f','--file', type=str, help="Specify a formatted drive file")
    if len(sys.argv)==1 and sys.stdin.isatty():
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    return args

def evalInfo(argsData):
    try:
        data = []
        if not sys.stdin.isatty():
            file = fileinput.input()
        if argsData.file != None:
            fileName = argsData.file
            file = open(fileName)
        if file != None:
            collectRawDisk(data,file)
            file.close()
            printRawDisk(data)
        if argsData.directory:
            print('')
    except:
        print("Error: The disk is broken or does not exist, please provide a correct drive file.")

def printFolders():
    print("")

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
# def printStdIn(stdIn):
#     for line in stdIn:
#             if stdIn.lineno() > 2:
#                 sys.stdout.write(line[3:])

# Main

parsed = parseInput()
evalInfo(parsed)
    