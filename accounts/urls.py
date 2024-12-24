from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('logout/', views.sign_out, name='logout'),
    path('home/', views.user_home, name='user_home'), 
    path('admin/home/', views.admin_home, name='admin_home'),
    path('notes/', views.notes, name='notes'),
    path('notes/8th/', views.grade_8, name='grade_8'),
    path('notes/9th/', views.grade_9, name='grade_9'),
    path('notes/10th/', views.grade_10, name='grade_10'),
    path('notes/11th/', views.grade_11, name='grade_11'),
    path('notes/12th/', views.grade_12, name='grade_12'),
    path('science/', views.science, name='science'),
    path('commerce/', views.commerce, name='commerce'),
    path('physics/', views.physics, name='physics'),
    path('chemistry/', views.chemistry, name='chemistry'),
    path('biology/', views.biology, name='biology'),
    path('economics/', views.economics, name='economics'),
    path('accountancy/', views.accountancy, name='accountancy'),
    path('business_studies/', views.business_studies, name='business_studies'),
    path('commerce_12th/', views.commerce_12th, name='commerce_12th'),
    path('science_12th/', views.science_12th, name='science_12th'),
]
