"""
URL configuration for Shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from phone import views
from computer import views as v1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('showphone/',views.showphone,name='show'),
    path('details/<int:id>/',views.details,name='details'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_register/',views.auth_register,name='auth_register'),
    path('auth_login/',views.auth_login,name='auth_login'),
    path('auth_logout/',views.auth_logout,name='auth_logout'),
    path('checkout/<int:id>/',views.checkout,name='checkout'),
    path('add_to_card/<int:id>/',views.add_to_card,name='add_to_card'),
    path('shopcomputer/',v1.shopcomputer,name='shopcomputer'),
    path('detail/<int:id>/',v1.detail,name='detail'),
    path('add_to_card/<int:id>/',v1.add_to_card,name='add_to_cardv1'),
     path('checkout2/<int:id>/',v1.checkout2,name='checkout2'),
    
   
    

]
