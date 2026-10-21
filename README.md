# OnlineCourse Django Final Project

This project implements the Coursera final assessment feature for an online course:

- `onlinecourse/models.py` defines `Question`, `Choice`, and `Submission`.
- `onlinecourse/admin.py` registers the course, lesson, question, choice, and submission administration experience.
- `onlinecourse/templates/onlinecourse/course_details_bootstrap.html` displays the course and related lessons with Bootstrap.
- `onlinecourse/views.py` implements `submit` and `show_exam_result`.
- `onlinecourse/urls.py` routes the exam submission and result pages.

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Demo admin credentials: `admin` / `AdminPass123!`

Screenshots for the assignment are in `screenshots/03-admin-site.png` and `screenshots/07-final.png`.
