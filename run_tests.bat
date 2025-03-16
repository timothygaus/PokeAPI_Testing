
:: Run all tests
:run_tests
echo Activating virtual environment...
call venv\Scripts\activate

echo Running tests...
call pytest