# Entrata Code Challenge
This is a repository for Entrata automation which include UI tests
This repository is following Page Object Model
Setup and Run Tests Locally
Pre-requisites:
Before setting up and running the tests locally, ensure you have the following:

Python installed: Python 3.9 should be installed on your machine. You can check the Python version by running the 
command python --version in the terminal. Or download Python latest version.

Code editor: VS Code is the recommended code editor for the automation project.

Browsers: Chrome browser should be installed on your machine to execute the tests. 

Installation Steps:
Git Checkout: Clone the automation repository by running the following command in the terminal:

git clone link of repo

Create a Virtual Environment: Navigate to the 'Entrata' directory and Create a virtual environment named "venv" using the following command:

py -m venv venv

Activate the Virtual Environment: Activate the virtual environment by executing the following command:

.\venv\Scripts\activate

Required Modules Installation: Navigate to the 'Entrata' directory and install the required modules from the 'requirement.txt' file:

cd Entrata

pip install -r requirement.txt

This step will automatically install pytest and other necessary packages specified in 'requirements.txt'.

Execute Test:
To execute the tests, follow these steps:

Open a terminal.

Navigate to the project root directory ('Entrata').

Run the following command with the appropriate options:

pytest

To run a single test:

pytest -k 'test_name'

Example: pytest -k test_navigate_to_pages


