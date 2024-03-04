from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app.models import Session_Year, Course, CustomUser, Student


@login_required(login_url='/')
def HOME(request):
    return render(request, 'hod/home.html')


"""
@login_required: This is a decorator in Django used to restrict access to a particular view
(in this case, the HOME view) to authenticated users only. If a user is not authenticated 
(i.e., they are not logged in), they will be redirected to the login page. 
You can specify the login URL as an argument to the decorator, which is login_url='/ ' in this case."""


@login_required(login_url='/')
def add_student(request):
    course = Course.objects.all()
    # print(course)
    sessionyesr = Session_Year.objects.all()
    # print(sessionyesr)

    if request.method == "POST":
        p_pic = request.FILES.get('profilepic')  # for getting images we use file feild
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        eml = request.POST.get('email')
        uname = request.POST.get('username')
        ps_word = request.POST.get('password')
        adrs = request.POST.get('Address')
        gend = request.POST.get('gender')
        crs = request.POST.get('course_id')  # in o/p getting value from template value value attribute that is id
        sesion_yr = request.POST.get('session_year_id')

        print(p_pic, fname, lname, eml, uname, ps_word, adrs, gend, crs, sesion_yr)

        if CustomUser.objects.filter(email=eml).exists():
            messages.warning(request, "email already exist")
            return redirect('add_student')
        if CustomUser.objects.filter(username=uname).exists():
            messages.warning(request, "username already exist")
            return redirect("add_student")
        else:
            user = CustomUser(
                # user_profile=p_pic,
                first_name=fname,
                last_name=lname,
                email=eml,
                username=uname,
                user_type=3,
            )
            user.set_password(ps_word)
            user.save()

            corse = Course.objects.get(id=crs)
            session_year = Session_Year.objects.get(id=sesion_yr)

            student = Student(
                admin=user,
                address=adrs,
                gender=gend,
                course=corse,
                session_year_id=session_year,

            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + "student save successfully")
            return redirect('add_student')

    context = {
        "course": course,
        'sessionyesr': sessionyesr,
    }

    return render(request, 'hod/add_student.html', context)


def view_student(request):
    stud = Student.objects.all()
    print(stud)
    context = {
        "stud1": stud,
    }
    return render(request, 'hod/view_student.html', context)


def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    print(student)
    context = {
        'stud': student,
        'crs': course,
        'session': session_year
    }
    return render(request, 'hod/edit_student.html', context)


def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        print(student_id)

        p_pic1 = request.FILES.get('profilepic')  # for getting images we use file feild
        fname1 = request.POST.get('firstname')
        lname1 = request.POST.get('lastname')
        eml1 = request.POST.get('email')
        uname1 = request.POST.get('username')
        print(uname1)
        ps_word1 = request.POST.get('password')
        adrs1 = request.POST.get('Address')
        print(adrs1)
        gend1 = request.POST.get('gender')
        print(gend1)
        crs1 = request.POST.get('course_id')  # in o/p getting value from template value value attribute that is id
        sesion_yr1 = request.POST.get('session_year_id')

        print(p_pic1, fname1, lname1, eml1, uname1, ps_word1, adrs1, gend1, crs1, sesion_yr1)

        user = CustomUser.objects.get(id=student_id)

        user.first_name = fname1
        user.last_name = lname1
        user.email = eml1
        user.username = uname1

        if ps_word1 != None and ps_word1 != ' ':
            user.set_password(ps_word1)

        if p_pic1 != None and p_pic1 != ' ':
            user.user_profile = p_pic1

            user.save()

        student = Student.objects.get(admin=student_id)
        student.address = adrs1
        student.gender = gend1

        courese = Course.objects.get(id=crs1)
        student.course = courese

        sessionyesr = Session_Year.objects.get(id=sesion_yr1)
        student.session_year_id = sessionyesr

        student.save()

        messages.success(request, "records are successfully updated")
        return redirect('view_student')

    return render(request, 'hod/edit_student.html')


def DELETE_Student(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, "data deleted successfully ")
    return redirect('view_student')


def add_course(request):
    if request.method == 'POST':
        cors_name = request.POST.get('course_name')
        print(cors_name)

        corss = Course(
            name=cors_name
        )
        corss.save()
        messages.success(request, 'Course added Successfully')

    return render(request, 'hod/add_course.html')


def view_course(request):
    crs = Course.objects.all()
    print(crs)
    context = {
        'course': crs
    }
    return render(request, 'hod/view_course.html', context)


def EDIT_COURSE(request, id):
    corse_name = Course.objects.filter(id=id)
    print("corse_name", corse_name)

    context = {
        'corse_name': corse_name
    }

    return render(request, 'hod/edit_course.html', context)


def UPDATE_COURSE(request):
    if request.method == "POST":
        crs_name = request.POST.get("course_name")
        crs_id = request.POST.get("course_id")
        print(crs_name, crs_id)

        cours = Course.objects.get(id=crs_id)
        cours.name = crs_name

        cours.save()

        messages.success(request, "Course updated successffuly")
        return redirect('view_course')

    return render(request, 'hod/edit_course.html')


def COURSE_delete(request, id):
    corse = Course.objects.get(id=id)
    corse.delete()
    messages.success(request, "Course deleted successfully")

    return redirect('view_course')


def ADD_STAFF(request):
    if request.method=='POST':
        profile_pic=request.FILES.get('profilepic')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        username=request.POST.get('username')
        






    return render(request,'hod/add_staff.html')