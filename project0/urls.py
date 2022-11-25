"""project0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1_if_if_else/',a1_if_if_else,name = 'a1_if_if_else'),
    path('a1_if_elif_if/',a1_if_elif_if,name = 'a1_if_elif_if'),
    path('a2_nested_if/',a2_nested_if,name = 'a2_nested_if'),
    path('a2_forloop_/',a2_forloop_,name='a2_forloop_'),
]
