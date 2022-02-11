from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from PIL import Image
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
STATE_CHOICES = (
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Delhi',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'J&K',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal',
)


def index(request):
    return render(request, 'college/index.html')


def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get(
            'email'), password=request.POST.get('password'))
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Email or Password is Incorrect")
            return render(request, 'college/login.html')
    else:
        return render(request, 'college/login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'college/register.html')
        else:
            user = User.objects.create_user(request.POST.get(
                'username'), request.POST.get('email'), request.POST.get('password1'))
            user.first_name = request.POST.get('name')
            user.save()
            return redirect(reverse('create_student', kwargs={'email_': str(user.email), 'college': request.POST.get('college'), 'course': request.POST.get('course'), 'name': request.POST.get('name')}))
    else:
        colleges = College.objects.all()
        return render(request, 'college/register.html', {'colleges': colleges})


def create_student(request, email_, college, course, name):
    stu = Student()
    user = User.objects.get(email=email_)
    stu.user = user
    stu.name = name
    stu.collegename = College.objects.get(id=int(college))
    stu.course = Course.objects.get(id=int(course))
    stu.save()
    # send_mail(
    #     'Account created successfully!',
    #     f'Welcome to CollegeGeek {user.first_name}!. \n Your account has been created successfully. \n Email: {user.email} \n Happy Learning! \n Regards CollegeGeek Developer Team',
    #     settings.EMAIL_HOST_USER,
    #     [str(user.email)],
    #     fail_silently=False,
    # )
    return redirect('login')


@csrf_exempt
def get_branches(request):
    if request.method == "POST":
        college = College.objects.get(id=request.POST.get('college_id'))
        branches = CollegeBranch.objects.filter(collegename=college).values()
        branches = list(branches)
        for branch in branches:
            branch['branchname'] = Branch.objects.get(
                id=branch['branchname_id']).branchname
        return JsonResponse({'status': 'success', 'branches': branches})
    else:
        return JsonResponse({'status': 0})


@csrf_exempt
def get_courses(request):
    if request.method == "POST":
        branch = CollegeBranch.objects.get(id=request.POST.get('branch_id'))
        courses = Course.objects.filter(collegebranch=branch).values()
        courses = list(courses)
        return JsonResponse({'status': 'success', 'courses': courses})
    else:
        return JsonResponse({'status': 0})


def forgot_password(request):
    return render(request, 'college/resetpassword.html')


def changepassworddone(request):
    return render(request, 'college/changepassworddone.html')


def profile(request):
    if request.user.is_authenticated:
        stud = Student.objects.get(user=request.user)
        return render(request, 'college/profile.html', {'stud': stud})
    else:
        return redirect('login')


def edit_profile(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            stud = Student.objects.get(user=request.user)
            stud.name = request.POST.get('name')
            stud.mobileno = request.POST.get('mobile')
            stud.rollno = request.POST.get('rollno')
            stud.currentsem = request.POST.get('currentsem')
            stud.address = request.POST.get('address')
            stud.city = request.POST.get('city')
            stud.state = request.POST.get('state')
            stud.pincode = request.POST.get('pincode')
            stud.profile_image = request.FILES.get('profilepic')
            stud.skills = request.POST.get('skills')
            stud.tips = request.POST.get('tips')
            stud.save()
            request.user.first_name = request.POST.get('name')
            request.user.save()
            return redirect('profile')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return render(request, 'college/editprofile.html', {'states': STATE_CHOICES, 'stud': Student.objects.get(user=request.user)})
        else:
            return render(request, 'college/editprofile.html', {'states': STATE_CHOICES, })


def academic(request):
    if request.user.is_authenticated:
        color = ['primary', 'secondary', 'success', 'danger',
                 'warning', 'info', 'light', 'transparent']
        course = Student.objects.get(user=request.user).course
        sem = course.no_semester
        course_name = course.coursename
        branch_name = CollegeBranch.objects.get(
            id=course.collegebranch.id).branchname.branchname
        semesters = []
        i = 0
        while i < sem:
            j = i
            lst = []
            while(j < i+3 and j < len(color)):
                lst.append({'color': color[j], 'sem_no': j+1})
                j += 1
            i = j
            semesters.append(lst)
        return render(request, 'college/academic.html', {"semesters": semesters, 'course_name': course_name, 'branch_name': branch_name})
    else:
        return redirect('login')


def subjects(request, sem_no=None):
    if request.user.is_authenticated:
        subjects = Subject.objects.filter(
            Q(course=Student.objects.get(user=request.user).course) & Q(semester=sem_no))
        return render(request, 'college/subjects.html', {'subjects': subjects, 'semester': sem_no})
    else:
        return redirect('login')


def classtimetable(request, sem_no=None):
    if request.user.is_authenticated:
        # subjects = Subject.objects.filter(course=Student.objects.get(user=request.user).course)
        return render(request, 'college/classtimetable.html', {'semester': sem_no})
    else:
        return redirect('login')


def academiccalendar(request, sem_no=None):
    if request.user.is_authenticated:
        try:
            semcal = Semester.objects.get(Q(course=Student.objects.get(
                user=request.user).course) & Q(semesterno=sem_no))
        except Semester.DoesNotExist:
            semcal = None
        return render(request, 'college/academiccalendar.html', {'semester': sem_no, 'semcal': semcal})
    else:
        return redirect('login')


def notifications(request):
    if request.user.is_authenticated:
        try:
            notifications = Notification.objects.filter(semester=Semester.objects.get(Q(course=Student.objects.get(
                user=request.user).course), Q(semesterno=Student.objects.get(user=request.user).currentsem)))
        except Semester.DoesNotExist:
            notifications = None
        return render(request, 'college/notifications.html', {'notifications': notifications})
    else:
        return redirect('login')


def material(request, id=None):
    if request.user.is_authenticated:
        sub = Subject.objects.get(id=id)
        materials = Material.objects.filter(subject=sub)
        return render(request, 'college/material.html', {'id': id, 'materials': materials, 'subjectname': sub.subjectname, 'semester': Subject.objects.get(id=id).semester})
    else:
        return redirect('login')


def batchmates(request):
    if request.user.is_authenticated:
        batchmates = Student.objects.filter(Q(course=Student.objects.get(user=request.user).course) & Q(
            currentsem=Student.objects.get(user=request.user).currentsem))
        return render(request, 'college/batchmates.html', {'batchmates': batchmates})
    else:
        return redirect('login')


def seniors(request):
    if request.user.is_authenticated:
        seniors = Student.objects.filter(Q(course=Student.objects.get(user=request.user).course) & Q(
            currentsem=Student.objects.get(user=request.user).currentsem+1))
        return render(request, 'college/seniors.html', {'seniors': seniors})
    else:
        return redirect('login')
