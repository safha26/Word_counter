This Django project builds a Word Counter web tool that counts words, letters with spaces, and without spaces from user-submitted text via a Bootstrap-styled form. Named "count" with app "app1", it uses forms for input validation and renders results dynamically.

**Set up instructions:**

1. Clone: `git clone <repo>`
2. Virtualenv: `python -m venv .venv, (Windows: `.venv\scripts\Activate.ps1`)
3. Install: `pip install django`
4. Migrate: `python manage.py migrate`
5. Run: `python manage.py runserver`
6. Visit: http://127.0.0.1:8000/

## Features
- Text input form
- Word count (split())
- Char counts (len with/without spaces)
- Responsive Bootstrap UI

## Models, Form and views:
FORM: Handles user input validation.
  CSRF protection automatic ({% csrf_token %}), prevents invalid/malicious input. Fresher-friendly intro to form handling without ModelForms.

**Views:**
  countpage: Receives input. If POST is requested and form is valid them it counts the length of the tect using len(). 
  for counting words: len(text.split())
  count_with space: len(text)
  count_without space: len(text.replace(' ',''))
  then the values are returned. 
