# weather-platform
A Django based yahoo weather API wrapper

## REQUIREMENTS ##
THe project requirements are listed in the `requirements.txt` file.

## DEVELOPMENT ##
To set-up project for local development, run the project in a virtualenv.

```
# Change into project directory
cd <project_name>

# Make virtual environment
mkvirtualenv <project_name>

# Activate virtual environment
workon <project_name>

# Install requirements
pip install -r requirements.txt

# Start the development server
python manage.py runserver 10000
```

Test endpoint, `http://localhost:10000/weather/pretoria/7` for Pretoria weather over a period of 7 hours.

## DEPLOYMENT ##
Deploy the service behind a gunicorn server following this post https://medium.com/analytics-vidhya/dajngo-with-nginx-gunicorn-aaf8431dc9e0

