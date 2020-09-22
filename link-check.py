import argparse
import sys

parser = argparse.ArgumentParser(description="link-check is a broken link identifier")
parser.add_argument('-v',"--version", action='store_true', help="returns version of tool")
parser.add_argument('-f','--file',help="parses file", metavar='\b')

args=parser.parse_args()

version=0.1