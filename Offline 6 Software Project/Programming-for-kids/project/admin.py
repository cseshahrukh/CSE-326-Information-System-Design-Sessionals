from django.contrib import admin
from .models import ReadingMaterial, Course, Mcq, WeeklyModules, Student, ProgrammingProblem


# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    list_display = ("week", "contentId", "sectionId", "contentTopic")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("id","course_name", "course_level", "short_description")

class McqAdmin(admin.ModelAdmin):
    list_display = ("course", "question", "right_option", "wrong_option1", "wrong_option2", "wrong_option3")

class StudentAdmin(admin.ModelAdmin):
    list_display=("name", "school", "_class")

class WeeklyModulesAdmin(admin.ModelAdmin):
    list_display=("course","contents")

class ProgrammingProblemAdmin(admin.ModelAdmin):
    list_display=("rdmat", "problem", "sample_input", "sample_output")

admin.site.register(ReadingMaterial, MaterialAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Mcq, McqAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(WeeklyModules, WeeklyModulesAdmin)
admin.site.register(ProgrammingProblem, ProgrammingProblemAdmin)


