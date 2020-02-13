# to execute run
# python shell.py <arguments>
import sys
import os
import subprocess
import fileinput

args = sys.argv

for i in range(0,args.__len__()):
    if args[i] == "-v" or args[i] == "-V":
        sys.stdout.write("Version 1.0.0\n")
    if args[i] == "-h" or args[i] == "-H" or args[i] == "-?":
        sys.stdout.write("Version 1.0.0")


#for fileinput_line in fileinput.input():
#    if 'Exit' == fileinput_line.rstrip():
#        break
#    print(f'Processing Message from fileinput.input() *****{fileinput_line}*****')

#print("Done")

#while True:
#    data = input("Please enter the message:\n")
#    if 'Exit' == data:
#        break
#    print(f'Processing Message from input() *****{data}*****')

#print("Done")
