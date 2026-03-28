# Playwright BDD with Behave

This project demonstrates using Playwright for browser automation with Python and the Behave BDD framework.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:
   ```
   playwright install
   ```

## Running Tests

Run the BDD tests with:
```
python run_tests.py
```

Or directly with behave:
```
behave
```

Or for a specific feature:
```
behave features/google_search.feature
```

## Project Structure

- `features/` - BDD feature files
- `features/steps/` - Step definitions
- `features/environment.py` - Behave hooks and fixtures
- `requirements.txt` - Python dependencies 
