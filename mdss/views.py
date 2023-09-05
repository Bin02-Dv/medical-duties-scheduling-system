from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

update = False

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {
        'user_role': user_role,
        'current_user':current_user
    }
    return render(request, 'index.html', context)

# Mdeical director section
# ------------------------------------------------------------------------------
def add_medical_dr(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {
        'user_role': user_role,
        'current_user':current_user
    }
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist !!!')
                return redirect('medical-dr')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exist !!!')
                return redirect('medical-dr')
            else:
                user = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, password=password, is_superuser=True)
                user.save()

                # user_model = User.objects.get(username=username)
                # new_complete_info = Complete_info.objects.create(user=user_model, id_user=user_model.id)
                # new_complete_info.save()
                messages.info(request, 'Medical Director Added Successfully.......')
                return redirect('view-medical-dr')
    return render(request, './medical-dr-dept/medical-dr.html', context)

def view_medical_dr(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    directors = User.objects.filter(is_superuser=True)
    context = {
        'directors':directors,
        'current_user':current_user,
        'user_role':user_role
    }
    return render(request, './medical-dr-dept/medical-dr-view.html', context)

def try_update_dr(request, id):
    update = True
    directors = User.objects.get(id=id)
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']

        directors.first_name = f_name
        directors.last_name = l_name
        directors.username = username
        directors.email = email
        directors.save()
        messages.info(request, 'Medical Director Updated Successfully...')
        return redirect('view-medical-dr')
    context = {
        'directors':directors,
        'update':update,
        'current_user':current_user,
        'user_role': user_role
    }
    return render(request, './medical-dr-dept/medical-dr.html', context)


# Delete section

def request_for_delete_dr(request, id):
    director = User.objects.get(id=id)
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'director':director, 'current_user':current_user, 'user_role':user_role}
    return render(request, './medical-dr-dept/request-for-delete-dr.html', context)

def delete_dr(request, id):
    director = User.objects.get(id=id)
    director.delete()
    messages.info(request, 'Medical Director Deleted Successfully...')
    return redirect('view-medical-dr')

# ----------------------------------------------------------------------------------------------

# H.O.D section
# ----------------------------------------------------------------------------------------------


def add_hod(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {
        'user_role': user_role,
        'current_user':current_user
    }
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist !!!')
                return redirect('hod')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exist !!!')
                return redirect('hod')
            else:
                user = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, password=password)
                user.save()
                # creating a complete info model for the staff
                user_model = User.objects.get(username=username)
                new_complete_info = Complete_info.objects.create(user=user_model, id_user=user_model.id, role='H.O.D')
                new_complete_info.save()
                messages.info(request, 'H.O.D Added Successfully.......')
                return redirect('view-hod')
    return render(request, './hod-dept/hod.html', context)

def view_hod(request):
    hods = Complete_info.objects.filter(role='H.O.D')
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'hods':hods, 'current_user':current_user, 'user_role':user_role}
    return render(request, './hod-dept/hod-view.html', context)

def try_update_hod(request, id):
    staff = Complete_info.objects.get(id_user=id)
    depts = Department.objects.all()
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'staff':staff, 'depts':depts, 'current_user':current_user, 'user_role': user_role}
    return render(request, './hod-dept/complete-staff-info.html', context)

def update_hod(request, id):
    staff = Complete_info.objects.get(id_user=id)
    if request.method == 'POST':
        f_name = request.POST['f_name']
        address = request.POST['address']
        role = request.POST['role']
        dept = request.POST['dept']

        staff.full_name = f_name
        staff.complete_address = address
        staff.role = role
        staff.department = dept
        staff.save()
        messages.info(request, 'H.O.D Updated successfully..')
        return redirect('view-hod')


    

def request_for_delete_hod(request, id):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    hod = User.objects.get(id=id)
    context = {'hod':hod, 'current_user':current_user, 'user_role':user_role}
    return render(request, './hod-dept/request-for-delete-hod.html', context)

def delete_hod(request, id):
    hod = User.objects.get(id=id)
    hod.delete()
    messages.info(request, 'H.O.D Deleted Successfully...')
    return redirect('view-hod')


# ----------------------------------------------------------------------------------------------

# Department section
# ----------------------------------------------------------------------------------------------


month = datetime.datetime.now().month
day = datetime.datetime.now().day
year = datetime.datetime.now().year
date_format = f"{month}/{day}/{year}"

def add_department(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'current_user':current_user, 'user_role':user_role}
    if request.method == 'POST':
        department_name = request.POST['department-name']
        date_created = date_format
        if len(department_name) < 2:
            messages.info(request, 'Please add a reasonble name!!')
            return redirect('add-department')
        else:
            new_dept = Department.objects.create(department_name=department_name, date_created=date_created)
            new_dept.save()
            messages.info(request, 'Department Added successfully...')
            return redirect('view-department')
    return render(request, 'add-department.html', context)

def view_department(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    depts = Department.objects.all()
    context = {'depts':depts, 'current_user':current_user, 'user_role':user_role}
    return render(request, 'view-departments.html', context)


def try_update_dept(request, id):
    update = True
    dept = Department.objects.get(id=id)
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'dept':dept, 'update':update, 'current_user':current_user, 'user_role':user_role}
    return render(request, 'add-department.html', context)

def update_dept(request, id):
    dept = Department.objects.get(id=id)
    if request.method == 'POST':
        deparment_name = request.POST['department-name']
        dept.department_name = deparment_name
        dept.save()
        messages.info(request, 'Department Update Successfully...')
        return redirect('view-department')
    
def request_for_delete_dept(request, id):
    dept = Department.objects.get(id=id)
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    context = {'dept':dept, 'current_user':current_user, 'user_role':user_role}
    return render(request, 'request-for-delete-dept.html', context)

def delete_dept(request, id):
    dept = Department.objects.get(id=id)
    dept.delete()
    messages.info(request, 'Department Deleted Successfully...')
    return redirect('view-department')

# ----------------------------------------------------------------------------------------------

# staff section
# ----------------------------------------------------------------------------------------------


def add_staff(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    for dept in user_role:
        pass
    context = {'current_user':current_user, 'user_role':user_role}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if cpassword == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist !!!')
                return redirect('staff')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exist !!!')
                return redirect('staff')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # creating a complete info model for the staff
                user_model = User.objects.get(username=username)
                new_complete_info = Complete_info.objects.create(user=user_model, id_user=user_model.id, role='Staff', department=dept.department)
                new_complete_info.save()

                # create a schedule model for the staff
                user_model2 = User.objects.get(username=username)
                new_schedule = Schedule.objects.create(user=user_model2, id_user=user_model2.id,)
                new_schedule.save()
                messages.info(request, 'Staff Added Successfully.......')
                return redirect('view-staff')
    return render(request, 'staff.html', context)

def view_staff(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    staffs = Complete_info.objects.filter(role='Staff')
    context = {'staffs':staffs,'current_user':current_user, 'user_role':user_role}
    return render(request, 'view-staff.html', context)

def try_update_staff(request, id):
    staff = Complete_info.objects.get(id_user=id)
    depts = Department.objects.all()
    context = {'staff':staff, 'depts':depts}
    return render(request, 'complete-staff-info.html', context)

def update_staff(request, id):
    staff = Complete_info.objects.get(id_user=id)
    if request.method == 'POST':
        f_name = request.POST['f_name']
        address = request.POST['address']
        role = request.POST['role']
        dept = request.POST['dept']

        staff.full_name = f_name
        staff.complete_address = address
        staff.role = role
        staff.department = dept
        staff.save()
        messages.info(request, 'Staff Updated successfully..')
        return redirect('view-staff')
    
def request_for_delete_staff(request, id):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    update = True
    staff = User.objects.get(id=id)
    context = {'staff':staff, 'update':update, 'current_user':current_user, 'user_role':user_role}
    return render(request, './hod-dept/request-for-delete-hod.html', context)

def delete_staff(request, id):
    staff = User.objects.get(id=id)
    staff.delete()
    messages.info(request, 'Staff Deleted Successfully...')
    return redirect('view-staff')


# ----------------------------------------------------------------------------------------------

# Login section
# ----------------------------------------------------------------------------------------------

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password!!')
            return redirect('login')
    return render(request, 'login.html')

# ----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

def schedule(request, id):
    sh_staff = Schedule.objects.get(id_user=id)
    return render(request, "schedule.html", {'sh_staff':sh_staff})

def view_schedule(request):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    sh_staffs = Schedule.objects.all()
    return render(request, "view-schedule.html", {'sh_staffs':sh_staffs, 'user_role':user_role})

def view_schedule2(request):
    current_user = User.objects.get(username=request.user)
    sh_staffs = Schedule.objects.all()
    return render(request, "view-schedule2.html", {'sh_staffs':sh_staffs, 'current_user':current_user})


def make_schedule(request, id):
    current_user = User.objects.get(username=request.user)
    user_role = Complete_info.objects.filter(user=current_user)
    sh_staff = Schedule.objects.get(id_user=id)
    for dept in user_role:
        pass
    if request.method == 'POST':
        name = request.POST['name']
        time_type = request.POST['time-type']
        time = request.POST['time']

        sh_staff.staff_name = name
        sh_staff.day_scheduled = time_type
        sh_staff.time_scheduled = time
        sh_staff.department = dept.department
        sh_staff.save()
        messages.info(request, "Staff scheduled successfully....")
        return redirect("view-schedule")
    


# -----------------------------------------------------------------------------------------------