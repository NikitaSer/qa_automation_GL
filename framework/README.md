In order to run API tests use the following command:
> pytest tests/test_api_client.py

\
In order to run UI tests you need to specify browser parameter. For example, the test from tests/test_ui.py will run for Chrome browser:

> pytest --browser=chrome tests/test_ui.py

\
In order to see detailed pytest output use -v (verbose) flag:
> pytest -v .

\
Info about test framework:
Framework for testing API of the web app app.cosmosid.com 

Structure of test framework:
1. Tests should be in the 'tests' folder
2. All the configurations should be defined in the config/config class firstly
3. Fixtures should be defined in the 'conftest.py'

Code formatter using in framework is 'Black'
