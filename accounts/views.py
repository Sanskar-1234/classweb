from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

# Sign-Up View
# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('user_home')  # Update as needed
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/sign_up.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user without logging in
            # Do not log the user in automatically
            return redirect('sign_in')  # Redirect to the home page (or another page of your choice)
    else:
        form = SignUpForm()

    return render(request, 'accounts/sign_up.html', {'form': form})

# Sign-In View
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def notes(request):
    return render(request, 'notes.html')

def sign_out(request):
    logout(request)
    return redirect('home')

def grade_8(request):
    return render(request, 'grade_8.html')  # Page for 8th grade notes

def grade_9(request):
    return render(request, 'grade_9.html')  # Page for 9th grade notes

def grade_10(request):
    return render(request, 'grade_10.html')  # Page for 10th grade notes

def grade_11(request):
    return render(request, 'grade_11.html')  # Page for 11th grade notes

def grade_12(request):
    return render(request, 'grade_12.html')

def admin_home(request):
    # Logic for the admin home page
    return render(request, 'admin_home.html')

def science(request):
    return render(request, 'science.html')

def commerce(request):
    return render(request, 'commerce.html')

def physics(request):
    return render(request, 'physics.html')

def science_12th(request):
    return render(request, 'science_12th.html')

def commerce_12th(request):
    return render(request, 'commerce_12th.html')

def chemistry(request):
    return render(request, 'chemistry.html')

def biology(request):
    return render(request, 'biology.html')

def economics(request):
    return render(request, 'economics.html')

def accountancy(request):
    return render(request, 'accountancy.html')

def business_studies(request):
    return render(request, 'business_studies.html')
    
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('admin_home')  # Redirect Admin to Admin Home
            return redirect('user_home')  # Redirect User to User Home
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/sign_in.html', {'form': form})

# Admin Home View
@login_required
def admin_home(request):
    if not request.user.is_superuser:
        return redirect('user_home')
    return render(request, 'accounts/admin_home.html')

# User Home View
@login_required
def user_home(request):
    if request.user.is_superuser:
        return redirect('admin_home')
    return render(request, 'accounts/user_home.html')
