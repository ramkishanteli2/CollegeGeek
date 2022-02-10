from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','collegename','currentsem']
    
admin.site.register(Student,StudentAdmin)

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id','collegename','state','website']

admin.site.register(College,CollegeAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['id','branchname']

admin.site.register(Branch,BranchAdmin)

class CollegeBranchAdmin(admin.ModelAdmin):
    list_display = ['id','collegename','branchname','hodname']

admin.site.register(CollegeBranch,CollegeBranchAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','coursename','collegebranch','no_semester',]

admin.site.register(Course,CourseAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id','subjectcode','subjectname','course','instructorname','semester','compulsory']

admin.site.register(Subject,SubjectAdmin)

class SemesterAdmin(admin.ModelAdmin):
    list_display = ['id','course','semesterno']

admin.site.register(Semester,SemesterAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id','semester','message','datetime']

admin.site.register(Notification,NotificationAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['id','subject','title','filefield']

admin.site.register(Material,MaterialAdmin)