# eyos-assessment
#Assignment 2
# Development Setup



<h3>Prerequisites</h3>

- Python
- 

Create and open a virtual environment.
- python -m venv env
- source env/bin/activate

**Run following commands from project root directory to get up and running.**

**Install Packages**

pip install -r requirements.txt

**Run Test**

pytest <filename.py>

**Allure for Reports**

Run your tests using pytest with the --alluredir option to specify the directory where the allure reports will be generated:

pytest --alluredir=./allure_reports

Generate the allure report using the `allure`

allure serve ./allure_reports
 
