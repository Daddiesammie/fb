from django.contrib import admin
from django.urls import path
from formcollector import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.form_view, name='form'),
    path('success/', views.success_view, name='success'),
]
