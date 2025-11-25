## Installation Check

- Ran `python manage.py runserver` → Django server started successfully.
- Initially saw 18 unapplied migrations (admin, auth, contenttypes, sessions).
- Fixed by running:
  ```bash
  python manage.py migrate
