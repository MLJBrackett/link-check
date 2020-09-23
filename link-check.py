import requests
import re
import argparse
import sys
from colorama import init, Fore, Back, Style

init(convert=True)

parser = argparse.ArgumentParser(description="link-check is a broken link identifier")
parser.add_argument('-v',"--version", action='store_true', help="returns version of tool")
parser.add_argument('-f','--file',help="parses file", metavar='\b')

args=parser.parse_args()

version=0.1
properUrls=[]

if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)


def urlparse():
    with open(args.file) as file:
        for line in file:
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
            if len(urls) != 0:
                properUrls.append(urls)
    urlcheck()

def urlcheck():
    for url in properUrls:
        if len(url) > 1:
            for currentUrl in url:
                try:
                    r = requests.head(currentUrl,timeout=2.5,allow_redirects=True)
                    if r.status_code==200:
                        print(Fore.GREEN+currentUrl,r.status_code,' GOOD')
                    elif r.status_code==404:
                        print(Fore.RED+currentUrl,r.status_code,' DEAD')
                    else:
                        print(Fore.YELLOW+currentUrl,r.status_code,' OKAY')
                except requests.exceptions.RequestException:
                    print(Fore.RED+currentUrl,"TIMEOUT")
        else:
            try:
                r = requests.head(url[0],timeout=2.5,allow_redirects=True)
                
                if r.status_code==200:
                    print(Fore.GREEN+url[0],r.status_code,' GOOD')
                elif r.status_code==404:
                    print(Fore.RED+url[0],r.status_code,' DEAD')
                else:
                    print(Fore.YELLOW+url[0],r.status_code,' OKAY')
            except requests.exceptions.RequestException:
                print(Fore.RED+url[0],"TIMEOUT")
    print(Style.RESET_ALL)


if args.version:
    print(version)
if args.file:
    urlparse()