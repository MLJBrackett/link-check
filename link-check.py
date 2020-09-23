import requests
import re
import argparse
import sys
from colorama import init, Fore, Back, Style
init()

parser = argparse.ArgumentParser(description="link-check is a broken link identifier")
parser.add_argument('-v',"--version", action='store_true', help="Returns the current version of tool")
parser.add_argument('-f','--file',help="Checks the given file in the current directory for urls (-f htmls.txt)", metavar='\b')
parser.add_argument('-r','--redirect',help="Checks the given file in the current directory for urls and allows for redirecting of urls (-r htmls.txt)", metavar="\b")

args = parser.parse_args()

version = 0.1
foundUrls = []

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

def urlParse():
    if args.file:
        with open(args.file) as file:
            for line in file:
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                if len(urls) != 0:
                    foundUrls.append(urls)
            urlCheck()

    if args.redirect:
        with open(args.redirect) as file:
            for line in file:
                urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                if len(urls) != 0:
                    foundUrls.append(urls)
            urlCheckRedirect()
        

def urlCheck():
    for url in foundUrls:
        if len(url) > 1:
            for currentUrl in url:
                try:
                    r = requests.head(currentUrl,timeout=1.5)
                    if r.status_code in range(200,299):
                        print(Fore.GREEN + currentUrl,r.status_code,' GOOD')
                    elif r.status_code in range (400,599):
                        print(Fore.RED + currentUrl,r.status_code,' CLIENT/SERVER ISSUE')
                    else:
                        print(Fore.YELLOW + currentUrl,r.status_code,' REDIRECT')
                except requests.exceptions.RequestException:
                    print(Fore.RED + currentUrl,"TIMEOUT")
        else:
            try:
                r = requests.head(url[0],timeout=1.5)
                if r.status_code in range(200,299):
                    print(Fore.GREEN+url[0],r.status_code,' GOOD')
                elif r.status_code in range(400,599):
                    print(Fore.RED + url[0],r.status_code,' CLIENT/SERVER ISSUE')
                else:
                    print(Fore.YELLOW + url[0],r.status_code,' REDIRECT')
            except requests.exceptions.RequestException:
                print(Fore.RED + url[0],"TIMEOUT")
    print(Style.RESET_ALL)

def urlCheckRedirect():
    for url in foundUrls:
        if len(url) > 1:
            for currentUrl in url:
                try:
                    r = requests.head(currentUrl,timeout=1.5,allow_redirects=True)
                    if r.status_code in range(200,299):
                        print(Fore.GREEN + currentUrl,r.status_code,' GOOD')
                    elif r.status_code in range(400,599):
                        print(Fore.RED + currentUrl,r.status_code,' CLIENT/SERVER ISSUE')
                    else:
                        print(Fore.YELLOW + currentUrl,r.status_code,' OKAY')
                except requests.exceptions.RequestException:
                    print(Fore.RED + currentUrl,"TIMEOUT")
        else:
            try:
                r = requests.head(url[0],timeout=1.5,allow_redirects=True)
                if r.status_code in range(200,299):
                    print(Fore.GREEN + url[0],r.status_code,' GOOD')
                elif r.status_code in range(400,599):
                    print(Fore.RED + url[0],r.status_code,' CLIENT/SERVER ISSUE')
                else:
                    print(Fore.YELLOW + url[0],r.status_code,' OKAY')
            except requests.exceptions.RequestException:
                print(Fore.RED + url[0],"TIMEOUT")
    print(Style.RESET_ALL)

if args.version:
    print(version)
elif args.file:
    urlParse()
elif args.redirect:
    urlParse()