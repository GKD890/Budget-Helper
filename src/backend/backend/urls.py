"""backend URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from web_manage import views
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r'members',views.MemberView,'member')
router.register(r'records',views.RecordView,'record') 
# router.register(r'login',views.) 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('login/', csrf_exempt(views.LoginView.as_view()),name="login"), # TODO: not secure login url
    # path('logout/',csrf_exempt(views.LogoutView.as_view()),name="logout"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
