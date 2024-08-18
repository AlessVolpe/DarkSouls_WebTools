# Dark Souls Souls Calculator
[![Django CI](https://github.com/AlessVolpe/DarkSouls_WebTools/actions/workflows/django.yml/badge.svg)](https://github.com/AlessVolpe/DarkSouls_WebTools/actions/workflows/django.yml)

This is a Django web application that calculates the number of souls required to level up in the Dark Souls game. The application features a single-page form where users can input their current and desired levels, and it calculates the required souls dynamically.

## Features

- **Dynamic Calculation**: Enter your current and desired levels to see the number of souls needed.
- **AJAX Form Submission**: The form submits data asynchronously, and the result is displayed without refreshing the page.
- **Bootstrap with Material Design**: The app uses Bootstrap for styling, adhering to Material Design principles, with a dark mode theme.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- Pipenv or virtualenv for managing virtual environments
- Heroku CLI (if deploying to Heroku)

### Clone the Repository

```bash
# Clone Repository
git clone https://github.com/AlessVolpe/dark-souls-calculator.git
cd dark-souls-calculator

# Setup pipenv
pipenv install
pipenv shell

# or setup vrtualenv
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py migrate
```
Access the application at http://127.0.0.1:8000/calculator/.

## Usage

    Navigate to the app: Open http://127.0.0.1:8000/calculator/ in your browser.
    Input levels: Enter your current and desired levels.
    View results: The required souls will be displayed dynamically under the form.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests.

## Acknowledgements

    Dark Souls is a trademark of FromSoftware, Inc.
    Bootstrap and Material Design by Bootstrap.


This `README.md` provides a comprehensive overview of the project, instructions for setup, deployment steps, and additional information about usage and licensing. Customize the `git clone` URL and other placeholders to match your project details before using it.
