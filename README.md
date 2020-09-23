# Link Check

Link Check is a Python program for finding good/dead links in any file type.

![Link Check](https://i.imgur.com/NQogvnF.gif)

## Getting Started

To locally install link-check follow these steps

### Prerequisites
* [Python/Python 3] (https://www.python.org/)
* [Git] (https://git-scm.com/)

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

Use the -h/--help flags to see arguements
```bash
python link-check -h
```
Check URLs **without** redirect support
```bash
python link-check -f links.txt
```
Check URLs **with** redirect support

```bash
python link-check -r links.txt
```
## Contributing
Contributions are welcomed, if you think you have a good idea or see an improvement that you can make, create an issue or submit a pull request.

## License
Distributed under the [MIT](https://choosealicense.com/licenses/mit/) License. See LICENSE for more information.
