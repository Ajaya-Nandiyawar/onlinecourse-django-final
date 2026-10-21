from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Choice, Course, Lesson, Question, Submission


class ChoiceInline(TabularInline):
    model = Choice
    extra = 2


class QuestionInline(TabularInline):
    model = Question
    extra = 1


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("text", "lesson", "order")
    list_filter = ("lesson__course",)
    inlines = [ChoiceInline]


@admin.register(Lesson)
class LessonAdmin(ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    inlines = [QuestionInline]


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("name", "instructor")


@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = ("student_name", "lesson", "score", "total_questions", "submitted_at")
    readonly_fields = ("submitted_at",)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group)
