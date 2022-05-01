Command to run tests:

> pytest .

In order to debug or to see any standard output use -s flag is equivalent to --capture=no:

> pytest -s .

In order to see detailed pytest output use -v (verbose) flag:
> pytest -v

\
Info about test framework:
Framework for testing API of the web app app.cosmosid.com 

Structure of test framework:
1. Tests should be in the 'tests' folder
2. All the configurations should be defined in the config/config class firstly
3. Fixtures should be defined in the 'conftest.py'

Code formatter using in framework is 'Black'