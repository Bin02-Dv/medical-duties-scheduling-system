from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medical-dr', views.add_medical_dr, name='medical-dr'),
    path('view-medical-dr', views.view_medical_dr, name='view-medical-dr'),
    path('hod', views.add_hod, name='hod'),
    path('view-hod', views.view_hod, name='view-hod'),
    path('add-department', views.add_department, name='add-department'),
    path('view-department', views.view_department, name='view-department'),
    path('staff', views.add_staff, name='staff'),
    path('view-staff', views.view_staff, name='view-staff'),
    path('schedule/<int:id>', views.schedule, name='schedule'),
    path('view-schedule', views.view_schedule, name='view-schedule'),
    path('view-schedule2', views.view_schedule2, name='view-schedule2'),
    path('make-schedule/<int:id>', views.make_schedule, name='make-schedule'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

# update - section

    path('try-update-dr/<int:id>', views.try_update_dr, name='try-update-dr'),
    path('try-update-hod/<int:id>', views.try_update_hod, name='try-update-hod'),
    path('update-hod/<int:id>', views.update_hod, name='update-hod'),
    path('try-update-staff/<int:id>', views.try_update_staff, name='try-update-staff'),
    path('update-staff/<int:id>', views.update_staff, name='update-staff'),
    path('try-update-dept/<int:id>', views.try_update_dept, name='try-update-dept'),
    path('update-dept/<int:id>', views.update_dept, name='update-dept'),

# delete - section

    path('request-for-delete-dr/<int:id>', views.request_for_delete_dr, name='request-for-delete-dr'),
    path('delete-dr/<int:id>', views.delete_dr, name='delete-dr'),
    path('request-for-delete-hod/<int:id>', views.request_for_delete_hod, name='request-for-delete-hod'),
    path('delete-hod/<int:id>', views.delete_hod, name='delete-hod'),
    path('request-for-delete-staff/<int:id>', views.request_for_delete_staff, name='request-for-delete-staff'),
    path('delete-staff/<int:id>', views.delete_staff, name='delete-staff'),
    path('request-for-delete-dept/<int:id>', views.request_for_delete_dept, name='request-for-delete-dept'),
    path('delete-dept/<int:id>', views.delete_dept, name='delete-dept'),
]