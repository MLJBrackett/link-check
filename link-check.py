import requests
import re
import argparse
import sys
from colorama import init, Fore, Back, Style

init() # Colour support for Windows operating systems

parser = argparse.ArgumentParser(description="link-check is a broken link identifier")
parser.add_argument('-v',"--version", action='store_true', help="Returns the current version of tool")
parser.add_argument('-f','--file',help="Checks the given file in the current directory for urls (-f htmls.txt)", metavar='\b')
parser.add_argument('-r','--redirect',help="Checks the given file in the current directory for urls and allows for redirecting of urls (-r htmls.txt)", metavar="\b")

args = parser.parse_args()

version = 0.1
foundUrls = []

# If no arguements print help
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

# Parses the URL from the given file
def urlParse():
    if args.file:
        argFile=args.file
    elif args.redirect:
        argFile=args.redirect
    with open(argFile) or open(argFile) as file:
        for line in file:
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            if len(urls) != 0:
                foundUrls.append(urls)
        urlCheck()

# Returns the status code of the given URLs
def urlCheck():
    for url in foundUrls:
            try:
                if args.file:
                    r = requests.head(url[0],timeout=1.5)
                elif args.redirect:
                    r = requests.head(url[0],timeout=1.5,allow_redirects=True)
                if r.status_code in range(200,299):
                    print(Fore.GREEN + url[0],r.status_code,' GOOD')
                elif r.status_code in range(400,599):
                    print(Fore.RED + url[0],r.status_code,' CLIENT/SERVER ISSUE')
                elif r.status_code in range(300,399):
                    print(Fore.YELLOW + url[0],r.status_code,' REDIRECT')
                else:
                    print(Fore.WHITE + url[0],r.status_code,' UNKNOWN')
            except requests.exceptions.RequestException:
                print(Fore.RED + url[0],"TIMEOUT")
    print(Style.RESET_ALL)

if args.version:
    print(version)
elif args.file or args.redirect:
    urlParse()