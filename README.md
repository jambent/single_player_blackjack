# Installation
### Create virtual environment, and activate:
python -m venv venv

source venv/bin/activate

### Install required packages from requirements.txt file:
pip install -r requirements.txt


# Run the program
PYTHONPATH=$(pwd)/ python src/main.py



## Notes
Due to an incompatibility between Python 3.12 and autopep8, Python 3.11 was deliberately selected for use instead
