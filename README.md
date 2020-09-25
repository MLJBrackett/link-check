# Link Check

Link Check is a Python program for finding good/dead links in any file type.

![Link Check](https://i.gyazo.com/4e7e46ca83fc24950ad70194ab222b63.gif)

## Getting Started

To locally install link-check follow these steps

### Prerequisites
* [Python/Python 3](https://www.python.org/)
* [Git](https://git-scm.com/)

### Installation

1. Clone the repo
```bash
git clone https://github.com/MLJBrackett/link-check.git
```
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```bash
pip install -r requirements.txt
```

## Usage

**For the program to run with a file you must either use the -f or -r flag**

Use the -h/--help flags to see arguements
```bash
python link-check.py -h
```
![Help](https://i.gyazo.com/4f79f6498f592b5da95191d68fc1a01d.png)

Check URLs **without** redirect support
```bash
python link-check.py -f links.txt
```
![File](https://i.gyazo.com/4e7e46ca83fc24950ad70194ab222b63.gif)

Check URLs **with** redirect support (Redirection causes the program to run slower)
```bash
python link-check.py -r links.txt
```
![Redirect]( https://i.gyazo.com/a5642797c002d9bd04b3dd59d4824d5c.gif)

Check version of tool
```bash
python link-check.py -v
```
![Version](https://i.gyazo.com/23be09cff4fb01dccc2ba4178802db2c.png)

## Contributing
Contributions are welcomed, if you think you have a good idea or see an improvement that you can make, create an issue or submit a pull request.

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.
