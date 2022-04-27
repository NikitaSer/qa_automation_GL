Command to run tests:

> pytest .

In order to debug or to see any standard output use -s flag is equivalent to --capture=no:

> pytest -s .



Info about test framework:

Structure of test framework:
1. Tests should be in the 'tests' folder
2. All the configurations should be defined in the config/config class firstly