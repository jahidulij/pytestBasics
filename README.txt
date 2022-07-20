# Pre Requisite:
    - python                [Language]
    - selenium              [Automate Browsers]
    - webdriver-manager     [Get Browser Drivers]
    - pytest                [Framework]
    - pytest-html           [HTML Report Generation]
    - pytest-xdist          [To Run Parallel Execution]

# Test function names should start with test_ [test_login_01.py]

# Run pytest from terminal:
    - Go to the directory
    - Command:
            pytest
            pytest -v [This will print the short test summary info]
            pytest filename -v [To run a particular file]
            pytest -k <substring> -v  [Substring Matching of Test Names]

# Markers:
    Grouping the Tests:
            @pytest.mark.<markername>   [To use mark you have to import pytest]
            Run:  pytest -m <markername> -v

# Fixtures:
    @pytest.fixture         [To use mark you have to import pytest]
    * Instead of running the same code for every test, we can attach fixture function to the
      tests and it will run and return the data to the test before executing each test.
    * A test function can use a fixture by mentioning the fixture name as an input parameter.

# Pytest - conftest.py:
    * This fixture function is accessible across multiple test files.
    * The tests will look for fixture in the same file. As the fixture is not found in the file, it will check for fixture in conftest.py file.

# Pytest - Parameterizing Tests:
    * Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −
        @pytest.mark.parametrize("val1, val2",
                                [
                                 (val1_value, val2_value),
                                 (val1_value, val2_value),
                                 (val1_value, val2_value),
                                 ...
                                ])
        ** val1 & val2 must be used as a parameter of the function where you want to use this.

# Pytest - Xfail/Skip Tests:
    * Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests.
        @pytest.mark.xfail
    * Skipping a test means that the test will not be executed.
        @pytest.mark.skip

# Pytest - Stop Test Suite after N Test Failures
    * If we want to stop the execution of test suite soon after n number of test fails. This can be done in pytest using maxfail.
        pytest --maxfail = <num>

# Pytest - Run Tests in Parallel
    - pip install pytest-xdist      [To run parallel tests we need this package/ library]
    - Command: pytest -n <num>

# Test Execution Results in XML Format
    - Generate the details of the test execution in a xml file.
    - Command: pytest filename --junitxml="result.xml"
