"""
URL configuration for student_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from . import views, student_views, staff_views, hods_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.Base, name='base'),
                  # login
                  path('', views.Login, name='login'),
                  path('dologin/', views.dologin, name='dologin'),
                  path('dologout/', views.dologout, name='dologout'),

                  # profile Update
                  path('pro file/', views.PROFILE, name='profile'),
                  path('profile/Update',views.profile_update, name='profile_update'),

                  # this is HOD Panel url
                  path('hod/home', hods_views.HOME, name='hod_home')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
