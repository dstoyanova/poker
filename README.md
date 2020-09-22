# Planning Poker

## Prerequisites

You need to have Python and Django installed.

To install Python (assuming you have set up Homebrew on your Mac):
```bash
brew install python
```

To install Django:
```bash
python -m pip install Django
```

## Run the application

From the application's directory, run the following:
```bash
python manage.py runserver
````

Planning Poker is now deployed and can be accessed here http://127.0.0.1:8000/polls/

If the port is currently occupied by another proces, change the port by passing it to the command line:
```bash
python manage.py runserver 8080
````

This will start the server on port 8080 instead.
