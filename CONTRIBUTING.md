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

## Formatting

This program uses [Python Black](https://pypi.org/project/black/) as the Source Code Formatter.
To run the formatter before you create a pull request use:
```bash
bash format.sh
```

The program has Visual Studio Code integration, saving the file with automatically run the formatter on link-check.py

## Linting

This program uses [Flake8](https://flake8.pycqa.org/en/latest/index.html) as the Linter.
To run the Linter before you create a pull request use:
```bash
bash linter.sh
```

The program has Visual Studio Code integration, saving the file with automatically run the linter on link-check.py

## Contributing
Prior to creating a pull request, make sure that the formatter and linter has run properly on your code, if you are using Visual Studio code it should automatically happen after you save.
If you are using something else, you will have to run the above commands before submitting a pull request.