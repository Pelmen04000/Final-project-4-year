# LMS Ready Project (fixed)

This project is prepared to run locally. It includes:
- Correct migrations using `django.utils.timezone`
- AUTH_USER_MODEL configured
- Management command `python manage.py seed` to create admin/admin123 and demo data
- Static directory present to avoid STATICFILES warning

How to run:
1. python -m venv venv
2. source venv/bin/activate  # or venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py seed
6. python manage.py runserver

If you see warnings about STATICFILES_DIRS, ensure `static/` exists (it does by default in this project).
