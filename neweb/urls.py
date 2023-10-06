"""
URL configuration for neweb project.

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
from django.contrib import admin
from django.urls import path
from neweb import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rum/', views.rum),
    path('beer/', views.beer),
    path('gin/', views.gin),
    path('brandy/', views.brandy),
    path('tequila/', views.tequila),
    path('vodka/', views.vodka),
    path('whiskey/', views.whiskey),
    path('about_us/', views.about_us, name='about'),
    path('login/', views.login,name= 'login'),
    path('sign_up/', views.sign_up,name='sign_up'),
    path('', views.home,name='home'),
    path('course/<courseID>', views.courseDetails),
    path('courseName/<courseName>',views.courseList),
]
