from django.db import models
from django.contrib.auth.models import User,AbstractUser

User._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('email').null = False


STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('J&K','J&K'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh	','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)

class College(models.Model):
    collegename = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=255)
    website = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.collegename)

class Branch(models.Model):
    branchname = models.CharField(max_length=255)

    def __str__(self):
        return str(self.branchname)

class CollegeBranch(models.Model):
    collegename = models.ForeignKey(College, on_delete=models.CASCADE)
    branchname = models.ForeignKey(Branch, on_delete=models.CASCADE)
    hodname = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Course(models.Model):
    coursename = models.CharField(max_length=255)
    collegebranch = models.ForeignKey(CollegeBranch, on_delete=models.CASCADE)
    no_semester = models.PositiveIntegerField(default=6)
    def __str__(self):
        return str(self.id)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    collegename = models.ForeignKey(College, on_delete=models.CASCADE,blank=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    currentsem = models.PositiveIntegerField(default=1)
    mobileno = models.CharField(max_length=20)
    rollno = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='student_photos',null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(choices=STATE_CHOICES,max_length=255)
    pincode = models.IntegerField(null=True)
    skills = models.TextField(null=True)
    tips = models.TextField(null=True)
    def __str__(self):
        return str(self.id)

class Subject(models.Model):
    subjectcode = models.CharField(max_length=255)
    subjectname = models.CharField(max_length=255,blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructorname = models.CharField(max_length=255)
    semester = models.PositiveIntegerField(default=1)
    compulsory = models.BooleanField(null=True,default=True)
    def __str__(self):
        return str(self.id)

class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semesterno = models.PositiveIntegerField()
    academiccalendar = models.FileField(upload_to='academiccalendar',null=True)

    def __str__(self):
        return str(self.id)

class Notification(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return str(self.id)

class Material(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    filefield = models.FileField(upload_to='material')

    def __str__(self):
        return str(self.id)
