"""pet_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.animal_list,name="animal_list"),
    path('detail/<int:animal_id>/', views.animal_detail,name="animal_detail"),
    path('create/', views.animal_create,name="animal_create"),
    path('update/<int:animal_id>/', views.animal_update,name="animal_update"),
     path('delete/<int:animal_id>/', views.animal_delete,name="animal_delete")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)