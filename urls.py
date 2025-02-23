from django.contrib import admin
from django.urls import path, include
from accounts import views  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name='home'),  # Root URL now points to home
]