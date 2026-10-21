from django.shortcuts import get_object_or_404, redirect, render
from .models import Lesson, Submission


def home(request):
    lesson = Lesson.objects.select_related("course").first()
    return redirect("course-details", lesson.course_id) if lesson else render(request, "onlinecourse/home.html")


def course_details(request, course_id):
    from .models import Course
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


def exam(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, "onlinecourse/exam.html", {"lesson": lesson})


def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    questions = list(lesson.questions.prefetch_related("choices"))
    score = sum(
        1 for question in questions
        if request.POST.get(f"question_{question.id}") == str(question.choices.get(is_correct=True).id)
    )
    student_name = request.POST.get("student_name", "Guest").strip() or "Guest"
    submission = Submission.objects.create(
        student_name=student_name, lesson=lesson, score=score, total_questions=len(questions)
    )
    return redirect("show_exam_result", submission_id=submission.id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission.objects.select_related("lesson__course"), pk=submission_id)
    return render(request, "onlinecourse/exam_result.html", {"submission": submission})
