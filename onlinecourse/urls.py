from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("course/<int:course_id>/", views.course_details, name="course-details"),
    path("exam/<int:lesson_id>/", views.exam, name="exam"),
    path("exam/<int:lesson_id>/submit/", views.submit, name="submit"),
    path("exam/result/<int:submission_id>/", views.show_exam_result, name="show_exam_result"),
]
