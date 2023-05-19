from django.db import models


class ReadingMaterial(models.Model):
    week = models.ForeignKey('WeeklyModules', on_delete=models.CASCADE, null=True, blank=True)
    contentId = models.IntegerField()
    sectionId = models.IntegerField()
    contentTopic = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.contentTopic}"

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_level= models.CharField(max_length=10)               #beginner,medium,hard
    short_description=models.CharField(max_length=100)          #to show in course list

    def __str__(self):
        return f"{self.course_name}"

class WeeklyModules(models.Model):
    course=models.ForeignKey('Course',on_delete=models.CASCADE, null=True, blank=True)
    contents = models.CharField(max_length=100,null=True, blank=True)

class Mcq(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    section= models.ForeignKey('ReadingMaterial', on_delete=models.CASCADE, null=True, blank=True)
    question = models.CharField(max_length = 100)
    right_option = models.CharField(max_length = 20)
    wrong_option1 = models.CharField(max_length = 20)
    wrong_option2 = models.CharField(max_length = 20)
    wrong_option3 = models.CharField(max_length = 20)

class Student(models.Model):
    name = models.CharField(max_length= 50)
    school = models.CharField(max_length=50)
    _class = models.IntegerField()

class ProgrammingProblem(models.Model):
    rdmat = models.ForeignKey('ReadingMaterial', on_delete=models.DO_NOTHING,null=True, blank=True)
    problem = models.CharField(max_length=1000, null=True, blank=True)
    sample_input = models.CharField(max_length=100, null=True, blank=True)
    sample_output = models.CharField(max_length=100,  null=True, blank=True)

class StudentCourseHistory(models.Model):
    Student = models.ForeignKey('Student', on_delete=models.DO_NOTHING,null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING,null=True, blank=True)
    week = models.ForeignKey('WeeklyModules', on_delete=models.DO_NOTHING,null=True, blank=True)
    reading_done = models.BooleanField(default=False)
    mcq_done = models.BooleanField(default=False)
    prog_done = models.BooleanField(default=False)

